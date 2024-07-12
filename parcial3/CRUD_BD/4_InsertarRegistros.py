from conexion import *
# Crear un cursor para ejecutar sentencias SQL
if conexion and conexion.is_connected():
    print("Conexión exitosa")

    # Crear un cursor para ejecutar sentencias SQL
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    # Insertar registros en la tabla
    #cursor.execute(
        #"""
        #INSERT INTO clientes (id, nombre, direccion, telefono)
        #VALUES (NULL, 'Alexander Tinoco Sanchez', 'Calle Verdadera', '6182318481')
        #"""
    #)
    cursor.execute(
        """
        INSERT INTO clientes (id, nombre, direccion, telefono)
        VALUES (NULL, %s, %s, %s)
        """, (nombre, direccion, telefono)
    )
    #Sirve para guardar los cambios en la base de datos
    conexion.commit()
    #Imprime el número de registros insertados
    print(cursor.rowcount, "registro(s) insertado(s)")
    #Cerrar el cursor
    cursor.close()
else:
    print("Error en la conexión")