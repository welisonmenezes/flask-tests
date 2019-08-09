from flask import current_app, Blueprint, render_template, request

bp = Blueprint('institucional', __name__, url_prefix='/', template_folder='templates/')

@bp.route('/')
def index():
    paises = ['Brasil', 'Argentina', 'Estados Unidos', 'França']
    return render_template('home.html', paises=paises)


@bp.route('/contato', methods=['GET', 'POST'])
def contato():
    feedback = ''
    print(request.method)
    if request.method == 'POST':
        #print(request.get_data())
        print(request.form.get('email', ''))
        print(request.form.get('assunto', ''))
        print(request.form.get('mensagem', ''))
        feedback = 'Mensagem enviada com sucesso'

    return render_template('contato.html', feedback=feedback)


@bp.route('/sobre')
def sobre():
    return render_template('sobre.html')


@bp.route('/servicos')
def servicos():
    return render_template('servicos.html')