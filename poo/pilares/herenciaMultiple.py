
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido():
        return "sonido general"
    

class Perro:
    def __init__(self, color):
        self.color = color

    def sonido():
        return f"Guau"
    

class Dogo(Animal, Perro):
   def __init__(self, nombre, color):
       super().__init__(nombre)
       Perro.__init__(self, color)


dog1 = Dogo("Jack", "Blanco")

print(dog1.nombre)
print(dog1.color)
