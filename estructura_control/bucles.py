
# # bucles for (definidos)

# # descendente
# for i in range(100, 10, -10):
#     print(i)

# # ascendente
# for i in range(10, 101, 10):
#     print(i)


# # bucles while (indefinidos)
# # infinito
# # while True:
# #     print("Hola mundo!")

# contador = 1

# while contador <= 10000:
#     # print(f"El valor es: {contador}")
#     print("El valor es: ", contador)
#     # contador += 1
#     contador = contador + 1



# EJERCICIO MATIAS
# votantes = []

# def agregar_amigos():
    
#     while True:
#         amigo = input('Escribi un nombre: ')
#         print ('Escribi "Salir" para volver atras')
#         if amigo.lower() == 'salir':
#             print('Termino la carga de datos')
#             break
#         elif amigo.lower() not in votantes:
#             votantes.append(amigo)
#             print(votantes)
#         else:
#             print('Ya estas en la lista wachin')

# agregar_amigos()