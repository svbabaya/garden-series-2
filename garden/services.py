from garden.models import Message, Plant, Category, Article
from sqlalchemy.sql.expression import func

# def get_quantity(list):
#     quantity = len(list)
#     return quantity

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




# Messages
def get_message_for_render():
    message = Message.query.filter(Message.priority == 'normal',
                                           Message.status != 'DELETED',
                                           Message.display == 'enabled').order_by(func.random()).first()
    return message