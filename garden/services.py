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


# def get_all_plants():
#     return Plant.query.all()

def get_live_plants():
    return Plant.query.filter(Plant.status != Status.DELETED).all()

def get_plant_by_id(plant_id):
    return Plant.query.filter(Plant.id == plant_id).first()

def create_plant(form: PlantForm):
    name = form.name.data
    category = form.category.data
    code = form.code.data
    intro = form.intro.data
    thumbnail = form.thumbnail.data
    location = form.location.data

    if form.display.data == True:
        display = Display.enabled
    else: 
        display = Display.disabled

    plant = Plant(name=name,
                category=category,
                code=code,
                intro=intro,
                thumbnail=thumbnail,
                location=location,
                display=display)
    db.session.add(plant)
    db.session.commit()

def patch_plant(form: PlantForm, plant_id):
    plant = get_plant_by_id(plant_id)
    if plant:
        plant.name = form.name.data
        plant.category = form.category.data
        plant.code = form.code.data

        plant.intro = form.intro.data
        plant.thumbnail = form.thumbnail.data
        plant.location = form.location.data

        if form.display.data == True:
            plant.display = Display.enabled
        else: 
            plant.display = Display.disabled

        plant.status = Status.UPDATED
        plant.timestamp = datetime.now()
        db.session.commit()
    else:
        print('This id doesn\'t exist')

def delete_plant(plant_id):
    plant = get_plant_by_id(plant_id)
    if plant:
        plant.status = Status.DELETED
        plant.timestamp = datetime.now()
        db.session.commit()
    else:
        print('This id doesn\'t exist')  
