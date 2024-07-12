from conexion import conexion
# Asegúrate de que la conexión se realizó correctamente
if conexion and conexion.is_connected():
    print("Conexión exitosa")

    # Crear un cursor para ejecutar sentencias SQL
    cursor = conexion.cursor()

    # Crear una tabla si no existe
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(60),
            direccion VARCHAR(60),
            telefono VARCHAR(10)
        )
        """
    )
    # Imprimir si la tabla ya existía a la hora de crearla
    if cursor.rowcount == 0:
        print("La tabla ya existía")
    else:
        print("Tabla creada exitosamente")

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
else:
    print("Error en la conexión")
