from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length
 
class MessageForm(FlaskForm):
    text = TextAreaField('text', validators=[DataRequired(), Length(min=4, max=400)])
    author = StringField('author', validators=[DataRequired(), Length(min=4, max=80)])
    priority = SelectField('priority', choices=[('low', 'low'), 
                                                  ('normal', 'normal'), 
                                                  ('news', 'news'), 
                                                  ('absolute', 'absolute')])
    display = BooleanField('display', default=False)
    submit = SubmitField('Save')

class PlantForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=3, max=40)])
    category = SelectField('category', choices=[('tree', 'tree'), 
                                                  ('fruit_tree', 'fruit_tree'), 
                                                  ('bush', 'bush'),
                                                  ('fruit_bush', 'fruit_bush'), 
                                                  ('herb_perennial_ornamental', 'herb_perennial_ornamental'),
                                                  ('herb_annual_ornamental', 'herb_annual_ornamental'),
                                                  ('herb_perennial_wild', 'herb_perennial_wild')])
    code = StringField('code', validators=[DataRequired(), Length(min=3, max=10)])
    intro = TextAreaField('intro', validators=[DataRequired(), Length(min=30, max=300)])
    thumbnail = StringField('thumbnail', validators=[DataRequired(), Length(min=5, max=50)])
    location = SelectField('location', choices=[('unknown', 'unknown'), 
                                                  ('zone_1', 'zone_1'),
                                                  ('zone_2', 'zone_2'),
                                                  ('zone_3', 'zone_3'), 
                                                  ('zone_4', 'zone_4'), 
                                                  ('zone_5', 'zone_5')])
    display = BooleanField('display', default=False)
    submit = SubmitField('Save')
