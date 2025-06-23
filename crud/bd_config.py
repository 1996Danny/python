
import mysql.connector

def conexion():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "1234",
        database = "personas_db"
    )