from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail



# Initializing application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fbd6ee00a61d3489e582407ab0284ea4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from app.auth import views