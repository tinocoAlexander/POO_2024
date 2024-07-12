from empleados import Personas, Estudiantes, Profesores, Clases, Calificaciones

# Creación de dos objetos de la clase Personas
persona1 = Personas("Luis", "Ramírez", "Torres", 30, "555-9876", "luis.ramirez@example.com", "Calle Principal 101", "Universidad Nacional", False, "password123")
persona2 = Personas("Elena", "Mendoza", "Rojas", 25, "555-1234", "elena.mendoza@example.com", "Calle Secundaria 202", "Universidad Nacional", False, "mypassword")

# Creación de dos objetos de la clase Estudiantes
estudiante1 = Estudiantes("Juan", "Pérez", "Gómez", 20, "555-1234", "juan.perez@example.com", "Calle Falsa 123", "Universidad Nacional", "20211234", 2, "A", 9.2, "Clásica", "Ingeniería")
estudiante2 = Estudiantes("María", "López", "Fernández", 21, "555-5678", "maria.lopez@example.com", "Calle Verdadera 456", "Universidad Nacional", "20215678", 3, "B", 8.5, "Bilingue", "Medicina")

# Creación de dos objetos de la clase Profesores
profesor1 = Profesores("Carlos", "Martínez", "Rodríguez", 45, "555-8765", "carlos.martinez@example.com", "Avenida Siempreviva 789", "Universidad Nacional", "Profesor Titular", 50000, 10, "Doctorado", ["Matemáticas", "Física"])
profesor2 = Profesores("Ana", "González", "Hernández", 38, "555-4321", "ana.gonzalez@example.com", "Bulevar de los Sueños 321", "Universidad Nacional", "Profesor Asociado", 40000, 5, "Maestría", ["Química", "Biología"])

# Creación de dos objetos de la clase Clases
clase1 = Clases("Carlos", "Martínez", "Rodríguez", 45, "555-8765", "carlos.martinez@example.com", "Avenida Siempreviva 789", "Universidad Nacional", "Profesor Titular", 50000, 10, "Doctorado", ["Matemáticas", "Física"], "Física", "Lunes 8:00-10:00")
clase2 = Clases("Ana", "González", "Hernández", 38, "555-4321", "ana.gonzalez@example.com", "Bulevar de los Sueños 321", "Universidad Nacional", "Profesor Asociado", 40000, 5, "Maestría", ["Química", "Biología"], "Química", "Martes 10:00-12:00")

# Creación de dos objetos de la clase Calificaciones
calificacion1 = Calificaciones(estudiante1, clase1, {"Parcial 1": 9.5, "Parcial 2": 8.5, "Parcial 3": 9.0})
calificacion2 = Calificaciones(estudiante2, clase2, {"Parcial 1": 8.0, "Parcial 2": 9.0, "Parcial 3": 10.0})

# Mostrar información de los objetos creados
print("Objetos de persona:\n")
print("Persona 1:\n")
print(persona1.get_info())
print("\nPersona 2:\n")
print(persona2.get_info())

print("\nObjetos de estudiante:\n")
print("Estudiante 1:\n")
print(estudiante1.get_info())
print("\nEstudiante 2:\n")
print(estudiante2.get_info())

print("\nObjetos de profesor:\n")
print("Profesor 1:\n")
print(profesor1.get_info())
print("\nProfesor 2:\n")
print(profesor2.get_info())

print("\nObjetos de clase:\n")
print("Clase 1:\n")
print(clase1.get_info())
print("\nClase 2:\n")
print(clase2.get_info())

print("\nObjetos de calificación:\n")
print("Calificación 1:\n")
print(calificacion1.get_info())
print("\nCalificación 2:\n")
print(calificacion2.get_info())
