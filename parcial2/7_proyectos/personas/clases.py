# Definición de la primera clase que va a heredar a las demás
class Personas:
    def __init__(self, nombre, edad, tel):
        self.nombre = nombre
        self.edad = edad
        self.tel = tel

    #Método de obtención de información
    def info_persona(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Teléfono: {self.tel}"

    #Métodos getter y setter
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self,edad):
        self.edad = edad

    def get_tel(self):
        return self.tel

    def set_tel(self, tel):
        self.tel = tel             

#Clase Estudiantes que hereda de la clase Personas
class Estudiantes(Personas):
    def __init__(self, nombre, edad, tel,carrera,matricula):
        super().__init__(nombre, edad, tel)
        self.__carrera = carrera
        self.__matricula = matricula

    #Metodo de obtención de información 
    def info_persona(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Teléfono: {self.tel}, Carrera: {self.__carrera},Matricula: {self.__matricula}"   
    
    #Métodos getter y setter
    def get_carrera(self):
        return self.__carrera
    
    def set_carrera(self,carrera):
        self.__carrera = carrera

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    #Crear método informar_carrera
    def informar_carrera(self):
        return f"La carrera del alumno es {self.__carrera}"      

#Clase Maestros que hereda de la clase Personas
class Docentes(Personas):
    def __init__(self, nombre, edad, tel, modalidad, num_empleado):
        super().__init__(nombre, edad, tel)            
        self.__modalidad = modalidad
        self.__num_empleado = num_empleado

    #Método de obtención de información
    def info_persona(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Teléfono: {self.tel}, Modalidad: {self.__modalidad}, Número de empleado: {self.__num_empleado}"

    #Métodos getter y setter
    def get_modalidad(self):
        return self.__modalidad

    def set_modalidad(self,modalidad):
        self.__modalidad = modalidad

    def get_num_empleado(self):
        return self.__num_empleado

    def set_num_empleado(self,num_empleado):
        self.__num_empleado = num_empleado

    #Crear método informar_modalidad
    def informar_modalidad(self):
        return f"La modalidad del maestro es {self.__modalidad}"    