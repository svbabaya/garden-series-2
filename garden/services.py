from garden.models import Message, Plant, Category, Display, Status, Article
from sqlalchemy.sql.expression import func
from garden.forms import MessageForm, PlantForm
from garden import db
from datetime import datetime

def get_category_plants_for_render(category_name):
    plants = Plant.query.filter(Plant.category == category_name,
                                Plant.status != 'DELETED',
                                Plant.display == 'enabled').all()
    return plants

def get_quantity_categories():
    dict = {}
    for cat in Category:
        quantity = Plant.query.filter(Plant.category == cat.name,
                                Plant.status != 'DELETED',
                                Plant.display == 'enabled').count()
        dict[cat.name] = quantity
    return dict

def get_plant(id):
    plant = Plant.query.filter(Plant.id == id).first()
    return plant

def get_message_for_render():
    # ToDo add analyze of priority, duration of show, existing of news and absolute
    message = Message.query.filter(Message.priority == 'normal',
                                           Message.status != 'DELETED',
                                           Message.display == 'enabled').order_by(func.random()).first()
    return message




# def get_all_messages():
#     return Message.query.all()

def get_live_messages():
    return Message.query.filter(Message.status != Status.DELETED).all()

def get_message_by_id(message_id):
    return Message.query.filter(Message.id == message_id).first()

def create_message(form: MessageForm):
        text = form.text.data
        author = form.author.data
        priority = form.priority.data
        
        if form.display.data == True:
            display = Display.enabled
        else: 
            display = Display.disabled

        message = Message(text=text, 
                          author=author, 
                          priority=priority, 
                          display=display)
        db.session.add(message)
        db.session.commit()

def patch_message(form: MessageForm, message_id):
    message = get_message_by_id(message_id)
    if message:
        message.text = form.text.data
        message.author = form.author.data
        message.priority = form.priority.data

        if form.display.data == True:
            message.display = Display.enabled
        else: 
            message.display = Display.disabled

        message.status = Status.UPDATED
        message.timestamp = datetime.now()
        db.session.commit()
    else:
        print('This id doesn\'t exist')     

def delete_message(message_id):
    message = get_message_by_id(message_id)
    if message:
        message.status = Status.DELETED
        message.timestamp = datetime.now()
        db.session.commit()
    else:
        print('This id doesn\'t exist')  
