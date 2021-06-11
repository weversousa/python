from flask import Flask
from brasileirao import configurations


def create_app():
    app = Flask(__name__)
    configurations.init_app(app)
    configurations.load_extensions(app)
    return app
