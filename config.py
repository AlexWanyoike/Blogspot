
import os

class Config:
    '''
    General configuration parent class
    '''

    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql://gkfqbhhevqcfnd:db4d3d926414b13d841f3e32931ae4bb9407aa333479a410534e283097f97e52@ec2-34-200-94-86.compute-1.amazonaws.com:5432/d9tuj4uncf9us6?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass

    # simple mde  configurations
    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:12345@localhost/blogpost'
   

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    #SQLALCHEMY_DATABASE_URI = 
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:12345@localhost/blogpost'
    DEBUG = True
    ENV = 'development'

    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:12345@localhost/blogpost'
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig

}