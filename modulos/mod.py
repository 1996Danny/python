
import math 

# numero = 16
# raiz = math.sqrt(numero)
# potencia = math.pow(numero, 3)

# print(f"la raiz de {numero} es {raiz}")
# print(f"la potencia de {numero} es {potencia}")


# import random as rd

# # simular lanzamiento de moneda

# resultado = rd.randint(0, 1)

# if resultado == 1:
#     print("Cruz")
# else:
#     print("Cara")


# from datetime import * # Así no
# from datetime import datetime, date # Así sí

# # fecha_actual = date.today()
# # print(fecha_actual)

# def calcular_edad():
#     # ingreso por consola de fecha de naciemieto (01/05/1999)
#     fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/YYYY): ")
#     nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()

#     hoy = date.today()

#     edad = (hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)))

#     # print(hoy.year - nacimiento.year) # Devuelve la edad == 29
#     # print(((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))) # Devuelve 1 == True

#     return edad



# # Completar!!! Cuantos dias faltan para cumplir años
# print(calcular_edad())


# Módulo propio para importar a otro archivo
def saludar():
    print("Hola, mundo desde el modulo mod.py")

# saludar()

def potenciar(n):
    potencia = math.pow(n, 3)
    return potencia