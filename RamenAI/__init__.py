"""Asesor de ramen"""

__version__ = "0.1.0"
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Load configurations from environment variables
app.config['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

from .db import init_db

# Initialize the database
init_db()

from . import views
