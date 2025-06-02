

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def prensentar(self):
        return f"Mi nombre es {self.nombre}, mi apellido es {self.apellido} y tengo {self.edad}"

    def saludar(self):
        return "Hola"
    

# pers_1 = Persona("Dani", "Frias", 28)
# print(pers_1.prensentar())

class PersonaEstudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera, universidad):
        super().__init__(nombre, apellido, edad)
        self.carrera = carrera
        self.universidad = universidad

    def estudio(self):
        return f"Estudio en {self.universidad} la carrera {self.carrera}"
    

# pers_est = PersonaEstudiante("Dani", "Frias", 28, "Tecnicatura Nuclear", "Embalse")

# print(pers_est.prensentar())
# print(pers_est.estudio())


class PersonaIngeniero(Persona):
    def __init__(self, nombre, apellido, edad, anios_trabajo, tipo_ing):
        super().__init__(nombre, apellido, edad)
        self.anios_trabajo = anios_trabajo
        self.tipo_ing = tipo_ing

    def prensentar(self):
        return super().prensentar() + f". Estudié Ing. {self.tipo_ing} y antigüedad de {self.anios_trabajo} años"


per_ing = PersonaIngeniero("Jose", "Marin", 50, 20, "Electronica")
print(per_ing.prensentar())