from flask import render_template, request, redirect, url_for, abort, flash, session, g
from .app import app

""" def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'uid' not in session:
            flash("Por favor ingresa a sesión")
            return redirect(url_for('login_get'))

        return view(**kwargs)

    return wrapped_view """

@app.get("/login")
def login_get():
    return render_template("login.html")

@app.post("/login")
def login_post():
    return redirect(url_for('chat', _method="GET"))

@app.route("/")
def chat():
    return render_template("chat.html")
