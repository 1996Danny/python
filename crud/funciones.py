
from bd_config import *


def create_persona():
    connection = conexion()
    cursor = connection.cursor()

    cursor.execute(
        "insert into personas(nombre, apellido, direccion, edad) values (%s,%s,%s,%s)", 
        ("Marta", "Juarez", "calle reconquista", 30)
        )
    print("Consulta ejecutada!")

    connection.commit()

    connection.close()

def read_persona():
    connection = conexion()
    cursor = connection.cursor()
    cursor.execute("select * from personas")

    print("Consulta ejecutada!")

    # registros = cursor.fetchone()
    # print(registros)
    # registros = cursor.fetchone()
    # print(registros)
    # registros = cursor.fetchone()
    # print(registros)
    registros = cursor.fetchall()

    for persona in registros:
        print(persona)

    connection.close()
    

def update_persona():
    pass

def delete_persona():
    pass


# create_persona()
read_persona()