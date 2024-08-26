from clases import *
from funciones import *
import getpass

def main():
    while True:
        borraPantalla()
        print("Bienvenido a la veterinaria")
        print("Menu de opciones")
        print("1. Ingresar")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion == "1":
            login()
        elif opcion == "2":
            registro()
        elif opcion == "3":
            print("Gracias por usar el sistema")
            esperarTecla()
            break;
        else:
            print("Opcion invalida")

def registro():
    borraPantalla()
    print("Registro de usuario")
    print("Ingrese los siguientes datos")
    CURP_persona = input("Ingrese su CURP: ")
    nombre_persona = input("Ingrese su nombre: ")
    direccion_persona = input("Ingrese su direccion: ")
    telefono_persona = input("Ingrese su telefono: ")
    contrasena_persona = getpass.getpass("Ingrese su contrasena: ")
    print("¿Es usted cliente o empleado?")
    print("1. Cliente")
    print("2. Empleado")
    tipo_persona = input("Ingrese la opcion: ")
    if tipo_persona == "1":
        print("Registro de cliente")
        clave_cliente = input("Ingrese su clave de cliente, tienen que ser 10 caraceteres alfanumericos: ")
        tipo_cliente = input("Ingrese el tipo de cliente: ")
        objeto_persona = Personas(CURP_persona, nombre_persona, direccion_persona, telefono_persona, contrasena_persona)
        objeto_persona.registrar_persona()
        objeto_cliente = Clientes(clave_cliente, tipo_cliente, privilegio = 0, CURP_persona=CURP_persona)
        objeto_cliente.registrar_cliente()
        if objeto_cliente and objeto_persona:
            print("Registro exitoso")
            esperarTecla()
        else:
            print("Error en el registro")
            esperarTecla()
        
    elif tipo_persona == "2":
        print("Registro de empleado")
        clave_empleado = input("Ingrese su clave de empleado, tienen que ser 10 caraceteres alfanumericos: ")
        puesto_empleado = input("Ingrese su puesto: ")
        salario_empleado = float(input("Ingrese su salario: "))
        objeto_persona = Personas(CURP_persona, nombre_persona, direccion_persona, telefono_persona, contrasena_persona)
        objeto_persona.registrar_persona()
        objeto_empleado = Empleados(clave_empleado, puesto_empleado, salario_empleado, privilegio=1, CURP_persona=CURP_persona)
        objeto_empleado.registrar_empleado()
        if objeto_empleado and objeto_persona:
            print("Registro exitoso")
            esperarTecla()
        else:
            print("Error en el registro")
            esperarTecla()
    else:
        print("Opcion invalida")


def login():
    borraPantalla()
    print("Inicio de sesion")
    CURP_persona = input("Ingrese su CURP: ")
    contrasena_persona = getpass.getpass("Ingrese su contrasena: ")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM personas WHERE CURP_persona = %s AND contrasena_persona = %s", (CURP_persona, contrasena_persona))
    resultado = cursor.fetchone()
    if resultado:
        print("Inicio de sesion exitoso")
        cursor.execute("SELECT privilegio FROM empleados WHERE CURP_persona = %s", (CURP_persona,))
        privilegio = cursor.fetchone()
        if privilegio[0] == 0:
            borraPantalla()
            print("Menu de opciones")
            print("1. Agendar cita")
            print("2. Salir")
            opcion = input("Ingrese la opcion: ")
            if opcion == "1":
                print("¿Tiene ya registrado un animal?")
                print("1. Si")
                print("2. No")
                opcion = input("Ingrese la opcion: ")
                if opcion == "1":
                    clave_animal = input("Ingrese la clave del animal: ")
                    cursor.execute("SELECT * FROM animales WHERE clave_animal = %s", (clave_animal,))
                    resultado = cursor.fetchone()
                    if resultado:
                        fecha_cita = input("Ingrese la fecha de la cita: ")
                        clave_cliente = resultado[1]
                        clave_empleado = input("Ingrese la clave del empleado: ")
                        clave_veterinaria = input("Ingrese la clave de la veterinaria: ")
                        clave_animal = resultado[0]
                        clave_servicio = input("Ingrese la clave del servicio: ")
                        consulta = "INSERT INTO citas (fecha_cita, clave_cliente, clave_empleado, clave_veterinaria, clave_animal, clave_servicio) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.execute(consulta, (fecha_cita, clave_cliente, clave_empleado, clave_veterinaria, clave_animal, clave_servicio))
                        conexion.commit()
                        print("Cita agendada")
                        esperarTecla()
                    else:
                        print("El animal no existe")
                        esperarTecla()
                esperarTecla()
        elif privilegio[0] == 1:
            while True:
                borraPantalla()
                print("Menu de opciones")
                print("1. Agregar servicio")
                print("2. Agregar vacunas a animal")
                print("3. Agregar consultas a animal")
                print("4. Mostar citas")
                print("5. Mostrar servicios")
                print("6. Mostrar animales")
                print("7. Mostrar clientes")
                print("8. Salir")
                opcion = input("Ingrese la opcion: ")
                if opcion == "1":
                    clave_servicio = input("Ingrese la clave del servicio: ")
                    nombre_servicio = input("Ingrese el nombre del servicio: ")
                    descripcion_servicio = input("Ingrese la descripcion del servicio: ")
                    costo_servicio = float(input("Ingrese el costo del servicio: "))
                    consulta = "INSERT INTO servicios (clave_servicio, nombre_servicio, descripcion_servicio, costo_servicio) VALUES (%s, %s, %s, %s)"
                    cursor.execute(consulta, (clave_servicio, nombre_servicio, descripcion_servicio, costo_servicio))
                    conexion.commit()
                    print("Servicio agregado")
                    esperarTecla()
                elif opcion == "2":
                    numero_vacuna = input("Ingrese el numero de vacuna: ")
                    clave_animal = input("Ingrese la clave del animal: ")
                    consulta = "SELECT * FROM animales WHERE clave_animal = %s"
                    cursor.execute(consulta, (clave_animal,))
                    resultado = cursor.fetchone()
                    if resultado:
                        consulta = "INSERT INTO vacunas (numero_vacuna, clave_animal) VALUES (%s, %s)"
                        cursor.execute(consulta, (numero_vacuna, clave_animal))
                    else:
                        print("El animal no existe")
                    esperarTecla()
                elif opcion == "3":
                    numero_consultas = input("Ingrese el numero de consulta: ")
                    clave_animal = input("Ingrese la clave del animal: ")
                    consulta = "SELECT * FROM animales WHERE clave_animal = %s"
                    cursor.execute(consulta, (clave_animal,))
                    resultado = cursor.fetchone()
                    if resultado:
                        consulta = "INSERT INTO consultas (numero_consultas, clave_animal) VALUES (%s, %s)"
                        cursor.execute(consulta, (numero_consultas, clave_animal))
                    else:
                        print("El animal no existe")
                    esperarTecla()
                elif opcion == "4":
                    consulta = "SELECT * FROM citas"
                    cursor.execute(consulta)
                    resultado = cursor.fetchall()
                    for fila in resultado:
                        print(fila)
                    esperarTecla()    
                elif opcion == "5":
                    consulta = "SELECT * FROM servicios"
                    cursor.execute(consulta)
                    resultado = cursor.fetchall()
                    for fila in resultado:
                        print(fila)
                    esperarTecla()    
                elif opcion == "6":
                    consulta = "SELECT * FROM animales"
                    cursor.execute(consulta)
                    resultado = cursor.fetchall()
                    for fila in resultado:
                        print(fila)
                    esperarTecla()
                elif opcion == "7":
                    consulta = "SELECT * FROM clientes"
                    cursor.execute(consulta)
                    resultado = cursor.fetchall()
                    for fila in resultado:
                        print(fila)
                    esperarTecla()
                elif opcion == "8":
                    print("Gracias por usar el sistema")
                    esperarTecla()
                    return
                else:
                    print("Opcion invalida")
                    esperarTecla()
    else:
        print("Inicio de sesion fallido")
        esperarTecla()

if __name__ == "__main__":
    main()