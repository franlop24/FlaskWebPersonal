import pymysql

def get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='example',
                                 db='platzi_blog',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection