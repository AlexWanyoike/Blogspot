from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from config import config_options
from flask_login import LoginManager 
from flask_bootstrap import Bootstrap
from flask_uploads import IMAGES, UploadSet,configure_uploads


db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    

    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    #simple.init_app(app)

    configure_uploads(app,photos)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

