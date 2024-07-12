from mysql.connector import connect, Error

def obtener_conexion():
    try:
        conexion = connect(
            host="localhost",
            user="root",
            password="",
            database="bd_python"
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

conexion = obtener_conexion()
