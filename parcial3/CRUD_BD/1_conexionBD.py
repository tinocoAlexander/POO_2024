import mysql.connector
from mysql.connector import Error, InterfaceError

# Conexión a la base de datos
try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_python"
    )
except Exception as e:
    print(f"Tipo de excepción {type(e).__name__}")

    #print("Error al conectarse a la base de datos")    
except InterfaceError:
    print("Error al conectarse a la base de datos")
else:
    #Verificar si la conexión fue exitosa
    if conexion.is_connected():
        print("Conexión exitosa")
    else:
        print("Error en la conexión")

    # Crear un cursor para ejecutar sentencias SQL
    conexion=conexion.cursor()


