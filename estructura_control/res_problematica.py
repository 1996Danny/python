
opcion = [] #[Pizza, Emapanda, Hamburguesa]
votos = {} # {"Pizza": 3, "Empanadas": 2} key: Nombre de la opción , value: votos recibidos
votantes = set() # {Marcelo, Maria, Lucas}

print("Bienvenido al sistema de votación")

while True:
    comida = input("ingrese la comida deseada o 'salir' para terminar el ingreso de datos:")
    if comida.lower() == "salir":
        print("terminó la carga de datos")
        continue
    elif comida not in opcion:
        opcion.append(comida)
        print(opcion)

    votante = input("Ingrese su nombre: ")
    if votante in votantes:
        print("Usted ya dió su voto!!")
        continue
    else:
        votantes.add(votante)
        print(votantes)