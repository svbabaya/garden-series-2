from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(300), unique=True, nullable=False)
    author = db.Column(db.String(100))
    priority = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f'<Phrase {self.id}>'

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    describe = db.Column(db.Text(1000), nullable=False)
    location = db.Column(db.Integer, nullable=False)
    photos = db.Column(db.String(100), nullable=False, default='default.jpg')
    status = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return f'<Article {self.id}>'
    
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    