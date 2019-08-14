#### Os comandos listados abaixo podem ser executados no cmd do visual studio ou no prompt do windows
###### *A única exceção fica por conta do comando git clone, que deverá ser executado no prompt do git

# Criar ambiente virtual com Python 3

`python -m venv nome-de-sua-escolha-aqui`

# Ativar seu ambiente virtual

`caminho-para-seu-ambiente-virtual-aqui/Scripts/activate`

Caso não funcione com a barra (/), tente com contra barra (\\)

# Instalar dependências à partir de requirements.txt

`pip install -r requirements.txt`

Executando o código acima, todas as dependênicas desse projetos serão automaticamente instalados, dessa forma os comandos pip install subsequêntes não serão mais necessários.

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

`python -m flask run --reload`

Rodar dessa forma facilita no desenvolvimento, pois cada alteração no código ficará prontamente disponível para visualização no navegador, sem a necessidade de matar o serviço e levantar novamente.

# Para se conectar à um banco de dados MySQL

`pip install PyMySQL`

No arquivo config.py atualize os campos abaixo com os dados da sua conexão

```
MYSQL_HOST = 'seu-host-aqui'
MYSQL_USER = 'seu-user-aqui'
MYSQL_PASSWORD = 'sua-senha-aqui'
MYSQL_DB = 'seu-banco-de-dados-aqui'
```