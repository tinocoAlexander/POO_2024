class Coche:
    def __init__(self, color, marca, modelo, matricula):
        self.color = color
        self.marca = marca
        self._modelo = modelo # Atributo protegido
        self.__matricula = matricula # Atributo privado


    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula


    def Arrancar(self):
        print("El coche ha arrancado")
    
    def Acelerar(self):
        print("El coche ha acelerado")  
    
    def Frenar(self):
        print("El coche ha frenado")

# Haz un objeto e intenta acceder a los atributos de la clase Coche
coche1= Coche("Rojo","Toyota","Corolla","ABC123")
print(coche1.color)
print(coche1.marca)
print(coche1._modelo)
print(coche1.matricula)



