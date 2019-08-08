from flask import Flask
from institucional import init

def create_app():
    app = Flask(__name__)

    app.register_blueprint(init.bp)

    app.debug = True
    return app