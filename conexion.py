import pymysql

def conectar_db():
    try:
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="gestor_productos"
            
        )
        return db
    except pymysql.Error as err:
        print(f"Error: {err}")