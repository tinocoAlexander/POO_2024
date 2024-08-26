from clases import *
from funciones import *
import getpass

def main():
    while True:
        borraPantalla()
        print("Bienvenido a nuestro sistema de calificaciones")
        print("""
        .::  Menu Principal ::. 
            1.- Registro
            2.- Login
            3.- Salir 
            """)
        opcion = input("\t Elige una opción: ")
        if opcion == "1":
            registro()
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("Gracias por utilizar nuestro sistema")
            break
        else:
            print("Opción incorrecta, por favor elige una opción válida")
            esperarTecla()

def registro():
    borraPantalla()
    print("Procederemos a registrar un nuevo usuario")
    print("Registro de usuario")
    while True:
        curp_persona = input("Escriba su CURP: ").upper()
        es_valido, mensaje = verificar_curp(curp_persona)
        print(mensaje)
        if es_valido:
            break
    nombre_persona = input("Escriba su nombre: ").upper()
    apellidop_persona = input("Escriba su apellido paterno: ").upper()
    apellidom_persona = input("Escriba su apellido materno: ").upper()
    while True:
        try:
            edad_persona = int(input("Escriba su edad: "))
            if edad_persona > 0:
                break
            else:
                print("La edad debe ser un número positivo")
        except ValueError:
            print("La edad debe ser un número entero")
    while True:
        telefono_persona = input("Escriba su telefono: ")
        if not telefono_persona.isdigit() or len(telefono_persona) != 10:
            print("El telefono debe tener 10 digitos")
        else:
            break
    while True:
        # Solicita el correo y verifica con la función verificar_correo
        email_persona = input("Escriba su correo: ").upper()
        es_valido, mensaje = verificar_correo(email_persona)
        print(mensaje)
        if es_valido:
            break
    direccion_persona = input("Escriba su direccion: ").upper()
    contrasena_persona = getpass.getpass("Escriba su contraseña: ")
    escuela_persona = input("Escriba su escuela: ").upper()
    print("Es usted un alumno o un maestro")
    print("""
        1.- Alumno
        2.- Maestro
        """)
    while True:
        tipo_persona = input("\t Elige una opción: ")
        if tipo_persona == "1":
            while True:
                matricula_estudiante = input("Escriba su matricula: ").upper()
                es_valido, mensaje = verificar_matricula_estudiante(matricula_estudiante)
                print(mensaje)
                if es_valido:
                    break
            while True:
                grado_estudiante = input("Escriba su grado: ").upper()
                # Tiene que ser solo un numero, no mas de un numero
                if int(grado_estudiante.isdigit()) and len(grado_estudiante) == 1:
                    break
                else:
                    print("El grado debe ser un número entero")
            while True:
                grupo_estudiante = input("Escriba su grupo: ").upper()
                # Tiene que ser solo una letra, no mas de una letra
                if grupo_estudiante.isalpha() and len(grupo_estudiante) == 1:
                    break
                else:
                    print("El grupo debe ser una letra")
            while True:
                try:
                    promedio_estudiante = float(input("Escriba su promedio: "))
                    if promedio_estudiante >= 0 and promedio_estudiante <= 10:
                        break
                    else:
                        print("El promedio debe ser un número entre 0 y 10")
                except ValueError:
                    print("El promedio debe ser un número")
            modalidad_estudiante = input("Escriba su modalidad: ").upper()
            carrera_estudiante = input("Escriba su carrera: ").upper()
            objeto_persona = Personas(curp_persona, nombre_persona, apellidop_persona, apellidom_persona, edad_persona, telefono_persona, email_persona, direccion_persona, contrasena_persona, escuela_persona)
            resultado1=objeto_persona.registrar()
            objeto_estudiante = Estudiantes(matricula_estudiante, grado_estudiante, grupo_estudiante, promedio_estudiante, modalidad_estudiante, carrera_estudiante, privilegio=0, CURP_persona=curp_persona)
            resultado2=objeto_estudiante.registrar()
            if resultado1 and resultado2:
                print(f"\n\t {nombre_persona} {apellidop_persona} se registro correctamente, con el email: {email_persona}")
                break
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")
                esperarTecla()
        elif tipo_persona == "2":
            while True:
                matricula_profesor = input("Escriba su matricula: ").upper()
                es_valido, mensaje = verificar_matricula_profesor(matricula_profesor)
                print(mensaje)
                if es_valido:
                    break
            puesto_profesor = input("Escriba su puesto: ").upper()
            salario_profesor = input("Escriba su salario: ")
            while True:
                antiguedad_profesor = input("Escriba su antiguedad: ")
                if int(antiguedad_profesor) >= 0:
                    break
                else:
                    print("La antiguedad debe ser un número positivo")
            titulo_profesor = input("Escriba su titulo: ").upper()
            objeto_persona = Personas(curp_persona, nombre_persona, apellidop_persona, apellidom_persona, edad_persona, telefono_persona, email_persona, direccion_persona, contrasena_persona, escuela_persona)
            resultado1=objeto_persona.registrar()
            objeto_profesor = Profesores(matricula_profesor, puesto_profesor, salario_profesor, antiguedad_profesor, titulo_profesor, privilegio=1, CURP_persona=curp_persona)
            resultado2 = objeto_profesor.registrar()
            if resultado1 and resultado2:
                print(f"\n\t {nombre_persona} {apellidop_persona} se registro correctamente, con el email: {email_persona}")
                break
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")
                esperarTecla()
        else:
            print("Opción incorrecta, por favor elige una opción válida")
            esperarTecla()
            
def login():
    borraPantalla()
    print("Procederemos a iniciar sesión")
    print("Inicio de sesión")
    email_persona = input("Escriba su correo: ").upper()
    contrasena_persona = getpass.getpass("Escriba su contraseña: ")
    cursor = conexion.cursor()
    
    consulta = "SELECT CURP_persona FROM Personas WHERE email_persona = %s AND contrasena_persona = %s"
    cursor.execute(consulta, (email_persona, contrasena_persona))
    resultado = cursor.fetchone()
    
    if resultado:
        curp_persona = resultado[0]
        print("Inicio de sesión correcto")
        esperarTecla()
        
        # Busca el privilegio según la curp en la tabla de Estudiantes y de Profesores
        consulta = "SELECT privilegio FROM Estudiantes WHERE CURP_persona = %s"
        cursor.execute(consulta, (resultado[0],))
        resultado_privilegio = cursor.fetchone()
        
        if resultado_privilegio:
            privilegio = resultado_privilegio[0]
        else:
            consulta = "SELECT privilegio FROM Profesores WHERE CURP_persona = %s"
            cursor.execute(consulta, (resultado[0],))
            resultado_privilegio = cursor.fetchone()
            
            if resultado_privilegio:
                privilegio = resultado_privilegio[0]
            else:
                privilegio = 0
                print("No se encontró CURP en Estudiantes ni Profesores, privilegio = 0")
        
        if privilegio == 0:
            while True:
                borraPantalla()
                print("Bienvenido alumno")
                print("Menu de alumno")
                print("""
                1.- Ver calificaciones
                2.- Ver materias
                3.- Cambiar contraseña
                4.- Salir
                """)
                opcion = input("\t Elige una opción: ")
                if opcion == "1":
                    # Consultar calificaciones
                    consulta = "SELECT * FROM Calificaciones WHERE matricula_estudiante = (SELECT matricula_estudiante FROM Estudiantes WHERE CURP_persona = %s)"
                    cursor.execute(consulta, (curp_persona,))
                    resultados = cursor.fetchall()
                    if resultados:
                        for resultado in resultados:
                            print(resultado)
                    else:
                        print("No se encontraron calificaciones")
                    esperarTecla()
                elif opcion == "2":
                    consulta = "SELECT * FROM Materias"
                    cursor.execute(consulta)
                    resultados = cursor.fetchall()
                    if resultados:
                        for resultado in resultados:
                            print(resultado)
                    else:
                        print("No se encontraron materias")
                    esperarTecla()    
                elif opcion == "3":
                    nueva_contrasena = getpass.getpass("Escriba su nueva contraseña: ")
                    try:
                        consulta = "UPDATE Personas SET contrasena_persona = %s WHERE CURP_persona = %s"
                        cursor.execute(consulta, (nueva_contrasena, curp_persona))
                        conexion.commit()  
                        print("Contraseña actualizada correctamente")
                    except Exception as e:
                        print(f"Error al actualizar la contraseña: {e}")
                    esperarTecla()
                elif opcion == "4":
                    #Rompe el ciclo del while
                    break    
                else:
                    print("Opción incorrecta, por favor elige una opción válida")
                    esperarTecla()
        elif privilegio == 1:
            while True:
                borraPantalla()
                print("Bienvenido profesor")
                print("Menu de profesor")
                print("""
                1.- Ver alumnos
                2.- Ver materias
                3.- Insertar calificaciones
                4.- Consultar calificaciones
                5.- Modificar calificaciones
                6.- Eliminar calificaciones
                7.- Salir
                """)
                opcion = input("\t Elige una opción: ")
                if opcion == "1":
                    # Haz que la consulta traiga todos los datos de la tabla estudiantes y agrege los nombres de la tabla personas que coinciden con las matriculas
                    consulta = "SELECT * FROM Estudiantes INNER JOIN Personas ON Estudiantes.CURP_persona = Personas.CURP_persona"
                    cursor.execute(consulta)
                    resultados = cursor.fetchall()
                    if resultados:
                        for resultado in resultados:
                            print(resultado)
                    else:
                        print("No se encontraron alumnos")
                    esperarTecla()
                elif opcion == "2":
                    consulta = "SELECT * FROM Materias"
                    cursor.execute(consulta)
                    resultados = cursor.fetchall()
                    if resultados:
                        for resultado in resultados:
                            print(resultado)
                    else:
                        print("No se encontraron materias")
                    esperarTecla()    
                elif opcion == "3":
                    # Insertar calificaciones
                    matricula_estudiante = input("Escriba la matricula del estudiante: ")
                    clave_materia = input("Escriba la clave de la materia: ")
                    calificacion = input("Escriba la calificación: ")
                    observaciones = input("Escriba las observaciones: ")
                    objeto_calificacion = Calificaciones(None, calificacion, observaciones, clave_materia, matricula_estudiante)
                    resultado = objeto_calificacion.registrar()
                    if resultado:
                        print("Calificación registrada correctamente")
                    else:
                        print("No se pudo registrar la calificación")
                    esperarTecla()
                elif opcion == "4":
                    # Consultar calificaciones
                    matricula_estudiante = input("Escriba la matricula del estudiante: ")
                    clave_materia = input("Escriba la clave de la materia: ")
                    consulta = "SELECT * FROM Calificaciones WHERE matricula_estudiante = %s AND clave_materia = %s"
                    cursor.execute(consulta, (matricula_estudiante, clave_materia))
                    resultados = cursor.fetchall()
                    if resultados:
                        for resultado in resultados:
                            print(resultado)
                    else:
                        print("No se encontraron calificaciones")
                    esperarTecla()
                elif opcion == "5":
                    # Modificar calificaciones
                    matricula_estudiante = input("Escriba la matrícula del estudiante: ")
                    clave_materia = input("Escriba la clave de la materia: ")
                    calificacion = input("Escriba la calificación: ")
                    observaciones = input("Escriba las observaciones: ")
                    
                    # Obtener el id_calificacion basado en la matrícula del estudiante y la clave de materia
                    cursor.execute(
                        "SELECT id_calificacion FROM calificaciones WHERE matricula_estudiante=%s AND clave_materia=%s",
                        (matricula_estudiante, clave_materia)
                    )
                    resultado = cursor.fetchone()

                    if resultado:
                        id_calificacion = resultado[0]
                        # Llamar al método estático actualizar de la clase Calificaciones
                        resultado = Calificaciones.actualizar(id_calificacion, calificacion, observaciones)
                        if resultado:
                            print("Calificación actualizada correctamente")
                        else:
                            print("No se pudo actualizar la calificación")
                    else:
                        print("No se encontró la calificación para la matrícula y clave de materia proporcionadas")
                    
                    esperarTecla()

                elif opcion == "6":
                    # Eliminar calificaciones
                    matricula_estudiante = input("Escriba la matrícula del estudiante: ")
                    clave_materia = input("Escriba la clave de la materia: ")
                    resultado = Calificaciones.eliminar(matricula_estudiante, clave_materia)
                    
                    if resultado:
                        print("Calificación eliminada correctamente")
                    else:
                        print("No se pudo eliminar la calificación")
                    esperarTecla()
                elif opcion == "7":
                    #Rompe el ciclo del while
                    break    
    else:
        print("Inicio de sesión incorrecto")
        esperarTecla()

    

if __name__ == '__main__':
    main()