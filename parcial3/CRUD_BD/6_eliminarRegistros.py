from conexion import *
if conexion and conexion.is_connected():
    print("Conexión exitosa")

    # Crear un cursor para ejecutar sentencias SQL
    cursor = conexion.cursor()

    # Eliminar registros de la tabla
    cursor.execute(
        """
        DELETE FROM clientes WHERE id = 1
        """
    )
    print("Registro eliminado")
    #Sirve para guardar los cambios en la base de datos
    conexion.commit()
    #Imprime el número de registros eliminados
    print(cursor.rowcount, "registro(s) eliminado(s)")
else:
    print("Error en la conexión")