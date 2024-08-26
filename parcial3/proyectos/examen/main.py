from clases import *
from funciones import *
import getpass

def main():
    while True:
        print("Bienvenido al sistema de gestión de autos")
        print("1. Ingresar al sistema")
        print("2. Registrar al sistema")
        print("3. Salir")
        print("Seleccione una opción")
        opcion = input()
        if opcion == "1":
            email_usuario = input("Ingrese su email: ")
            contrasena_usuario = getpass.getpass("Ingrese su contraseña: ")
            consulta = "SELECT * FROM usuarios WHERE email_usuario = %s AND contrasena_usuario = %s"
            cursor.execute(consulta, (email_usuario, contrasena_usuario))
            usuario = cursor.fetchone()
            if usuario:
                main_secundario()
            else:
                print("Error al ingresar al sistema")
        elif opcion == "2":
            while True:
                email_usuario = input("Ingrese su email: ")
                if validarEmail(email_usuario):
                    print("El email ingresado ya existe")
                else:
                    break
            contrasena_usuario = getpass.getpass("Ingrese su contraseña: ")
            usuario = Usuarios(email_usuario, contrasena_usuario)
            if usuario.insertar():
                print("Usuario registrado correctamente")
            else:
                print("Error al registrar el usuario")
        elif opcion == "3":
            print("Gracias por usar nuestro sistema")
            esperarTecla()
            break
def main_secundario():
    while True:
        print("Bienvenido al sistema de gestión de autos")
        print("1. Ir a la gestión de autos")
        print("2. Ir a la gestión de revisiones")
        print("3. Ir a la gestión de clientes")
        print("4. Salir")
        print("Seleccione una opción")
        opcion = input()
        if opcion == "1":
            autos()
        elif opcion == "2":
            revisiones()
        elif opcion == "3":
            clientes()
        elif opcion == "4":
            print("Gracias por usar nuestro sistema")
            esperarTecla()
            break
        else:
            print("Opción inválida")
def autos():
    while True:
        print("Bienvenido a nuestro sistema de gestión de autos")
        print("1. Ingresar un nuevo auto")
        print("2. Consultar todos los autos")
        print("3. Actualizar un auto")
        print("4. Eliminar un auto")
        print("5. Salir")
        print("Seleccione una opción")
        opcion = input()
        if opcion == "1":
            matricula = input("Ingrese la matrícula del vehículo: ")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            color = input("Ingrese el color del vehículo: ")
            while True:
                nif = input("Ingrese el NIF del propietario: ")
                if validarNIF(nif):
                    break
                else:
                    print("El NIF ingresado no existe")
            auto = Autos(matricula, marca, modelo, color, nif)
            if auto.insertar():
                print("Auto ingresado correctamente")
            else:
                print("Error al ingresar el auto")
            esperarTecla()
        elif opcion == "2":
            autos = Autos.consultar()
            if autos is not None:
                for auto in autos:
                    print(auto)
            else:
                print("Error al consultar los autos")
            esperarTecla()
        elif opcion == "3":
            while True:
                matricula = input("Ingrese la matrícula del vehículo a actualizar: ")
                if validarMatricula(matricula):
                    break
                else:
                    print("La matrícula ingresada no existe")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            color = input("Ingrese el color del vehículo: ")
            if Autos.actualizar(matricula, marca, modelo, color):
                print("Auto actualizado correctamente")
            else:
                print("Error al actualizar el auto")
        elif opcion == "4":
            while True:
                matricula = input("Ingrese la matrícula del vehículo a eliminar: ")
                if validarMatricula(matricula):
                    break
                else:
                    print("La matrícula ingresada no existe")
            if Autos.eliminar(matricula):
                print("Auto eliminado correctamente")
            else:
                print("Error al eliminar el auto")
        elif opcion == "5":
            print("Gracias por usar nuestro sistema")
            esperarTecla()     
            break       

def revisiones():
    while True:
        print("Bienvenido a nuestro sistema de revisiones de vehículos")
        print("1. Ingresar una nueva revisión")
        print("2. Consultar todas las revisiones")
        print("3. Actualizar una revisión")
        print("4. Eliminar una revisión")
        print("5. Salir")
        print("Seleccione una opción")
        opcion = input()
        if opcion == "1":
            no_revision = int(input("Ingrese el número de revisión: "))
            cambiofiltro = input("¿Se cambió el filtro? (S/N): ").upper()
            cambioaceite = input("¿Se cambió el aceite? (S/N): ").upper()
            cambiofrenos = input("¿Se cambiaron los frenos? (S/N): ").upper()
            otros = input("Otros cambios: ")
            while True:
                matricula = input("Ingrese la matrícula del vehículo: ")
                if validarMatricula(matricula):
                    break
                else:
                    print("La matrícula ingresada no existe")
            revision = Revisiones(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
            if revision.insertar():
                print("Revisión ingresada correctamente")
            else:
                print("Error al ingresar la revisión")
            esperarTecla()
        elif opcion == "2":
            revisiones = Revisiones.consultar()
            if revisiones is not None:
                for revision in revisiones:
                    print(revision)
            else:
                print("Error al consultar las revisiones")
            esperarTecla()
        elif opcion == "3":
            while True:
                no_revision = input("Ingrese el número de revisión a actualizar: ")
                if validarNoRevision(no_revision):
                    break
                else:
                    print("El número de revisión ingresado no existe")
            
            cambiofiltro = input("¿Se cambió el filtro? (S/N): ").upper()
            cambioaceite = input("¿Se cambió el aceite? (S/N): ").upper()
            cambiofrenos = input("¿Se cambiaron los frenos? (S/N): ").upper()
            otros = input("Otros cambios: ")
            
            if Revisiones.actualizar(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros):
                print("Revisión actualizada correctamente")
            else:
                print("Error al actualizar la revisión")
        elif opcion == "4":
            while True:
                no_revision = input("Ingrese el número de revisión a eliminar: ")
                if validarNoRevision(no_revision):
                    break
                else:
                    print("El número de revisión ingresado no existe")
            if Revisiones.eliminar(no_revision):
                print("Revisión eliminada correctamente")
            else:
                print("Error al eliminar la revisión")
        elif opcion == "5":
            print("Gracias por usar nuestro sistema")
            esperarTecla()
            break
        else:
            print("Opción inválida")

def clientes():
    while True:
        print("Bienvenido a nuestro sistema de gestión de clientes")
        print("1. Ingresar un nuevo cliente")
        print("2. Consultar todos los clientes")
        print("3. Actualizar un cliente")
        print("4. Eliminar un cliente")
        print("5. Salir")
        print("Seleccione una opción")
        opcion = input()
        if opcion == "1":
            nif = input("Ingrese el NIF del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            ciudad = input("Ingrese la ciudad del cliente: ")
            tel = input("Ingrese el teléfono del cliente: ")
            cliente = Clientes(nif, nombre, direccion, ciudad, tel)
            if cliente.insertar():
                print("Cliente ingresado correctamente")
            else:
                print("Error al ingresar el cliente")
            esperarTecla()
        elif opcion == "2":
            clientes = Clientes.consultar()
            if clientes is not None:
                for cliente in clientes:
                    print(cliente)
            else:
                print("Error al consultar los clientes")
            esperarTecla()
        elif opcion == "3":
            while True:
                nif = input("Ingrese el NIF del cliente a actualizar: ")
                if validarNIF(nif):
                    break
                else:
                    print("El NIF ingresado no existe")
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            ciudad = input("Ingrese la ciudad del cliente: ")
            tel = input("Ingrese el teléfono del cliente: ")
            if Clientes.actualizar(nif, nombre, direccion, ciudad, tel):
                print("Cliente actualizado correctamente")
            else:
                print("Error al actualizar el cliente")
        elif opcion == "4":
            while True:
                nif = input("Ingrese el NIF del cliente a eliminar: ")
                if validarNIF(nif):
                    break
                else:
                    print("El NIF ingresado no existe")
            if Clientes.eliminar(nif):
                print("Cliente eliminado correctamente")
            else:
                print("Error al eliminar el cliente")
        elif opcion == "5":
            print("Gracias por usar nuestro sistema")
            esperarTecla()
            break
        else:
            print("Opción inválida")            

if __name__ == "__main__":
    main()

