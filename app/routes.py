from flask import request, render_template, jsonify
from app import app

@app.route('/index')
def index():
    return 'Hi!'

@app.route('/')
def open_form():
    return render_template('form.html')

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
