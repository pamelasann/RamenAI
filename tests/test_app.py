from flask import session
from flask import g
from ramenai.main import app
import ramenai.views

# import ramenai.db
import secrets


def test_login_despliega(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Log In con Google" in response.data


def test_login_redirige_ok(client):
    response = client.post("/login", follow_redirects=True)
    assert len(response.history) == 1
    assert response.history[0].status == "302 FOUND"
    assert response.request.path == "/"
    assert b"HOLA PRUEBA" in response.data
