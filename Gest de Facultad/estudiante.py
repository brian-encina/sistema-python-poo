from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, dni, carrera):
        super().__init__(nombre, dni)
        self.carrera = carrera

    def __str__(self):
        return f"Estudiante: {self.nombre} - {self.carrera}"