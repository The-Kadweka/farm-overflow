import os

class Config:
    """
    This is the class which will contain the general configurations
    """
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:qwerty12@localhost/farmers'
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    MAIL_PASSWORD='Nairobi001'
    MAIL_USERNAME='developersjuniors@gmail.com'
    SECRET_KEY='1234'
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:qwerty12@localhost/farmers' 
    DEBUG = True
  

class TestConfig(Config):
    """
    This is the class which will contain the test configurations
    """
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:qwerty12@localhost/farmers'


config_options = {
'development':DevConfig,
'production':ProdConfig,
'tests' : TestConfig
}

    