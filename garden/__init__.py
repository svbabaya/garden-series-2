from flask import Flask
from flask_sqlalchemy import SQLAlchemy # new
import os # new

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__)) # new
app.config['SQLALCHEMY_DATABASE_URI'] =\
     	'sqlite:///' + os.path.join(basedir, 'garden.sqlite') # new
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # new
app.config['SQLALCHEMY_ECHO'] = True # new
app.config['SECRET_KEY'] = 'development_secret_key'
app.config['JSON_AS_ASCII'] = False
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app) # new

from garden import routes, models
