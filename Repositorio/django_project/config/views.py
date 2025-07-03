
from django.http import HttpResponse, JsonResponse

def saludar(request):
    return HttpResponse("<h1>Hola mundo desde mi primera vista de django!</h1>")


def bienvenida(request):
    return HttpResponse("Bienvenido a mi página web")



def sumar(request):
    a = int(request.GET.get("a"))
    b = int(request.GET.get("b"))

    resultado = a + b

    return JsonResponse({
            "resultado": resultado
    })

# solicitar nombre y apellido


# solicitar año de nacimiento y calcular edad

from datetime import datetime

def calcular_edad(request):
    anio_nacimiento = int(request.GET.get("anio_nacimiento"))
    edad = int(datetime.now().year) - anio_nacimiento

    return JsonResponse({"edad":edad})



import json
# metodo post (simular el envio de datos desde el front)

def insertar_producto(request):
    if request.method == "POST":
        data = json.loads(request.body)
        nombre = data.get("nombre")
        precio = data.get("precio")

        respuesta = {
            "nombre": nombre,
            "precio": precio
        }

        return JsonResponse(respuesta)
    return JsonResponse({"error": "Metodo incorrecto"})


#  ver conexion django mysql
from django.db import connection

def listar_personas(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM personas")
        personas = cursor.fetchall()

    return JsonResponse({"personas": personas})






"""
    ejemplo de JSON

    {
        "clave" : "valor"
        "nombre" : "Pepito"
    }
"""