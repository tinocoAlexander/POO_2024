"""
Programación Orientada a Objetos (POO) o OOP

Clases: es como un molde a través del cual se puede instanciar un objeto. Dentro de las clases se 
definen atributos (propiedades/características) y los métodos (funciones o acciones).

Objetos o instancias: son parte de una clase, los objetos o instancias pertenecen a una clase.
Es decir, interactúan con la clase o clases y para hacer uso de los atributos y métodos es necesario
crear un objeto u objetos.

Método constructor: este método especial se coloca dentro de la clase y se utiliza para dar un valor a
los atributos del objeto de crear
"""

"""
Ejemplo 1: crear una clase (un molde para crear más objetos) llamada Coche y a partir de la clase
crear objetos o instancias (coche) con características similares.
"""

class Coche:
    """
    - Atributos o propiedades (variables)
    - Características del coche
    - Valores iniciales es posible declarar al principio de una clase
    """

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    #def __init__(self, marca, color):
        #self.marca = marca
        #self.color = color  

    # Métodos o acciones o funciones que hace el objeto

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def get_caballaje(self):
        return self.caballaje

    def set_caballaje(self, caballaje):
        self.caballaje = caballaje

    def get_plazas(self):
        return self.plazas

    def set_plazas(self, plazas):
        self.plazas = plazas

    def get_info(self):
        return f"Marca: {self.marca}, Color: {self.color}, Modelo: {self.modelo}, Velocidad: {self.velocidad}, Caballaje: {self.caballaje}, Plazas: {self.plazas}"

    """""
        En python el encapsulamiento tambien se le llama visibilidad y por lo general define como seran
        los atributos y metodos es decir publicos o privados
    """""
    #Atributo publico
    publico_atributo="Soy un atributo publico"
    #Atributo privado
    __privado_atributo="Soy un atributo privado"

    #Nota 1: para utilizar un atributo privado, se tendría que hacer dentro de un método que fuera publico
    def getPrivadoAtributo(self):
        return self.__privado_atributo
    
    #Metodo privado
    def __getFuncionPrivada(self):
        print("Soy un metodo privado")

    #por medio del doble __ python identifica que el atributo o el metodo es privado
# Fin de definición de la clase

