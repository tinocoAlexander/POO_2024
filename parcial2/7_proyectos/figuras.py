class Figura:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

    def CalcularArea(self, area):
        self.area = area

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getArea(self):
        return self.area
    
    def setArea(self, area):
        self.area = area

class Rectangulo(Figura):
    def __init__(self, nombre, area, largo, ancho):
        super().__init__(nombre, area)
        self._largo = largo
        self._ancho = ancho

    def getLargo(self):
        return self._largo
    
    def setLargo(self, largo):
        self._largo = largo

    def getAncho(self):
        return self._ancho
    
    def setAncho(self, ancho):
        self._ancho = ancho

    def CalcularArea(self, area):
        self.area = area   

class Circulo(Figura):
    def __init__(self, nombre, area, radio):
        super().__init__(nombre, area)   
        self._radio = radio   

    def getRadio(self):
        return self._radio
    
    def setRadio(self, radio):
        self._radio = radio

    def CalcularArea(self, area):
        self.area = area  

class Triangulo(Figura):
    def __init__(self, nombre, area, altura, ancho):
        super().__init__(nombre, area)  
        self._altura = altura
        self._ancho = ancho

    def getAncho(self):
        return self._ancho
    
    def setAncho(self, ancho):
        self._ancho = ancho

    def getAltura(self):
        return self._altura
    
    def setAltura(self, altura):
        self._altura = altura    

    def CalcularArea(self, area):
        self.area = area                     
