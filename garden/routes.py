from flask import request, session, render_template, redirect, url_for, flash, send_from_directory
from garden import app, db
from garden.models import Message, Display
from garden.forms import MessageForm
# import jsonify

# admin endpoints
@app.route('/admin/')
def open_admin_page():
    return render_template('admin.html')

@app.route('/messages/', methods=['POST', 'GET'])
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

        print(text)
        print(author)
        print(priority)
        print(display)

        message = Message(text=text, 
                          author=author, 
                          priority=priority, 
                          display=display)
        db.session.add(message)
        db.session.commit()

        flash('New message created successful')
        return redirect(url_for('open_admin_page'))
    return render_template('messages.html', form=form)




@app.route('/messages/all/')
def show_messages():
    print('Get all messages')
    return 'All messages'




@app.route('/')
def index():
    return 'Hi'


# ToDo export db to json
# @app.route('/export/messages/')
# def export_messages():
#   data = Message.query.all()
#   return jsonify(data) 




if __name__ == '__main__':
    app.run(debug=True)
