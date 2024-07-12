import mysql.connector

try:
    # Conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_python"
    )
except:
    print("Error al conectarse a la base de datos")        
else:    
        #Verificar si la conexión fue exitosa
        if conexion.is_connected():
            print("Conexión exitosa")
        else:
            print("Error en la conexión")

        # Crear un cursor para ejecutar sentencias SQL
        cursor=conexion.cursor()

        # Crear base de datos si no existe
        cursor.execute(
            """
            CREATE DATABASE IF NOT EXISTS bd_python
            """
        )
        # Imprimir si la base de datos existia a la hora de crearla
        if cursor.rowcount == 0:
            print("La base de datos ya existía")
        else: 
            print("Base de datos creada exitosamente")
