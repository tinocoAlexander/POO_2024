from conexion import *
if conexion and conexion.is_connected():
    print("Conexión exitosa")

    # Crear un cursor para ejecutar sentencias SQL
    cursor = conexion.cursor()


    # Seleccionar registros de la tabla
    cursor.execute(
        """
        SELECT * FROM clientes
        """
    )
    #Obtener los registros seleccionados
    registros = cursor.fetchall()
    #Imprimir los registros seleccionados
    for registro in registros:
        print(registro)

    # Seleccionar reigstros por id
    cursor.execute(
        """
        SELECT * FROM clientes WHERE id = 1
        """
    )
    #Obtener los registros seleccionados
    registros = cursor.fetchall()
    #Imprimir los registros seleccionados
    print("Registro con el id 1:")
    for registro in registros:
        print(registro)        
    #Cerrar el cursor
    cursor.close()
else:
    print("Error en la conexión")