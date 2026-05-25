from facultad import Facultad
from estudiante import Estudiante
from profesor import Profesor

facu = Facultad()

# Agregar datos
facu.agregar_estudiante(Estudiante("Juan", "123", "Ingeniería"))
facu.agregar_estudiante(Estudiante("Ana", "456", "Medicina"))

facu.agregar_profesor(Profesor("Dr. Pérez", "789", "Matemática"))

# Mostrar
facu.mostrar_estudiantes()
facu.mostrar_profesores()

# Buscar con manejo de error
try:
    est = facu.buscar_estudiante("Juan")
    print("Encontrado:", est)
except Exception as e:
    print("Error:", e)