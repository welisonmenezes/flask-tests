from flask import current_app, Blueprint, render_template

bp = Blueprint('institucional', __name__, url_prefix='/', template_folder='templates/')

@bp.route('/')
def index():
    paises = ['Brasil', 'Argentina', 'Estados Unidos', 'França']
    return render_template('home.html', paises=paises)


@bp.route('/contato')
def contato():
    return render_template('contato.html')


@bp.route('/sobre')
def sobre():
    return render_template('sobre.html')


@bp.route('/servicos')
def servicos():
    return render_template('servicos.html')