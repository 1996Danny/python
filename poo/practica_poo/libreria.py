
# Clase Abstacta Libro o Super clase libro
class Libro:
    def __init__(self, titulo, autor, isbn, paginas, genero="sin genero"):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.genero = genero
        # self.prestado == Falso (libro disponible) == True (libro no disponible)
        self.prestado = False

    # metodo abstracto
    def descripcion(self):
        pass

    def prestar(self):
        if self.prestado == False:
            self.prestado = True
            print("Libro Prestado")
        else:
            print("Libro no disponible para prestamos")
        

    def devolver(self):
        if self.prestado == True:
            self.prestado = False
            print("Libro Devuelto")
        else:
            print("Libro no prestado")

# subclase libro electronico
class LibroElectronico(Libro):
    # formato: pdf, docx, txt
    def __init__(self, titulo, autor, isbn, paginas, formato="pdf", genero="sin genero" ):
        super().__init__(titulo, autor, isbn, paginas, genero)
        self.formato = formato
    
    def descripcion(self):
        return f"Libro electronico {self.titulo}, {self.autor} en formato {self.formato}"

# subclase libro fisico
class LibroFisico(Libro):

    def descripcion(self):
        return f"Libro Fisico {self.titulo}, {self.autor} ISBN N. {self.isbn}"
    

class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento

    def publicar_libro(self, titulo, isbn, paginas, tipo):
        if tipo == "fisico":
            print(f"Libro publicado de {self.nombre}")
            return LibroFisico(titulo, self.nombre, isbn, paginas)
        elif tipo == "electronico":
            return LibroElectronico(titulo, self.nombre, isbn, paginas)


class Lector:
    def __init__(self, nombre, edad, direccion, n_socio):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.n_socio = n_socio

    def solicitar_prestamo(self, libro):
        return libro.prestar()

    def devolver_libro(self, libro):
        return libro.devolver()

    def datos_lector(self):
        print(f"Lector N: {self.n_socio} nombre: {self.nombre} direccion: {self.direccion}")


class Libreria:
    def __init__(self):     
        self.autores = []
        self.libros = []
        self.lectores = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro.descripcion()
        return f"Libro no encontrado"

    def registrar_lector(self, lector):
        self.lectores.append(lector)



autor1 = Autor("Dan Brown", "Norteamericano", "10/5/1960")

libro1 = autor1.publicar_libro("Inferno", "1234535sazf", 400, "fisico")

lector1 = Lector("dani", 28, "Av. Siempre Viva 123", 123)

# lector1.datos_lector()
libreria = Libreria()

libreria.agregar_libro(libro1)
libreria.registrar_lector(lector1)

# solicitud de prestamo
lector1.solicitar_prestamo(libro1)
lector1.solicitar_prestamo(libro1)
lector1.devolver_libro(libro1)
lector1.solicitar_prestamo(libro1)