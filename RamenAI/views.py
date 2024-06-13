import functools
from flask import render_template, redirect, url_for, flash, session
from .app import app
from .auth import google


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if "user" not in session:
            flash("Por favor ingresa a sesión")
            return redirect(url_for("login_get"))

        return view(**kwargs)

    return wrapped_view


@app.get("/login")
def login_get():
    return render_template("login.html")


@app.post("/login")
def login_post():
    redirect_uri = url_for("authorized", _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/logout")
def logout():
    session.pop("user", None)
    print(session)
    flash("Has cerrado sesión exitosamente")
    return redirect(url_for("login_get"))


@app.route("/")
@login_required
def chat():
    return render_template("chat.html")
