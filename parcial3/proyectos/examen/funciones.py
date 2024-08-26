import re
from conexion import *
def borraPantalla():
    import os
    os.system("cls") 

def esperarTecla():
    print("\n \t \t Oprima cualquier tecla para continuar ...")
    input()  

# Funcion para validar que la matricula existe en la tabla vehiculo y no dejar pasar si no esta
def validarMatricula(matricula):
    try:
        cursor.execute(
            "select * from autos where matricula=%s",
            (matricula,)
        )
        if cursor.fetchone() is not None:
            return True
        else:
            return False
    except:
        return False
    
# Funcion para validar que el no_revision existe en la tabla revisiones y no dejar pasar si no esta
def validarNoRevision(no_revision):
    try:
        cursor.execute(
            "select * from revisiones where no_revision=%s",
            (no_revision,)
        )
        if cursor.fetchone() is not None:
            return True
        else:
            return False
    except:
        return False
    
def validarNIF(nif):
    try:
        cursor.execute(
            "select * from clientes where nif=%s",
            (nif,)
        )
        if cursor.fetchone() is not None:
            return True
        else:
            return False
    except:
        return False
    
def validarEmail(email):
    try:
        cursor.execute(
            "select * from usuarios where email=%s",
            (email,)
        )
        if cursor.fetchone() is not None:
            return True
        else:
            return False
    except:
        return False
