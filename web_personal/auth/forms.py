from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, 
                    SubmitField, EmailField, 
                    IntegerField, RadioField, 
                    SelectField, TextAreaField)
from wtforms.validators import DataRequired, Email, EqualTo


################# Formularios de WTForms ##################
class LoginForm(FlaskForm):
    username = EmailField('Username', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), EqualTo('confirm_password', message='Las contraseñas no coinciden')])
    confirm_password = PasswordField('Confirmar contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar')

########### TODO: Formularios de Profile ###########
class ProfileForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    last_name = StringField('Apellidos', validators=[DataRequired()])
    phone = IntegerField('Teléfono')
    is_married = RadioField('Estado Civil', choices=[('True', 'Casado'), ('False', 'Soltero')])
    gender = SelectField('Genero', choices=[('male', 'Masculino'), ('female', 'Femenino'), ('other', 'Otro')])
