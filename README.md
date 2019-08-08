#### Os comandos listados abaixo podem ser executados no cmd do visual studio ou no prompt do windows
###### *A única exceção fica por conta do comando git clone, que deverá ser executado no prompt do git

# Criar ambiente virtual com Python 3

`python -m venv nome-de-sua-escolha-aqui`

# Ativar seu ambiente virtual

`caminho-para-seu-ambiente-virtual-aqui/Scripts/activate`

Caso não funcione com a barra (/), tente com contra barra (\\)

# Instalar o Flask no ambiente virtual

`pip install flask`

# Clonar este repositório

`git clone https://github.com/welisonmenezes/flask-tests.git`

Este comando deve ser executado no prompt do Git

# Acessar raíz deste projeto exemplo

`cd flask-testes`

# Para rodar o flask em modo de desenvolvimento

`set FLASK_ENV='development'`

`set FLASK_DEBUG=1`

`python -m flask run`

Rodar dessa forma facilita no desenvolvimento, pois cada alteração no código ficará prontamente disponível para visualização no navegador, sem a necessidade de matar o serviço e levantar novamente.
