from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
     	'sqlite:///' + os.path.join(basedir, 'garden.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'development_secret_key'
app.config['JSON_AS_ASCII'] = False
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
app.config['UPLOAD_ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

db = SQLAlchemy(app)

from garden import routes, models
