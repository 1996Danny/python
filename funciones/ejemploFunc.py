
# # sin parametros y no retorna valores
# def saludar():
#     print("Hola, mundo!")


# # llamar o invocar
# saludar()

# # con retorno sin parametros
# def saludar():
#     return "Hola, mundo"

# saludo = saludar()
# print(saludo)

# def multiplicar(numero):
#     m = numero * 2
#     return m

# resultado = multiplicar(4)
# print(resultado)

# print(multiplicar(5))


# ARGS (1,22,3,44,5)

# def sumar(*args):
#     # varible local
#     total = 0
#     for numero in args:
#         total += numero

#     return total

# resultado1 = sumar(1,44,55,99,234)
# print(f"el resultado de la suma es: {resultado1}")
# resultado2 = sumar(1,2,3,4,5,6,78,8,9,0,0,7,56,34,23)
# resultado2 = sumar(1,2,3,4,5,6,78,8,9,0,0,7,56,34,23)
# print(f"el resultado de la suma es: {resultado2}")
# resultado2 = sumar(1,2,3,4,5,6,78,8,9,0,0,7,56,34,23)
# print(f"el resultado de la suma es: {resultado2}")
# resultado2 = sumar(1,2,3,4,5,6,78,8,9,0,0,7,56,34,23)
# print(f"el resultado de la suma es: {resultado2}")
# resultado2 = sumar(1,2,3,4,5,6,78,8,9,0,0,7,56,34,23)
# resultado2 = sumar(1,2,3,4,5,6,78,8,9,0,0,7,56,34,23)
# resultado2 = sumar(1,2,3,4,5,6,78,8,9,0,0,56,34,23)
# print(f"el resultado de la suma es: {resultado2}")
# resultado2 = sumar(1,2,3,4,5,6,78,8,9,0,0,7,56,34,23)
# resultado2 = sumar(1,2,3,4,5,6,78,8,0,0,7,56,34,23)
# resultado2 = sumar(1,2,3,4,5,6,78,0,0,7,56,34,23)
# print(f"el resultado de la suma es: {resultado2}")
# resultado2 = sumar(1,2,3,4,5,6,78,8,9,0,0,7,56,34,23)
# resultado2 = sumar(1,2,3,4,5,6,78,8,9,0,0,7,56,34,23)
# resultado2 = sumar(1,2,3,4,5,7,56,34,23)
# print(f"el resultado de la suma es: {resultado2}")


#  KWAGS
# {clave:valor}
# def db(**kwargs):
#     config = {
#         "host": kwargs.get("host"),
#         "puerto": kwargs.get("puerto")
#     }
#     print(f"Estas conectado a la BD: {config['host']}:{config["puerto"]}")

# db(host="192.658.2.3", puerto=8000)


# def alumno(**kwags):
#     for clave, valor in kwags.items():
#         print(f"{clave} = {valor}")

# alumno(nombre="Juanito", apellido="Casa", nota=7)

# Pruebas
# def sumar(a, b):
#     return a + b

# assert sumar(2, 2) == 5
# print()
# print(sumar(2, 2))