from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'usohxspjv3lkjpnc8po6p9gbzbe7w6ws'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app