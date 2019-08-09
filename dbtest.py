import pymysql

def configure(app):
    db = pymysql.connect(
        app.config.get('MYSQL_HOST'),
        app.config.get('MYSQL_USER'),
        app.config.get('MYSQL_PASSWORD'),
        app.config.get('MYSQL_DB'))
        
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM direita"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        print("Conectado ao banco de dados")
    except:
        print("Erro na conexão ao banco de dados")