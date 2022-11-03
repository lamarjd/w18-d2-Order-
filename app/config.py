#  create a Configuration class that has a static variable named SECRET_KEY. Then, set it to the value from the environment variable of the same name.

import os


class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # connects Alchemy to the db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False