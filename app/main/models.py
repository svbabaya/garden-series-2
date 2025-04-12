from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()

class Status(enum.Enum):
    CREATED = 0
    UPDATED = 1
    DELETED = 2

class Category(enum.Enum):
    empty = 0
    tree = 1
    fruit_tree = 2
    bush = 3
    fruit_bush = 4
    herb_perennial_ornamental_plant = 5
    herb_annual_ornamental_plant = 6
    herb_perennial_wild_plant = 7   

class Location(enum.Enum):
    unknown = 0 
    zone_1 = 1
    zone_2 = 2
    zone_3 = 3
    zone_4 = 4
    zone_5 = 5

class Composition(enum.Enum):
    img_top = 1
    img_right = 2
    img_bottom = 3
    img_left = 4
    text_only = 5

class Priority(enum.Enum):
    low = 0
    normal = 1
    news = 2
    general = 3   

class Display(enum.Enum):
    disabled = 0
    enabled = 1

# ToDo does it need to add hash for ident items in db

class Plant(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.Enum(Category), nullable=False, default=Category.empty)
    intro = db.Column(db.String(300), unique=True, nullable=False)
    thumbnail = db.Column(db.String(100), nullable=False, default='default.jpg')
    location = db.Column(db.Enum(Location), nullable=False, default=Location.unknown)
    status = db.Column(db.Enum(Status), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    display = db.Column(db.Enum(Display), nullable=False, default=Display.disabled)
    articles = db.relationship('Article', backref='plant',  lazy='dynamic', cascade='all, delete-orphan')
    def __repr__(self):
        return f'<Plant {self.name}>'

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False, unique=True)
    photo = db.Column(db.String(100), nullable=True, default='default.jpg')  
    composition = db.Column(db.Enum(Composition), nullable=False, default=Composition.img_top)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    display = db.Column(db.Enum(Display), nullable=False, default=Display.disabled)
    def __repr__(self):
        return f'<Article {self.id}>'

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.Enum(Priority), nullable=False, default=Priority.low)
    status = db.Column(db.Enum(Status), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    display = db.Column(db.Enum(Display), nullable=False, default=Display.disabled)
    def __repr__(self):
        return f'<Message {self.id}>'
