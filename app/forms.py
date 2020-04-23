from flask_wtf import FlaskForm
from app import app
from wtforms import TextAreaField
from wtforms.validators import DataRequired 
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    Description = TextAreaField('Description', validators=[DataRequired()])
    Photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'])])
