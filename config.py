import os
DEBUG = True
SECRET_KEY = os.urandom(24)
SQLALCHEMY_TRACK_MODIFICATIONS = False
HOST = '127.0.0.1'
PORT ='3306'
USERNAME = 'root'
PASSWORD = ''
DB_NAME = 'ICBC'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.format(
    username=USERNAME,password=PASSWORD,host=HOST,port=PORT,db=DB_NAME
)
SQLALCHEMY_DATABASE_URI = DB_URI

