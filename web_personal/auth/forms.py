from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, 
                    SubmitField, EmailField, ValidationError)
from wtforms.validators import DataRequired, Email, EqualTo

from .models import get_user_by_email, get_user_by_username

################# Formularios de WTForms ##################
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), EqualTo('confirm_password', message='Las contraseñas no coinciden')])
    confirm_password = PasswordField('Confirmar contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    ######## Validar Correo Unico #########
    def validate_email(self, field):
        ######## Consultar si el correo existe en la base de datos #######
        if get_user_by_email(field.data):
            raise ValidationError('El correo ya existe')

    ######## Validar Username Unico #########
    def validate_username(self, field):
        ######## Consultar si el username existe en la base de datos #######
        if get_user_by_username(field.data):
            raise ValidationError('El username ya existe')

########### TODO: Formularios de Profile ###########
class ProfileForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    last_name = StringField('Apellidos', validators=[DataRequired()])
    #phone = IntegerField('Teléfono')
    #is_married = RadioField('Estado Civil', choices=[('True', 'Casado'), ('False', 'Soltero')])
    #gender = SelectField('Genero', choices=[('male', 'Masculino'), ('female', 'Femenino'), ('other', 'Otro')])
