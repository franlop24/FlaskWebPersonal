########### Imports Flask & Python ##########
from flask import (redirect, render_template, request, 
                Blueprint, url_for)
from werkzeug.security import generate_password_hash

from flask_login import login_user, login_required, logout_user

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
            login_user(user)

            next = request.args.get('next')
            
            return redirect(next or url_for('index'))

    return render_template('auth/login.html', form=form)

@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

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