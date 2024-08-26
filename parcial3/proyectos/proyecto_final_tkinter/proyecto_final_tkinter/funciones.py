import re
from conexion import *
def borraPantalla():
    import os
    os.system("cls") 

def esperarTecla():
    print("\n \t \t Oprima cualquier tecla para continuar ...")
    input()  

#Verificar curp tiene que ver si la curp ya existe en la base de datos
def verificar_curp(curp_persona):
    # Verificar el formato de la CURP
    patron = r'^[A-Z]{4}\d{6}[H,M][A-Z]{5}[A-Z0-9]{2}$'
    
    if not re.match(patron, curp_persona):
        return False, "El CURP tiene un formato inválido."

    cursor = conexion.cursor()
    # Consulta para buscar la CURP en la tabla Personas
    consulta = "SELECT CURP_persona FROM Personas WHERE CURP_persona = %s"
    cursor.execute(consulta, (curp_persona,))

    # Verificar si se encontró la CURP
    resultado = cursor.fetchone()

    if resultado:
        return False, "La CURP ya existe en la base de datos."
    else:
        return True, "La CURP no existe en la base de datos. Puede continuar."

def verificar_correo(email_persona):


    # Verificar el formato del correo
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if not re.match(patron, email_persona):
        return False, "El correo tiene un formato inválido."

    cursor = conexion.cursor()
    # Consulta para buscar el correo en la tabla Personas
    consulta = "SELECT email_persona FROM Personas WHERE email_persona = %s"
    cursor.execute(consulta, (email_persona,))

    # Verificar si se encontró el correo
    resultado = cursor.fetchone()

    if resultado:
        return False, "El correo ya existe en la base de datos."
    else:
        return True, "El correo no existe en la base de datos. Puede continuar."
    
def verificar_matricula_estudiante(matricula_estudiante):
    cursor = conexion.cursor()
    # Consulta para buscar la matricula en la tabla Alumnos
    consulta = "SELECT matricula_estudiante FROM Estudiantes WHERE matricula_estudiante = %s"
    cursor.execute(consulta, (matricula_estudiante,))

    # Verificar si se encontró la matricula
    resultado = cursor.fetchone()

    if resultado:
        return False, "La matricula ya existe en la base de datos."
    else:
        return True, "La matricula no existe en la base de datos. Puede continuar."
    
def verificar_matricula_profesor(matricula_profesor):
    cursor = conexion.cursor()
    # Consulta para buscar la matricula en la tabla Profesores
    consulta = "SELECT matricula_profesor FROM Profesores WHERE matricula_profesor = %s"
    cursor.execute(consulta, (matricula_profesor,))

    # Verificar si se encontró la matricula
    resultado = cursor.fetchone()

    if resultado:
        return False, "La matricula ya existe en la base de datos."
    else:
        return True, "La matricula no existe en la base de datos. Puede continuar."