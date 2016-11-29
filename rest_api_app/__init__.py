from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

# Create a flask app and set a random secret key
# Create the app

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.urandom(24)
db.init_app(app)

from rest_api_app import main_rest, models, post_requests



