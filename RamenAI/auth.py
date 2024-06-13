from flask import redirect, url_for, session
from .app import app, google
from authlib.jose import jwt


@app.route("/auth/login")
def auth_login():
    redirect_uri = url_for("authorized", _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/auth/logout")
def auth_logout():
    session.pop("user", None)
    return redirect(url_for("chat"))


@app.route("/auth/login/authorized")
def authorized():
    token = google.authorize_access_token()
    session["user"] = token["userinfo"]["name"]
    print(session["user"])
    return redirect(url_for("chat"))
