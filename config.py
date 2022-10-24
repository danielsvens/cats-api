import os

DEBUG = False
TESTING = False
DB_URI = f'postgresql://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("AWS_RDS_HOST")}:{os.environ.get("DB_PORT")}/{os.environ.get("DB_NAME")}'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
USE_RELOADER = False
ENV = 'development'
PORT = 80
