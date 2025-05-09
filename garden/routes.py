from flask import request, session, render_template, redirect, url_for, flash
from garden import app, db
from garden.models import Message, Display, Category, Plant
from garden.forms import MessageForm, PlantForm

from . import settings

import os
from flask import current_app, send_from_directory, abort
from werkzeug.utils import secure_filename

from . import services

# from pathlib import Path
# import jsonify



### admin
@app.route('/admin/')
def open_admin_page():
    return render_template('admin/admin.html', 
                           settings=settings)



## messages
@app.route('/admin/message/', methods=('POST', 'GET'))
def create_message():
    form = MessageForm(request.form)
    if request.method == 'POST' and form.validate():
        services.create_message(form)
        flash('New message created successful')
        return redirect(url_for('open_admin_page'))
    return render_template('admin/create_message.html', 
                           form=form, 
                           settings=settings)

@app.route('/admin/messages/')
def show_live_messages():
    messages = services.get_live_messages()
    return render_template('admin/messages.html', 
                           messages=messages, 
                           settings=settings)

@app.route('/admin/message/<int:message_id>', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def handle_message(message_id):
    if request.method == 'POST':
        method = request.form.get('_method', '').upper()

        if method == 'DELETE':
            services.delete_message(message_id)
            messages = services.get_live_messages()
            return render_template('admin/messages.html', 
                                   messages=messages, 
                                   settings=settings)
        elif method == 'PATCH':
            form = MessageForm(request.form)
            message = services.get_message_by_id(message_id)
            if form.validate():
                services.patch_message(form, message_id)
                flash('Message patched successful')
                return redirect(url_for('show_live_messages'))
            
    elif request.method == 'GET':
            message = services.get_message_by_id(message_id)
            form = MessageForm()
            form.text.data = message.text
            form.author.data = message.author
            form.priority.data = message.priority.name

            if message.display == Display.enabled:
                form.display.data = True
            else:
                form.display.data = False    

            return render_template('admin/edit_message.html', 
                                   form=form,
                                   message=message,
                                   settings=settings)



## plants
@app.route('/admin/plant/', methods=('POST', 'GET'))
def create_plant():
    form = PlantForm(request.form)
    if request.method == 'POST' and form.validate():
        services.create_plant(form)
        flash('New plant created successful')
        return redirect(url_for('open_admin_page'))
    return render_template('admin/create_plant.html', 
                           form=form, 
                           settings=settings)

@app.route('/admin/plants/')
def show_live_plants():
    plants = services.get_live_plants()
    return render_template('admin/plants.html', 
                           plants=plants, 
                           settings=settings)

@app.route('/admin/plant/<int:plant_id>', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def handle_plant(plant_id):
    if request.method == 'POST':
        method = request.form.get('_method', '').upper()

        if method == 'DELETE':
            services.delete_plant(plant_id)
            plants = services.get_live_plants()
            return render_template('admin/plants.html', 
                                   plants=plants, 
                                   settings=settings)
        elif method == 'PATCH':
            form = PlantForm(request.form)
            plant = services.get_plant_by_id(plant_id)
            if form.validate():
                services.patch_plant(form, plant_id)
                flash('Plant patched successful')
                return redirect(url_for('show_live_plants'))
            
    elif request.method == 'GET':
            plant = services.get_plant_by_id(plant_id)
            form = PlantForm()
            form.name.data = plant.name
            form.category.data = plant.category.name
            form.code.data = plant.code

            form.intro.data = plant.intro
            form.thumbnail.data = plant.thumbnail
            form.location.data = plant.location.name

            if plant.display == Display.enabled:
                form.display.data = True
            else:
                form.display.data = False    

            return render_template('admin/edit_plant.html', 
                                   form=form,
                                   plant=plant,
                                   settings=settings)



### view endpoints
@app.route('/')
@app.route('/index/')
def index():
    current_message = services.get_message_for_render()
    quantities = services.get_quantity_categories()
    return render_template ('view/index.html', 
                            message=current_message, 
                            categories=Category,
                            quantities=quantities,
                            quantity=100,
                            settings=settings)

@app.route('/plants/category/<category_name>/')
def show_category(category_name):
    plants = services.get_category_plants_for_render(category_name)
    return render_template('view/category.html', 
                           category_title=Category[category_name].value['title'],
                           plants=plants,
                        #    quantity=services.get_quantity(plants),
                           quantity=services.get_quantity_categories()[category_name],
                           settings=settings)

@app.route('/plants/<plant_id>/')
def show_plant(plant_id):
    plant = services.get_plant_by_id(plant_id)

    # ToDo get all articles about current plant and send to template

    return render_template('view/plant.html',
                           plant_id=plant.id, 
                           plant_name=plant.name, 
                           category=plant.category,
                           settings=settings)

@app.route('/plant/<plant_id>/location')
def show_map(plant_id):
    plant = services.get_plant_by_id(plant_id)
    return render_template('view/location.html',
                           plant_id=plant.id,
                           plant_name=plant.name,
                           category=plant.category,
                           location=plant.location.value,
                           settings=settings)

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
