from flask_login import UserMixin
from db.db_connection import get_connection
from werkzeug.security import check_password_hash

class User(UserMixin):

    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

def get_user_by_id(id):
    ####### Consultar en BD por id
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM users WHERE id = '{id}'"
        cursor.execute(sql)
        user = cursor.fetchone()
        if user:
            return User(user['id'], user['username'], user['email'])
        else:
            return None

def get_user_by_username_and_password(username, password):
    ####### Consultamos user por username ##########
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(sql)
        user = cursor.fetchone()
        if user:
            ####### Comparamos password #######
            if check_password_hash(user['password'], password):
                return User(user['id'], user['username'], user['email'])
            else:
                return None
        else:
            return None

def get_user_by_email(email):
    ######## Consultar en BD por email
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM users WHERE email = '{email}'"
        cursor.execute(sql)
        user = cursor.fetchone()
        if user:
            return User(user['id'], user['username'], user['email'])
        else:
            return None

def get_user_by_username(username):
    ####### Cosultar en BD por username
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(sql)
        user = cursor.fetchone()
        if user:
            return User(user['id'], user['username'], user['email'])
        else:
            return None