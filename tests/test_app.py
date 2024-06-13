from flask import session, g, url_for
from unittest.mock import patch
from ramenai.main import app
import ramenai.views

# import ramenai.db
import secrets


def test_login_despliega(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Log In con Google" in response.data


def test_login_redirige_google(client):
    response = client.post("/login")
    assert response.status_code == 302
    assert "location" in response.headers
    redirect_url = response.headers["location"]
    assert redirect_url.startswith("https://accounts.google.com/o/oauth2/v2/auth")


@patch("ramenai.auth.google.authorize_access_token")
def test_authorized(mock_authorize_access_token, client):
    mock_authorize_access_token.return_value = {"userinfo": {"name": "Test User"}}
    with app.app_context():
        response = client.get("/auth/login/authorized", follow_redirects=False)
        assert response.status_code == 302
        assert response.headers["Location"] == "/"

    with client.session_transaction() as sess:
        assert sess["user"] == "Test User"


def test_logout(client):
    with client.session_transaction() as sess:
        sess["user"] = "Test User"
    response = client.get("/logout", follow_redirects=True)

    assert response.status_code == 200
    assert "Has cerrado sesión exitosamente" in response.data.decode("utf-8")

    with client.session_transaction() as sess:
        assert "user" not in sess
    assert response.request.path == "/login"


def test_chat_ok(client):
    with client.session_transaction() as sess:
        sess["user"] = "Test User"
    response = client.get("/")
    assert response.status_code == 200
    assert "HOLA PRUEBA" in response.data.decode("utf-8")


def test_chat_error(client):
    response = client.get("/", follow_redirects=True)
    assert len(response.history) == 1
    assert response.history[0].status == "302 FOUND"
    assert response.request.path == "/login"
    assert "Por favor ingresa a sesión" in response.data.decode("utf-8")
