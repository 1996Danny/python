
class Persona:
    # constructor
    def __init__(self, nombre, edad):
        # atributos
        self.nombre = nombre
        self.edad = edad

    # método
    def saludar(self):
        print(f"{self.nombre} dice Buenos días")


# intanciar objeto persona1
persona1 = Persona("Ana", 18)
print(f"Hola, {persona1.nombre}")
print(f"tu edad es: {persona1.edad} años")
persona1.saludar()

# instanciar persona2
persona2 = Persona("Juan", 30)
print(f"Hola, {persona2.nombre}")
print(f"tu edad es: {persona2.edad} años")
persona2.saludar()

# instanciar persona3
persona3 = Persona("Romina", 25)
print(f"Hola, {persona3.nombre}")
print(f"tu edad es: {persona3.edad} años")
persona3.saludar()