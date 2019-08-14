import os
from flask import current_app, Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

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


@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    print(current_app.config)
    

    if request.method == 'POST':
        # verifica se existe o campo file na requisição
        if 'file' not in request.files:
            flash('Nenhum arquivo enviado.')
            return redirect(request.url)

        # pega o arquivo enviado
        file = request.files['file']
        
        # se for vazio
        if file.filename == '':
            flash('Por favor, selecione um arquivo.')
            return redirect(request.url)

        # verifica a extensão do arquivo
        if file and allowed_file(file.filename):
            # secure_filename: função nativa usada para validar o nome do arquivo
            filename = secure_filename(file.filename)
            # salva o arquivo no disco
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('institucional.upload', filename=filename))
        else:
            flash('Tipo de arquivo não permitido.')

    return render_template('upload.html')


# helper para testar se a extensão do arquivo é permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@bp.route('/url-params')
def url_without_params():
    valor_final = '-'
    return render_template('url-params.html', valor=valor_final)

@bp.route('/url-params/<int:valor1>/<int:valor2>/<int:valor3>')
def url_params(valor1, valor2, valor3):
    if ((valor1 > valor3) or (valor3 < valor2)):
        valor_final = int(valor3 / valor1)
    else:
        total = valor1 + valor2 + valor3
        separator = ''
        retorno = ''
        while (total > 0):
            if ((total % 3) == 0):
                retorno = retorno + separator + str(total)
                if (separator == ''):
                    separator = '-'
            total = total - 1
        valor_final = retorno
    return render_template('url-params.html', valor=valor_final)