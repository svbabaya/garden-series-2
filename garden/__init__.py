from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
     	'sqlite:///' + os.path.join(basedir, 'garden.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'development_secret_key'
app.config['JSON_AS_ASCII'] = False

app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
app.config['UPLOAD_ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

db = SQLAlchemy(app)

with open(os.path.join(basedir, 'settings.json'), mode='r', encoding='utf-8') as read_file:
    settings = json.load(read_file)

from garden import routes, models
