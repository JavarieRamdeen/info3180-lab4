from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    file = FileField('image', validators=[FileRequired(),FileAllowed(['jpg','png'], 'Images only!')])