
# clase abstracta no deja instancias

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def __init__(self, ruedas, freno, color):
        self.ruedas = ruedas
        self.freno = freno
        self.color = color
   
    @abstractmethod
    def mover(self):
        return "El vehiculo esta en movimiento"
    
    # __repr__
    # def __str__(self):
    #     return "Clase vehiculo"


class Auto(Vehiculo):
    def __init__(self, ruedas, freno, color):
        super().__init__(ruedas, freno, color)
    
    def mover(self):
        return super().mover()


class Camion(Vehiculo):
    pass

# v = Vehiculo(4, "de mano", "Azul")
a = Auto(4, "de mano", "Azul")
print(a.color)
print(a.freno)
print(a.ruedas)

# print(a)