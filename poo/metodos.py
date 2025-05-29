
# metodo independiente de la clase
# class Calculadora:

#     @staticmethod
#     def restar(a,b):
#         return a-b
#     # decorador
#     @staticmethod
#     def sumar(a, b):
#         return a + b

# print(Calculadora.restar(2, 5))


# datos predeterminados
# class Pastel:

#     def __init__(self, sabor):
#         self.sabor = sabor

#     @classmethod
#     def chocolate(cls):
#         return cls("chocolate")
    
# torta = Pastel("vainilla")
# print(torta.sabor)

# torta2 = Pastel("Frutilla")
# print(torta2.sabor)

# torta = Pastel.chocolate()
# print(torta.sabor)

# torta2 = Pastel.chocolate()
# print(torta2.sabor)