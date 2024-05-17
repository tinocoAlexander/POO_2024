"""
    En Python en modo consola para la salida de datos o impresión se utiliza
    la función "print" y para la entrada de datos se utiliza la función
    "input"
"""

#Solicitar los datos del alumno ¿
nombre=input("Nombre del alumno: ")
matricula=int(input("Matricula del alumno: "))
especialidad=input("Especialidad del alumno: ")
edad=int(input("Edad: "))
estatura=float(input("Estatura: "))

print(f"""
      Bienvenido, {nombre}.
            Matricula: {matricula}
            Especialidad: {especialidad}
            Edad: {edad}
            Estatura: {estatura}
      """)