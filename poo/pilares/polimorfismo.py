

class Animal: 
    def sonido():
        pass

class Vaca(Animal):
    def sonido(self):
        return "MUU"
    
class Oveja(Animal):
    def sonido(self):
        return "Mee"
    
v = Vaca()
o = Oveja()

print(v.sonido())
print(o.sonido())