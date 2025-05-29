

# animale voladores y no voladores (Principio de Liskov)
class Ave:
    def volar(self):
        print("Volandooo.")

class Pato(Ave):
    def volar(self):
        print("Pato esta volandoo")

class Pinguino(Ave):
    def volar(self):
        print("No puede volar")

# -----------------------------------------------------------------

from abc import ABC, abstractmethod
class AveVoladoras(ABC):
    @abstractmethod
    def volar(self):
        pass

class AveNoVoladoras(ABC):
    @abstractmethod
    def nadar(self):
        pass


class Pinguino(AveNoVoladoras):
    def nadar(self):
        print("El pinguino esta nadando")

class Paloma(AveVoladoras):
    def volar(self):
        print("La paloma esta volando")


pinguino1 = Pinguino()
paloma1 = Paloma()
pinguino1.nadar()
paloma1.volar()

