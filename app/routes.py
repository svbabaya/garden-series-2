from flask import request, session, render_template, redirect, url_for, flash
from app import app
from app.forms import MessageForm

# admin endpoints
@app.route('/admin')
def open_admin_page():
    return render_template('admin.html')

@app.route('/messages', methods=['POST', 'GET'])
def create_message():
    form = MessageForm(request.form)
    if request.method == 'POST' and form.validate():
        print('Make new object Message and add it to database')
        flash('New message created successful')
        return redirect(url_for('open_admin_page'))
    return render_template('messages.html', form=form)

@app.route('/messages/all')
def show_messages():
    print('Get all messages')
    return 'All messages'




@app.route('/')
def index():
    return 'Hi'



if __name__ == '__main__':
    app.run(debug=True)
