################## Imports Flask & Python Modules ##################
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, TextAreaField, FileField, URLField)
from wtforms.validators import DataRequired, URL, Length
from flask_wtf.file import FileAllowed

class FormProjectBase(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=10, max=50)])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    url = URLField('URL', validators=[DataRequired(), URL()])
    image = FileField('Imagen', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])

class NewProjectForm(FormProjectBase):    
    submit = SubmitField('Crear')

class UpdateProjectForm(FormProjectBase):
    submit = SubmitField('Actualizar')