from conexion import *
if conexion and conexion.is_connected():
    print("Conexión exitosa")

    # Crear un cursor para ejecutar sentencias SQL
    cursor = conexion.cursor()
    # Actualizar registros de la tabla
    cursor.execute(
        """
        UPDATE clientes SET nombre = 'Juan' WHERE id = 2
        """
    )
    print("Registro actualizado")
    #Sirve para guardar los cambios en la base de datos
    conexion.commit()
    #Imprime el número de registros actualizados
    print(cursor.rowcount, "registro(s) actualizado(s)")
    conexion.close()
else:
    print("Error en la conexión")    
