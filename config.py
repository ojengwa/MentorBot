import os


class BaseConfig(object):

    """docstring for Config"""

    SECRET_KEY = os.getenv('SECRET_KEY', default='my_not_so_secret_key')


class DevConfig(BaseConfig):

    """docstring for Dev"""

    DEBUG = True


class ProdConfig(BaseConfig):

    """docstring for ProdConfig"""
    DEBUG = False


class TestConfig(BaseConfig):

    """docstring for TestConfig"""
    DEBUG = True
