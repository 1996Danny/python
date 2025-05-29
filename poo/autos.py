
class Auto:
    # constructor
    def __init__(self, marca, modelo):
        # atributos
        self.marca = marca
        self.modelo = modelo

    # método
    def tocar_bocina(self):
        print(f"{self.modelo}: PI PI")


coche1 = Auto("Toyota", "Etios")

coche1.tocar_bocina()