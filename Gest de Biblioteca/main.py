from biblioteca import Biblioteca
from libro import Libro

biblio = Biblioteca()

while True:
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro")
    print("6. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")

        biblio.agregar_libro(Libro(titulo, autor, isbn))
        print("Libro agregado correctamente")

    elif opcion == "2":
        print("\nLista de libros:")
        biblio.mostrar_libros()

    elif opcion == "3":
        titulo = input("Título del libro a prestar: ")
        biblio.prestar_libro(titulo)

    elif opcion == "4":
        titulo = input("Título del libro a devolver: ")
        biblio.devolver_libro(titulo)

    elif opcion == "5":
        titulo = input("Título a buscar: ")
        try:
            libro = biblio.buscar_libro(titulo)
            print("Encontrado:", libro)
        except Exception as e:
            print("Error:", e)

    elif opcion == "6":
        print("Saliendo del sistema... ")
        break

    else:
        print("Opción inválida, intentá de nuevo")
