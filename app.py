from flask import Flask
from institucional import init

def create_app():
    app = Flask(__name__)

    # config app
    app.config.from_pyfile('config.py')
    print(app.config)
    
    app.register_blueprint(init.bp)

    return app