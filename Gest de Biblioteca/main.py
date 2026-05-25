from biblioteca import Biblioteca
from libro import Libro

biblio = Biblioteca()

biblio.agregar_libro(Libro("1984", "George Orwell", "123"))
biblio.agregar_libro(Libro("El Principito", "Antoine de Saint-Exupéry", "456"))

biblio.mostrar_libros()
biblio.prestar_libro("1984")
biblio.mostrar_libros()
biblio.devolver_libro("1984")
biblio.mostrar_libros()