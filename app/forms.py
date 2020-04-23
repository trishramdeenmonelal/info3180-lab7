from flask_wtf import FlaskForm
from flask import render_template, request, redirect, url_for, flash 
from app import app
from wtforms import TextAreaField
from wtforms.validators import DataRequired 
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'])])
