from flask import Flask

# Initializing application
app = Flask(__name__)

from app.auth import views