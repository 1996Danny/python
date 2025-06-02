

# publico
# _protegido (no modifica sino es una convención en el equipo de desarrollo)
# __privado (solamente se pude accede y modificar desde la misma clase)


class Cuenta:
    def __init__(self, propietario, saldo):
        self.propietario = propietario
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo


c1 = Cuenta("dani", 100)
print(c1.get_saldo())

print(c1.propietario)
print(c1.get_saldo())

c1._saldo = 0
print(c1._saldo)

c1.set_saldo(1000)
print(c1.get_saldo())



# -------------------------------------------
class Cuenta:
    def __init__(self, propietario, saldo):
        self.__propietario = propietario
        self.__saldo = saldo
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

    # get
    @property # funciones que envuelven otra función y modifica la E/S
    def propietario(self):
        return self.__propietario
    
    # set
    @propietario.setter
    def propietario(self, nuevo_propietario):
        self.__propietario = nuevo_propietario

    @propietario.deleter
    def propietario(self):
        print("Eliminando propietario .... ")
        del self.__propietario
    


c1 = Cuenta("dani", 100)
print(c1.propietario)

c1.propietario = "Luis"
print(c1.propietario)

del c1.propietario
print(c1.propietario)