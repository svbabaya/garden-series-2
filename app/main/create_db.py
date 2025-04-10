import sys
sys.dont_write_bytecode = True

from flask import Flask
from models import db, Plant, Article, Message

# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'garden.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.root_path}/garden.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
	    db.create_all()
      