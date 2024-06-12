from flask import render_template, request, redirect, url_for, abort, flash, session, g
from .app import app

@app.route("/")
def lista():
    return render_template(
        "base.html"
    )