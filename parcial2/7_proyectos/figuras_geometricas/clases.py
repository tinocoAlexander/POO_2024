import math

class Figuras:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    def estaVisible(self) -> bool:
        return self.visible

    def mostrar(self):
        return "La figura se está mostrando"

    def ocultar(self):
        return "La figura no está visible"

    def mover(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def calcularArea(self) -> float:
        pass

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_visible(self):
        return self.visible

    def set_visible(self, visible):
        self.visible = visible

class Rectangulos(Figuras):
    def __init__(self, x, y, alto, ancho, visible):
        super().__init__(x, y, visible)
        self.__alto = alto
        self.__ancho = ancho

    def calcularArea(self) -> float:
        return self.__alto * self.__ancho

    def mostrar(self):
        return super().mostrar() + f", esta figura es un rectángulo, su alto es {self.__alto}, su ancho es {self.__ancho}, su área es {self.calcularArea()} y su posición es {self.x},{self.y}"

    def ocultar(self):
        return super().ocultar() + f", esta figura es un rectángulo"

    def get_alto(self):
        return self.__alto

    def set_alto(self, alto):
        self.__alto = alto

    def get_ancho(self):
        return self.__ancho

    def set_ancho(self, ancho):
        self.__ancho = ancho

class Circulos(Figuras):
    def __init__(self, x, y, radio, visible):
        super().__init__(x, y, visible)
        self.__radio = radio

    def calcularArea(self) -> float:
        return math.pi * self.__radio ** 2

    def mostrar(self):
        return super().mostrar() + f", esta figura es un círculo, su radio es {self.__radio}, su área es {self.calcularArea()} y su posición es {self.x},{self.y}"

    def ocultar(self):
        return super().ocultar() + f", esta figura es un círculo"

    def get_radio(self):
        return self.__radio

    def set_radio(self, radio):
        self.__radio = radio