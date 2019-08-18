import pymysql

def configure(app):
    try:
        db = pymysql.connect(
            app.config.get('MYSQL_HOST'),
            app.config.get('MYSQL_USER'),
            app.config.get('MYSQL_PASSWORD'),
            app.config.get('MYSQL_DB'))

        cursor = db.cursor()
        sql = "SELECT * FROM usuarios"
        cursor.execute(sql)
        results = cursor.fetchall()
        #cursor.commit()
        cursor.close()
        db.close()
        print(results)
        print("Conectado ao banco de dados")
    except:
        print("Erro na conexão ao banco de dados")