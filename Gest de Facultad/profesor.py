from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, dni, materia):
        super().__init__(nombre, dni)
        self.materia = materia

    def __str__(self):
        return f"Profesor: {self.nombre} - {self.materia}"