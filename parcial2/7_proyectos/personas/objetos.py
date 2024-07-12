#Mandar a llamar las clases de clases.py
from clases import Personas, Estudiantes, Docentes
#Crear un objeto de la clase Personas
persona = Personas("Juan", 25, 1234567890)
#Crear un objeto de la clase Estudiantes
estudiante = Estudiantes("Ana Torres Guzmán", 20, 618129, "MECA", 235678)
#Crear un objeto de la clase Docentes
docente = Docentes("Daniel Fuentes Loera", 40, 6183335678,"TI", 123)

#Imprimir la información de los objetos
print("Información de la persona: ")
print(persona.info_persona())
print("Información del estudiante: ")
print(estudiante.info_persona())
print("Información del docente: ")
print(docente.info_persona())

#Imprimir la carrera del estudiante
print("Carrera del estudiante: ")
print(estudiante.informar_carrera())
#Imprimir la modalidad del docente
print("Modalidad del docente: ")
print(docente.informar_modalidad())


