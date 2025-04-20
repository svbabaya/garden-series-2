import sys
sys.dont_write_bytecode = True

from flask import Flask
from garden.models import db, Plant, Article, Message, Priority, Status, Category, Composition, Location, Display

# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'garden.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.root_path}/garden.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

def initialize_database():    
    with app.app_context():
        db.create_all()
        plant_1 = Plant(
            name='Гинкго билоба', 
            category=Category.tree,
            code = '1.5',
            intro='Дерево, пережившее динозавров, древний ключ к ясности ума.', 
            # thumbnail='/', # default
            # location=Location.unknown, # default
            # status=Status.CREATED # default
            # display=Display.disabled # default
            )
        db.session.add(plant_1)
        db.session.flush()
    
        article_1 = Article(
            text='Гинкго двулопастный — высокое листопадное дерево. Во взрослом возрасте высотой до 40 м и диаметром ствола до 4,5 м. Листья имеют веерообразную форму, разделённую на две доли, и осенью становятся ярко-жёлтыми.',
            # photo='/', # default
            # composition=Composition.img_top, # default 
            plant_id=plant_1.id,  
            # status=Status.CREATED # default
            # display=Display.disabled # default
            )

        message_1 = Message(
            text='Следи за своим садом — вот моё правило. Ухаживай за цветами, а не гоняйся за бабочками, и тогда бабочки прилетят к тебе сами. Так жизнь и устроена.', 
            author='Мэттью МакКонахи', 
            # priority=Priority.low, # default
            # display=Display.disabled # default
            # status=Status.CREATED, # default
            )
    
        try:
            db.session.add_all([article_1, message_1])
            db.session.commit()
            print('Data updated')
        except Exception as e:
            db.session.rollback()
            print(f'Error: {e}')

if __name__ == '__main__':    
    initialize_database()
