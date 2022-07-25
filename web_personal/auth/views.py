########### Imports Flask & Python ##########
from flask import redirect, render_template, Blueprint, url_for
from werkzeug.security import generate_password_hash

from db.db_connection import get_connection

########### Imports Forms ##########
from .forms import LoginForm, RegisterForm

auth_blueprint = Blueprint('auth', __name__)

############ Rutas Login ############
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        return render_template('admin/index.html', email=email)

    return render_template('auth/login.html', form=form)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():
        name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        ############ Cifrado de Password ###########
        hashed_password = generate_password_hash(password)
        phone = form.phone.data
        is_married = form.is_married.data
        gender = form.gender.data

        conn = get_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (name, last_name, email, password, phone, is_married, gender) "
            sql += f"VALUES ('{name}', '{last_name}', '{email}', '{hashed_password}', '{phone}', '{is_married}', '{gender}')"
            cursor.execute(sql)
            conn.commit()
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)