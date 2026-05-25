from facultad import Facultad
from estudiante import Estudiante

facu = Facultad()

while True:
    print("\n1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        carrera = input("Carrera: ")
        facu.agregar_estudiante(Estudiante(nombre, dni, carrera))
        print("Estudiante agregado")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        try:
            est = facu.buscar_estudiante(nombre)
            print("Encontrado:", est)
        except Exception as e:
            print("Error:", e)

    elif opcion == "3":
        break
