# Clase padre que pasará a heredar a nuestras clases hijas
class Personas:
    def __init__(self, nombre, apellidoP, apellidoM, edad, telefono, email, direccion, escuela, sesion_iniciada=False, contrasena=None):
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.edad = edad
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.escuela = escuela
        self.sesion_iniciada = sesion_iniciada
        self.contrasena = contrasena

    # Métodos para la gestión de sesión
    def iniciar_sesion(self, contrasena):
        if self.contrasena and self.contrasena == contrasena:
            self.sesion_iniciada = True
            return "Sesión iniciada correctamente."
        return "Contraseña incorrecta."

    def cerrar_sesion(self):
        self.sesion_iniciada = False
        return "Sesión cerrada correctamente."

    def crear_cuenta(self, contrasena):
        self.contrasena = contrasena
        return "Cuenta creada correctamente."

    def eliminar_cuenta(self):
        self.contrasena = None
        self.cerrar_sesion()
        return "Cuenta eliminada correctamente."

    def cambiar_contraseña(self, contrasena):
        self.contrasena = contrasena
        return "Contraseña cambiada correctamente."

    # Métodos getter y setter para cada uno de los atributos
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellidoP(self):
        return self.apellidoP
    
    def set_apellidoP(self, apellidoP):
        self.apellidoP = apellidoP

    def get_apellidoM(self):
        return self.apellidoM
    
    def set_apellidoM(self, apellidoM):
        self.apellidoM = apellidoM

    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad

    def get_telefono(self):
        return self.telefono
    
    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def get_direccion(self):
        return self.direccion
    
    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_escuela(self):
        return self.escuela
    
    def set_escuela(self, escuela):
        self.escuela = escuela

    # Método getInfo para imprimir los datos
    def get_info(self):
        return f"Nombre: {self.nombre}, Apellido paterno: {self.apellidoP}, Apellido materno: {self.apellidoM}, Edad: {self.edad}, Teléfono: {self.telefono}, Email: {self.email}, Dirección: {self.direccion}, Escuela: {self.escuela}, Sesión iniciada: {self.sesion_iniciada}"

    # Método actividad_diaria
    def actividad_diaria(self):
        return "Realizar actividades diarias generales."

# Clase hija 1: Estudiantes
class Estudiantes(Personas):
    def __init__(self, nombre, apellidoP, apellidoM, edad, telefono, email, direccion, escuela, matricula, grado, grupo, promedio, modalidad_carrera, carrera):
        super().__init__(nombre, apellidoP, apellidoM, edad, telefono, email, direccion, escuela)
        self.matricula = matricula
        self.grado = grado
        self.grupo = grupo
        self.promedio = promedio
        self.modalidad_carrera = modalidad_carrera
        self.carrera = carrera

    # Herencia de método getInfo
    def get_info(self):
        return super().get_info() + f", Matrícula: {self.matricula}, Grado: {self.grado}, Grupo: {self.grupo}, Promedio: {self.promedio}, Modalidad de Carrera: {self.modalidad_carrera}, Carrera: {self.carrera}"
    
    # Métodos específicos para estudiantes
    def consultar_calificaciones(self):
        return f"El alumno '{self.get_nombre()}' está consultando sus calificaciones."

    # Método actividad_diaria
    def actividad_diaria(self):
        return f"El estudiante '{self.get_nombre()}' asiste a clases y estudia."

    # Métodos getter y setter
    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_grado(self):
        return self.grado
    
    def set_grado(self, grado):
        self.grado = grado

    def get_grupo(self):
        return self.grupo
    
    def set_grupo(self, grupo):
        self.grupo = grupo

    def get_promedio(self):
        return self.promedio
    
    def set_promedio(self, promedio):
        self.promedio = promedio

    def get_modalidad_carrera(self):
        return self.modalidad_carrera
    
    def set_modalidad_carrera(self, modalidad_carrera):
        self.modalidad_carrera = modalidad_carrera

    def get_carrera(self):
        return self.carrera
    
    def set_carrera(self, carrera):
        self.carrera = carrera

# Clase hija 2: Profesores
class Profesores(Personas):
    def __init__(self, nombre, apellidoP, apellidoM, edad, telefono, email, direccion, escuela, puesto, salario, antiguedad, titulo_maestro, materias_impartidas):
        super().__init__(nombre, apellidoP, apellidoM, edad, telefono, email, direccion, escuela)
        self.puesto = puesto
        self.salario = salario
        self.antiguedad = antiguedad
        self.titulo_maestro = titulo_maestro
        self.materias_impartidas = materias_impartidas

    # Herencia de método getInfo
    def get_info(self):
        return super().get_info() + f", Puesto: {self.puesto}, Salario: {self.salario}, Antigüedad: {self.antiguedad}, Título de Maestro: {self.titulo_maestro}, Materias Impartidas: {self.materias_impartidas}"

    # Métodos específicos para profesores
    def anadir_calificaciones(self):
        return f"El maestro '{self.get_nombre()}' está añadiendo calificaciones."

    def actualizar_calificaciones(self):
        return f"El maestro '{self.get_nombre()}' está actualizando calificaciones."

    # Método actividad_diaria
    def actividad_diaria(self):
        return f"El profesor '{self.get_nombre()}' da clases y evalúa a los estudiantes."

    # Métodos getter y setter
    def get_puesto(self):
        return self.puesto
    
    def set_puesto(self, puesto):
        self.puesto = puesto

    def get_salario(self):
        return self.salario
    
    def set_salario(self, salario):
        self.salario = salario

    def get_antiguedad(self):
        return self.antiguedad
    
    def set_antiguedad(self, antiguedad):
        self.antiguedad = antiguedad

    def get_titulo_maestro(self):
        return self.titulo_maestro
    
    def set_titulo_maestro(self, titulo_maestro):
        self.titulo_maestro = titulo_maestro

    def get_materias_impartidas(self):
        return self.materias_impartidas
    
    def set_materias_impartidas(self, materias_impartidas):
        self.materias_impartidas = materias_impartidas

# Clase Clases que hereda de Profesores
class Clases(Profesores):
    def __init__(self, nombre, apellidoP, apellidoM, edad, telefono, email, direccion, escuela, puesto, salario, antiguedad, titulo_maestro, materias_impartidas, nombre_clase, horario):
        super().__init__(nombre, apellidoP, apellidoM, edad, telefono, email, direccion, escuela, puesto, salario, antiguedad, titulo_maestro, materias_impartidas)
        self.nombre_clase = nombre_clase
        self.horario = horario

    # Métodos getter y setter
    def get_nombre_clase(self):
        return self.nombre_clase
    
    def set_nombre_clase(self, nombre_clase):
        self.nombre_clase = nombre_clase

    def get_horario(self):
        return self.horario
    
    def set_horario(self, horario):
        self.horario = horario

    # Herencia de método getInfo
    def get_info(self):
        return super().get_info() + f", Nombre de la Clase: {self.nombre_clase}, Horario: {self.horario}"

# Clase Calificaciones que contiene instancias de Estudiantes y Clases
class Calificaciones:
    def __init__(self, estudiante, clase, calificaciones):
        self.estudiante = estudiante
        self.clase = clase
        self.calificaciones = calificaciones

    # Métodos getter y setter
    def get_calificaciones(self):
        return self.calificaciones
    
    def set_calificaciones(self, calificaciones):
        self.calificaciones = calificaciones

    # Método getInfo
    def get_info(self):
        return self.estudiante.get_info() + f", Clase: {self.clase.nombre_clase}, Horario: {self.clase.horario}, Calificaciones: {self.calificaciones}"
