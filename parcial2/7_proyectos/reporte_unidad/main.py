from empleados import Personas, Estudiantes, Maestro

# Creación de objetos Personas
persona1 = Personas("Juan", "González", "López", 20, "555-1234", "juan@example.com", "Calle Principal 123")
persona2 = Personas("María", "Martínez", "Sánchez", 22, "555-5678", "maria@example.com", "Av. Independencia 456")

# Creación de objetos Estudiantes
estudiante1 = Estudiantes("Carlos", "Pérez", "García", 18, "555-2468", "carlos@example.com", "Calle de la Paz 789",
                          "Escuela Secundaria", "E12345", "3ro", "A", 9.2)
estudiante2 = Estudiantes("Laura", "López", "Gómez", 21, "555-1357", "laura@example.com", "Av. Juárez 101",
                          "Preparatoria", "E67890", "6to", "B", 8.5)

# Creación de objetos Maestro
maestro1 = Maestro("Pedro", "Ramírez", "Pérez", 35, "555-3579", "pedro@example.com", "Calle Principal 456",
                   "Escuela Primaria", "Profesor", 40000, 12)
maestro2 = Maestro("Ana", "Gutiérrez", "Martínez", 40, "555-7890", "ana@example.com", "Av. Reforma 789", 
                   "Escuela Secundaria", "Directora", 60000, 18)

# Imprimir información de los objetos creados
print("Información de la persona 1:")
print(persona1.get_info())
print("\nInformación de la persona 2:")
print(persona2.get_info())

print("\nInformación del estudiante 1:")
print(estudiante1.get_info())
print("\nInformación del estudiante 2:")
print(estudiante2.get_info())

print("\nInformación del maestro 1:")
print(maestro1.get_info())
print("\nInformación del maestro 2:")
print(maestro2.get_info())
