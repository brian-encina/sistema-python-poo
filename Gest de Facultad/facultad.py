class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.profesores = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

    def mostrar_estudiantes(self):
        for e in self.estudiantes:
            print(e)

    def mostrar_profesores(self):
        for p in self.profesores:
            print(p)

    def buscar_estudiante(self, nombre):
        for e in self.estudiantes:
            if e.nombre.lower() == nombre.lower():
                return e
        raise Exception("Estudiante no encontrado")