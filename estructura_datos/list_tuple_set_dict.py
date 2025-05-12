
# # lista vacia
# # lista_vacia = []
# # print(lista_vacia)
# # print(type(lista_vacia))

# # lista_vacia = list()
# # print(lista_vacia)
# # print(type(lista_vacia))

# lista = [1, "Hola mundo", 1.5, "1", ["otra", "lista"], True, {}, 1]
# # print(lista)

# # print(lista[2])
# # agrega un elemento al final
# lista.append("nuevo")
# # print(lista)

# # agregar un numero en el indice número 3
# lista.insert(3, "Adios")
# # print(lista)

# # eleminar el ultimo elemento por defecto sino ingresar el índice
# lista.pop(3)
# # print(lista)

# # modificar un elemento
# lista[1] = "Hola Informatorio"
# # print(lista)

# # listas a trozos
# # print(lista[2:5])
# # print(lista[-1])

# #recorrer una lista
# # for i in lista:
# #     print(i)

# # imprimir un elemento dentro de otra lista
# # print(lista[4][1])

# # muestra la cantidad de elementos dentro de la lista
# print(len(lista))

# lista1 + lista2

# -------------------------- TUPLAS------------------------------------------

# tupla vacia
# tupla = ()
# print(tupla)
# print(type(tupla))
# tupla = tuple()
# print(tupla)
# print(type(tupla))

# tupla = (1, 5 , 2)
# print(tupla)

# indices en tuplas es igual que las listas
# print(tupla[2])

# contar los elemtos de la tupla "lenght"
# print(len(tupla))

# para ordenar tiene que ser los mismos elementos
# devuelve una lista ordenada
# print(sorted(tupla))

# tupla1 = (1,3)
# tupla2 = (4,5)

# tupla3 = tupla1 + tupla2
# print(tupla3)
# no se puede modificar
# tupla1[0] = 10

# ----------------------- Conjuntos----------------------------------

# conjunto vacio
# conjunto = set()
# print(type(conjunto))

# conjunto = {1,1,1,1,1,1,1,1,1,2,3,5,7,8}
# print(conjunto)

# union = todos los elementos del conjunto

# conjA = {1,2,3}
# conjB = {1,4,5,8,9}
# print(conjA.union(conjB))

# intersección = los elementos repetidos en conjA y conjB
# print(conjA.intersection(conjB))

# diferencia y diferencia simétrica
# print(conjA.difference(conjB))
# print(conjA.symmetric_difference(conjB))

# print(len(conjA))
# print(len(conjB))

# agregar un elemento al final del conjunto
# conjA.add(5)
# print(conjA)

# -------------------------------------Diccionarios--------------------------

# diccionario vacio
# diccionario = {}
# print(type(diccionario))
# diccionario = dict()
# print(type(diccionario))

# diccionario_autos = {
#     "marca": "toyota",
#     "modelo": "corolla",
#     "año": 2020
# }

# print(diccionario_autos)

# print(diccionario_autos.keys())
# print(diccionario_autos.values())
# print(diccionario_autos.items())

# diccionario_autos.pop("marca")
# print(diccionario_autos)

# diccionario_autos.update({"km": 100000})
# print(diccionario_autos)


# for clave, valor in diccionario_autos.items():
#     print(clave, valor)

# print(len(diccionario_autos))

# modificar un valor
# diccionario_autos["año"] = 2024
# print(diccionario_autos)