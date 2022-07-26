########### Imports Flask & Python ##########
from flask import redirect, render_template, Blueprint, url_for
from werkzeug.security import generate_password_hash

from db.db_connection import get_connection
from .models import get_user_by_username_and_password

########### Imports Forms ##########
from .forms import LoginForm, RegisterForm

auth_blueprint = Blueprint('auth', __name__)

############ Rutas Login ############
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = get_user_by_username_and_password(username, password)

        if user:
            return "Bienvenido!"
            #return render_template('admin/index.html', message='Bienvenido')

    return render_template('auth/login.html', form=form)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        ############ Cifrado de Password ###########
        hashed_password = generate_password_hash(password)

        conn = get_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (username, email, password) "
            sql += f"VALUES ('{username}', '{email}', '{hashed_password}')"
            cursor.execute(sql)
            conn.commit()
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)