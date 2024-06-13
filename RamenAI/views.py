from flask import render_template, request, redirect, url_for, flash, session, jsonify
from .app import app
from .db import get_db
from .auth import google
import openai
import datetime
import functools
import os
from pymongo import MongoClient


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
    return redirect(url_for("chat"))


@app.route("/")
@login_required
def chat():
    return render_template("chat.html")


# Setup OpenAI API key from app.config
openai.api_key = os.getenv('OPENAI_API_KEY')

conversation_history = [
    {"role": "system", "content": "Eres un excelente cocinero y experto en ramen. Eres bueno en descubrir e inventar nuevas formas de preparar y disfrutar ramen en casa. Das recetas sencillas e instrucciones concisas. Siempre contesta en máximo 500 tokens."}
]

@app.route('/api/maruchat', methods=['POST'])
def maruchat():
    try:
        db = get_db()
        conversations_collection = db['conversations']

        user_id = request.headers.get('UserId')  # Assuming userId is passed in headers
        user_input = request.json.get('userInput')

        if user_input:
            conversation_history.append({"role": "user", "content": user_input})

        # Using openai for text generation
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Replace with the appropriate model
            messages=conversation_history,
            max_tokens=500,  # Adjust as needed
            stop=None  # Customize stop conditions if required
        )
        print(response.choices[0].message)

        chat_response = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": chat_response})

        # Save conversation to MongoDB or any other storage
        conversation_records = [{
            "userId": user_id,
            "role": message['role'],
            "content": message['content'],
            "timestamp": datetime.datetime.now()
        } for message in conversation_history]

        conversations_collection.insert_many(conversation_records)

        return jsonify({"chatResponse": chat_response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

def get_db():
    # Placeholder for database connection
    client = MongoClient(os.getenv('MONGO_URI'))
    return client['your_database_name'] 