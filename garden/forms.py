from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length
 
class MessageForm(FlaskForm):
    text = TextAreaField('text ', validators=[DataRequired(), Length(min=4, max=400)])
    author = StringField('author ', validators=[DataRequired(), Length(min=4, max=80)])
    priority = SelectField('priority ', choices=[('low', 'low'), 
                                                  ('normal', 'normal'), 
                                                  ('news', 'news'), 
                                                  ('absolute', 'absolute')])
    display = BooleanField('display ', default=False)
    submit = SubmitField('upload')
