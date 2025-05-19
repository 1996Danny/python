
opcion = [] #[Pizza, Emapanda, Hamburguesa]
votos = {} # {"Pizza": 3, "Empanadas": 2} key: Nombre de la opción , value: votos recibidos
votantes = set() # {Marcelo, Maria, Lucas}

print("Bienvenido al sistema de votación")

while True:

    while True:
        comida = input("ingrese la comida deseada o 'salir' para terminar el ingreso de datos:")
        if comida.lower() == "salir":
            print("terminó la carga de datos")
            break
        elif comida not in opcion:
            opcion.append(comida.title())
            # print(opcion)

    for op in opcion:
        votos[op] = 0

    while True:
        votante = input("Ingrese su nombre o 'salir' para terminar el ingreso de datos: ")
        if votante in votantes:
            print("Usted ya dió su voto!!")
            continue
        elif votante == "salir":
            print("Votación finalizada")
            break
        else:
            votantes.add(votante)
            print(f"Opciones: {opcion}")
            voto = input("ingrese su voto: ").title()
            # print(votantes)

            votos[voto] += 1
    break

print("=============Resultados=============")
for opcion in votos:
    print(opcion + ":", votos[opcion], "voto(s)")

mayor = 0
ganadores = []
for opcion in votos:
    if votos[opcion] > mayor:
        mayor = votos[opcion]
        ganadores = [opcion]
    elif votos[opcion] == mayor:
        ganadores.append(opcion)

if len(ganadores) == 1:
    print("\n🏆 Ganador:", ganadores[0])
else:
    print("\n🤝 Empate entre:", ", ".join(ganadores))
