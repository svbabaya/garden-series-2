from flask import request, render_template, jsonify
from app import app
from app.forms import MessageForm

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    form = MessageForm()
    if form.validate_on_submit():
        print(form.text.data)
        print(form.author.data)
        print(form.priority.data)
        print(form.display.data)
    return render_template('admin.html', form=form)



@app.route('/')
def index():
    return 'Hi!'

@app.route('/form', methods = ['POST'])
def form_handler():
    name = request.form['name']
    return f'Name: {name}'

@app.route('/json')
def json_handler():
    message = {'name': 'Serge'}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
