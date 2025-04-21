from flask import request, session, render_template, redirect, url_for, flash, send_from_directory
from garden import app, db
from garden.models import Message, Display, Category
from garden.forms import MessageForm

from sqlalchemy.sql.expression import func

import random
# import jsonify

# admin endpoints
@app.route('/admin/')
def open_admin_page():
    return render_template('admin.html')

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
    return render_template('message.html', form=form)

@app.route('/admin/messages/')
def show_all_messages():
    messages = Message.query.all()
    return render_template('messages.html', messages=messages)

# ToDo make edit form for message
# @app.route('/admin/message/<int:message_id>', methods=('GET', 'PATCH'))
# def edit_message(message_id):
#     return 'Open edit form for message'


@app.route('/')
@app.route('/index/')
def index():
    current_message = Message.query.filter(Message.priority == 'normal',
                                           Message.status != 'DELETED',
                                           Message.display == 'enabled').order_by(func.random()).first()
    return render_template ('index.html', message=current_message, categories=Category)

@app.route('/plants/<category_name>/')
def show_category_list(category_name):
    # ToDo get list of plants
    print('Get list of plants')
    return render_template('category.html', category_title=Category[category_name].value)






# ToDo export db to json
# @app.route('/export/messages/')
# def export_messages():
#   data = Message.query.all()
#   return jsonify(data) 


if __name__ == '__main__':
    app.run(debug=True)
