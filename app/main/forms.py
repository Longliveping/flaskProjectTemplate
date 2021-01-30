from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, widgets, SelectField, \
    BooleanField, FieldList, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired, Length

class TryingForm(FlaskForm):
    index = StringField()
    check = BooleanField()
    submit = SubmitField()
    exit = SubmitField()
