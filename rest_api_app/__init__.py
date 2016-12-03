from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

# Create a flask app and set a random secret key
# Create the app

# Define the WSGI application object
app = Flask(__name__)
# Configurations
app.config.from_object('config')
app.secret_key = os.urandom(24)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from rest_api_app import controllers, models

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
