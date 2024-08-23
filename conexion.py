import mysql.connector

def conectar_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestor_productos"
            
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error: {err}")