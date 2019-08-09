from flask import Flask
from institucional import init
import dbtest

def create_app():
    app = Flask(__name__)

    # config app
    app.config.from_pyfile('config.py')
    print(app.config)

    dbtest.configure(app)
    
    
    app.register_blueprint(init.bp)

    return app