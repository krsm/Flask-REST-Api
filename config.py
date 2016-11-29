import os

# current working dir
curDir = os.path.abspath(os.path.dirname(__file__))

PATH_DB = 'sqlite:///' + curDir + '/RESTAPI.db'

# Configure to use the database
SQLALCHEMY_DATABASE_URI = PATH_DB
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True # Turns on debugging features in Flask