
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



"""
    {
        "clave" : "valor"
        "nombre" : "Pepito"
    }
"""