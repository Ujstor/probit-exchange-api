import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask

load_dotenv(find_dotenv())

KEY = os.environ.get('KEY')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = KEY

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app