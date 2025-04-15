from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length
 
class MessageForm(FlaskForm):
    text = TextAreaField('text: ', validators=[DataRequired('Введите текст сообщения'), Length(min=4, max=400)])
    author = StringField('author: ', validators=[DataRequired(), Length(min=4, max=80)])
    priority = SelectField('priority: ', choices=[(0, 'low'), (1, 'normal'), (2, 'news'), (3, 'general')])
    display = BooleanField('display: ', default=False)
    submit = SubmitField('upload')
