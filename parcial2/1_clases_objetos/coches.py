"""
    Programación Orientada a Objetos POO o OOP

    Clases: es como un molde a través del cual se puede instanciar un objeto. Dentro de las clases se 
    definen atributos (propiedades/características) y los métodos (funciones o acciones).

    Objetos o instancias: son parte de una clase, los objetos o instancias pertenecen a una clase.
    Es decir, interactúan con la clase o clases y para hacer uso de los atributos y métodos es necesario
    crear un objeto u objetos.
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

    # Métodos o acciones o funciones que hace el objeto

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

# Fin de definición de la clase

# Crear una instancia de la clase Coche con valores iniciales
coche1 = Coche("Ferrari", "rojo", "2010", 300, 500, 2)

# Mostrar los valores iniciales del objeto o instancia de la clase
print(f"Los valores del coche son los siguientes: \nMarca: {coche1.marca} \nColor: {coche1.color} \nModelo: {coche1.modelo} \nVelocidad: {coche1.velocidad} \nCaballaje: {coche1.caballaje} \nPlazas: {coche1.plazas}")

# Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

# Disminuir la velocidad del coche de 301 a 100
for _ in range(201):  # El rango debe ser 201 para disminuir 201 unidades y llegar a 100
    coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")

# Crear una segunda instancia de la clase Coche con diferentes valores
coche2 = Coche("Honda", "Azul", "2012", 100, 300, 3)

# Mostrar los valores iniciales del objeto o instancia de la clase
print(f"Los valores del coche son los siguientes: \nMarca: {coche2.marca} \nColor: {coche2.color} \nModelo: {coche2.modelo} \nVelocidad: {coche2.velocidad} \nCaballaje: {coche2.caballaje} \nPlazas: {coche2.plazas}")
