from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()

class Status(enum.Enum):
    EMPTY = 0
    CREATED = 1
    UPDATED = 2
    DELETED = 3

class Category(enum.Enum):
    empty = 0
    tree = 1
    fruit_tree = 2
    bush = 3
    fruit_bush = 4
    herb_perennial_ornamental_plant = 5
    herb_annual_ornamental_plant = 6
    herb_perennial_wild_plant = 7   

class Composition(enum.Enum):
    IMG_TOP = 1
    IMG_RIGHT = 2
    IMG_BOTTOM = 3
    IMG_LEFT = 4
    TEXT_ONLY = 5

class Priority(enum.Enum):
    ZERO = 0
    NORMAL = 1
    NEWS = 2
    ABSOLUTE = 3   

class Plant(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.Integer, nullable=False, default=Category.empty)
    intro = db.Column(db.String(300), nullable=False)
    thumbnail = db.Column(db.String(100), nullable=False, default='default.jpg')
    location = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=Status.EMPTY)
    date = db.Column(db.DateTime, default=datetime.now)
    articles = db.relationship('Article', backref='plant') # articles : attribute in model Plant, plant : attribute in model Article
    def __repr__(self):
        return f'<Plant {self.name}>'

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(3000), nullable=False)
    photo = db.Column(db.String(100), nullable=True, default='default.jpg')  
    composition = db.Column(db.Integer, nullable=False, default=Composition.IMG_TOP)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=Status.EMPTY)
    date = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return f'<Article {self.id}>'

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(300), unique=True, nullable=False)
    author = db.Column(db.String(100))
    priority = db.Column(db.Integer, nullable=False, default=Priority.ZERO)
    status = db.Column(db.Integer, nullable=False, default=Status.EMPTY)
    date = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return f'<Message {self.id}>'
