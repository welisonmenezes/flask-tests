# Criar ambiente virtual com Python 3

`python -m venv nome-de-sua-escolha-aqui`

# Ativar seu ambiente virtual

`caminho-para-seu-ambiente-virtual-aqui/Scripts/activate`

Caso não funcione com a barra (/), tente com contra barra (\\)

# Instalando o Flask no ambiente virtual

`pip install flask`

# Para rodar o flask em modo de desenvolvimento

`set FLASK_ENV='development'`

`set FLASK_DEBUG=1`

`python -m flask run`

Rodar dessa forma facilita no desenvolvimento, pois cada alteração no código ficará prontamente disponível para visualização no navegador, sem a necessidade de matar o serviço e levantar novamente.
