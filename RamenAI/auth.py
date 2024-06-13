from flask import redirect, url_for, session
from .app import app, google
from authlib.jose import jwt


@app.route("/auth/login/authorized")
def authorized():
    token = google.authorize_access_token()
    session["user"] = token["userinfo"]["name"]
    print(token["userinfo"])
    print(session["user"])
    return redirect(url_for("chat"))
