from db.db_connection import get_connection

class User:

    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

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