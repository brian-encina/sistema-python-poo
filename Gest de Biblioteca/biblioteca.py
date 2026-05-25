from libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        raise Exception("Libro no encontrado")

    def prestar_libro(self, titulo):
        try:
            libro = self.buscar_libro(titulo)
            libro.prestar()
            print("Libro prestado correctamente")
        except Exception as e:
            print("Error:", e)

    def devolver_libro(self, titulo):
        try:
            libro = self.buscar_libro(titulo)
            libro.devolver()
            print("Libro devuelto correctamente")
        except Exception as e:
            print("Error:", e)

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)