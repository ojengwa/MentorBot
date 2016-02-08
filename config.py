import os


class BaseConfig(object):

    """docstring for Config"""

    SECRET_KEY = os.getenv('SECRET_KEY', default='my_not_so_secret_key')
    BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__name__)))
    SQLALCHEMY_ECHO = False
    GOOGLE_LOGIN_REDIRECT_SCHEME = 'http'
    GOOGLE_LOGIN_CLIENT_ID = os.getenv('CLIENT_ID', default='fvhbfsjhdghfjsghhihsifhgirhsuihrs')
    GOOGLE_LOGIN_CLIENT_SECRET = os.getenv('CLIENT_SECRET', default='fsdjhgsjfgygsufgreuyreg')


class DevConfig(BaseConfig):

    """docstring for Dev"""

    DEBUG = True
    PORT = 5000
    DATABASE_URL = "postgresql://postgres:[]@localhost:5433/mentorbot"
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    HOST = 'http://localhost:' + str(PORT)
    GOOGLE_LOGIN_REDIRECT_URI = HOST + '/login/google'


class ProdConfig(BaseConfig):

    """docstring for ProdConfig"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    HOST = 'https://andela-mentorbot.herokuapp.com'
    GOOGLE_LOGIN_REDIRECT_URI = HOST + '/login/google'


class TestConfig(BaseConfig):

    """docstring for TestConfig"""
    DEBUG = True
    HOST = '0.0.0.0'
    GOOGLE_LOGIN_REDIRECT_URI = HOST + '/login/google'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    LIVESERVER_PORT = 8001
    TESTING = True
