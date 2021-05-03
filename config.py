
import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:12345@localhost/blogpost'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql://gkfqbhhevqcfnd:db4d3d926414b13d841f3e32931ae4bb9407aa333479a410534e283097f97e52@ec2-34-200-94-86.compute-1.amazonaws.com:5432/d9tuj4uncf9us6?sslmode=require'
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

class TestConfig(Config):
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig

}