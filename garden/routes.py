from flask import request, session, render_template, redirect, url_for, flash
from garden import app, db
from garden.models import Message, Display, Category, Plant
from garden.forms import MessageForm, PlantForm

from sqlalchemy.sql.expression import func

import os
from flask import current_app, send_from_directory, abort
from werkzeug.utils import secure_filename

# from pathlib import Path

# import jsonify

### admin endpoints
@app.route('/admin/')
def open_admin_page():
    return render_template('admin/admin.html')

@app.route('/admin/message/', methods=('POST', 'GET'))
def create_message():
    form = MessageForm(request.form)
    if request.method == 'POST' and form.validate():
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

        flash('New message created successful')
        return redirect(url_for('open_admin_page'))
    return render_template('admin/message.html', form=form)

@app.route('/admin/messages/')
def show_all_messages():
    messages = Message.query.all()
    return render_template('admin/messages.html', messages=messages)

# ToDo make edit form for message
@app.route('/admin/message/<int:message_id>', methods=('GET', 'PATCH'))
def edit_message(message_id):
    return 'Open edit form for message'

@app.route('/admin/plant/', methods=('POST', 'GET'))
def create_plant():
    form = PlantForm(request.form)
    if request.method == 'POST' and form.validate():
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

        flash('New plant created successful')
        return redirect(url_for('open_admin_page'))
    return render_template('admin/plant.html', form=form)

@app.route('/admin/plants/')
def show_all_plants():
    plants = Plant.query.all()
    return render_template('admin/plants.html', plants=plants)

# ToDo make edit form for plant
@app.route('/admin/plant/<int:plant_id>', methods=('GET', 'PATCH'))
def edit_plant(plant_id):
    return 'Open edit form for plant'




### view endpoints
@app.route('/')
@app.route('/index/')
def index():
    current_message = Message.query.filter(Message.priority == 'normal',
                                           Message.status != 'DELETED',
                                           Message.display == 'enabled').order_by(func.random()).first()
    return render_template ('index.html', message=current_message, categories=Category)

@app.route('/plants/category/<category_name>/')
def show_category_list(category_name):
    plants = Plant.query.filter(Plant.category == category_name,
                                Plant.status != 'DELETED',
                                Plant.display == 'enabled')
    return render_template('category.html', 
                           category_title=Category[category_name].value['title'],
                           plants=plants)

@app.route('/plants/<plant_id>/')
def open_details_plant(plant_id):
    plant = Plant.query.filter(Plant.id == plant_id).first()

    # ToDo get all articles about current plant and send to template
    
    return render_template('item.html', 
                           plant_name=plant.name, 
                           category_name=plant.category.name)

@app.route('/plant/<plant_id>/location')
def open_map(plant_id):
    plant = Plant.query.filter(Plant.id == plant_id).first()

    #ToDo get location code and send to template

    return render_template('location.html',
                           plant_name=plant.name,
                           category_name=plant.category.name,
                           location=plant.location.value)

# @app.route('/uploads/<path:filename>')  # Обратите внимание на <path:filename>
# def send_file(filename):
#     # Безопасная обработка имени файла
#     safe_filename = secure_filename(os.path.basename(filename))
#     directory = os.path.dirname(filename)
#     print(safe_filename)
#     print(directory)
    
#     # Полный путь к файлу
#     file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], directory, safe_filename)
    
#     # Проверка существования файла
#     if not os.path.exists(file_path):
#         current_app.logger.error(f"File not found: {file_path}")
#         abort(404)
    
#     # Проверка что файл находится внутри UPLOAD_FOLDER (безопасность)
#     try:
#         file_path = os.path.realpath(file_path)
#         upload_folder = os.path.realpath(current_app.config['UPLOAD_FOLDER'])
#         if not file_path.startswith(upload_folder):
#             abort(403)
#     except:
#         abort(400)
    
#     # Отправка файла
#     return send_from_directory(
#         os.path.join(current_app.config['UPLOAD_FOLDER'], directory),
#         safe_filename)

@app.route('/uploads/<path:filename>')
def send_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

# ToDo export db to json
# @app.route('/export/messages/')
# def export_messages():
#   data = Message.query.all()
#   return jsonify(data) 


if __name__ == '__main__':
    app.run(debug=True)
