#Clase padre que pasará a heredar a nuestras clases hijas
class Personas:
    def __init__(self, nombre, apellidoP, apellidoM, edad, telefono, email, direccion): #Declaración de atributos
        self.nombre=nombre
        self.apellidoP=apellidoP
        self.apellidoM=apellidoM
        self.edad=edad
        self.telefono=telefono
        self.email=email
        self.direccion=direccion

    #Metodos que haran uso del polimorfismo
    def actividad_diaria(self):
        pass
    
    def trabajar(self):
        pass
    
    def relajarse(self):
        pass
    
    #Metodos getter y setter para cada uno de los atributos
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

    #Metodo getInfo para imprimir los datos
    def get_info(self):
        return f"Nombre: {self.nombre}, Apellido paterno: {self.apellidoP}, Apellido materno: {self.apellidoM}, Edad: {self.edad}, Telefono: {self.telefono}, Email: {self.email}, Dirección: {self.direccion}"

#Clase hija 1 que hara uso de la herencia, polimorfismo y encapsulación
class Estudiantes(Personas):

    def __init__(self, nombre, apellidoP, apellidoM, edad, telefono, email, direccion, escuela, matricula, grado, grupo, promedio): #Declaración de todos los atributos
        super().__init__(nombre, apellidoP, apellidoM, edad, telefono, email, direccion) #Herencia de los atributos    
        self._escuela = escuela #Encapsulación en modo protegido
        self._matricula = matricula
        self._grado = grado
        self._grupo = grupo
        self._promedio = promedio

    #Herencia de metodo getInfo
    def get_info(self):
        return super().get_info() + f", Escuela: {self._escuela}, Matricula: {self._matricula}, Grado: {self._grado}, Promedio: {self._promedio}"
    
    #Polimorfismo de métodos
    def actividad_diaria(self):
        return f"El alumno '{self.get_nombre}' va todos a la escuela de lunes a viernes, el nombre de la escuela es: {self._escuela}"

    def trabajar(self):
        return f"El alumno '{self.get_nombre}' está haciendo sus tareas"

    def relajarse(self):
        return f"El alumno '{self.get_nombre}' se está relajando"

    #Métodos getter y setter
    def get_escuela(self):
        return self._escuela
    
    def set_escuela(self, escuela):
        self._escuela = escuela

    def get_matricula(self):
        return self._matricula
    
    def set_matricula(self, matricula):
        self._matricula = matricula

    def get_grado(self):
        return self._grado
    
    def set_grado(self, grado):
        self._grado = grado

    def get_grupo(self):
        return self._grupo
    
    def set_grupo(self, grupo):
        self._grupo = grupo

    def get_promedio(self):
        return self._promedio
    
    def set_promedio(self, promedio):
        self._promedio = promedio    

#Clase hija 2 que hara uso de la herencia, polimorfismo y encapsulación
class Maestro(Personas):
    def __init__(self, nombre, apellidoP, apellidoM, edad, telefono, email, direccion, escuela, puesto, salario, antiguedad): #Declaración de todos los atributos
        super().__init__(nombre, apellidoP, apellidoM, edad, telefono, email, direccion) #Herencia de los atributos    
        self._escuela = escuela #Encapsulación en modo protegido
        self._puesto = puesto
        self._salario = salario
        self._antiguedad = antiguedad

    #Herencia de metodo getInfo
    def get_info(self):
        return super().get_info() + f", Escuela: {self._escuela}, Puesto: {self._puesto}, Salario: {self._salario}, Antiguedad: {self._antiguedad}"
    
    #Polimorfismo de métodos
    def actividad_diaria(self):
        return f"El maestro '{self.get_nombre}' va todos a la escuela de lunes a viernes, el nombre de la escuela es: {self._escuela}"

    def trabajar(self):
        return f"El maestro '{self.get_nombre}' está haciendo dando clases a los alumnos"

    def relajarse(self):
        return f"El alumno '{self.get_nombre}' se está relajando"

    #Métodos getter y setter
    def get_escuela(self):
        return self._escuela
    
    def set_escuela(self, escuela):
        self._escuela = escuela

    def get_puesto(self):
        return self._puesto
    
    def set_puesto(self, puesto):
        self._puesto = puesto

    def get_salario(self):
        return self._salario
    
    def set_salario(self, salario):
        self._salario = salario

    def get_antiguedad(self):
        return self._antiguedad
    
    def set_antiguedad(self, antiguedad):
        self._antiguedad = antiguedad