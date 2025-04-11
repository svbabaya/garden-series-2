import sys
sys.dont_write_bytecode = True

from flask import Flask
from models import db, Plant, Article, Message, Priority, Status, Category, Composition, Location

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


plant_1 = Plant('Гинкго билоба', 
                Category.tree, 
                'Дерево, пережившее динозавров, древний ключ к ясности ума.', 
                '/', 
                Location.zone_1, 
                Status.CREATED
                )

article_1 = Article('Гинкго двулопастный — высокое листопадное дерево. Во взрослом возрасте высотой до 40 м и диаметром ствола до 4,5 м. Листья имеют веерообразную форму, разделённую на две доли, и осенью становятся ярко-жёлтыми.',
                    '/', 
                    Composition.img_top, 
                    1, 
                    Status.CREATED
                    )

message_1 = Message('Следи за своим садом — вот моё правило. Ухаживай за цветами, а не гоняйся за бабочками, и тогда бабочки прилетят к тебе сами. Так жизнь и устроена.', 
                    'Мэттью МакКонахи', 
                    Priority.normal, 
                    Status.CREATED
                    )
