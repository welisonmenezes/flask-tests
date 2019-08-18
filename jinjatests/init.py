import os
from flask import current_app, Blueprint, render_template

jinja_bp = Blueprint('jinja-tests', __name__, url_prefix='/jinja-tests', template_folder='templates/')

@jinja_bp.route('/')
def index():
    felinos = ['Leão', 'Tigre', 'Leopardo', 'Onça']
    myhtml = '<h3>Test safe</h3>'
    numbers = [1,3,5,2,4,9,4]
    def getName():
        return 'Welison Menezes'
    return render_template('index.html', felinos=felinos, myhtml=myhtml, numbers=numbers, getName=getName), 200

@jinja_bp.app_template_filter('add_sign')
def caps(text):
    return text + '-welisonmenezes'
