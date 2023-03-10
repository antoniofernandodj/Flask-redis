from flask import Flask
from src import views


def create_app():
    app = Flask(__name__)
    views.init_app(app)
    return app
