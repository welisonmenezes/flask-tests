from flask import Flask, render_template
from institucional import init
import dbtest

def create_app():
    app = Flask(__name__)

    # config app
    app.config.from_pyfile('config.py')
    print(app.config)

    # database test
    dbtest.configure(app)
    
    # blueprint test
    app.register_blueprint(init.bp)

    @app.errorhandler(404)
    def page404(error):
        return render_template('page-404.html'), 404

    return app