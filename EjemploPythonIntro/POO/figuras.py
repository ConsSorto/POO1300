import math
from abc import ABC, abstractmethod


"""
Programa para calcular areas y perimetros de las figuras geometricas

"""
class Visualizacion:
    def __init__(self, color, textura, texto, nombre):
        self.color = color
        self.textura = textura
        self.texto = texto
        self.nombre = nombre

class Figuras(ABC):

    def __init__(self):
        self.area = 0
        self.perimetro = 0

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass


class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        self.area = math.pi * self.radio ** 2

    def calcularPerimetro (self):
        self.perimetro = 2 * math.pi * self.radio

cir = Circulo(10)
print(cir)


class FiguraCuadrilateros(Figuras):
    def __init__(self, lado1, lado2, lado3, lado4):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4
        self.nombre = "Cuadrilateros"
    def calcularArea(self):
        self.area = self.lado1 * self.lado2

    def calcularPerimetro(self):
        self.perimetro = self.lado1 * 2 + self.lado2 * 2

    def __str__(self):
        return f'Tipo : {self.nombre}, Area: {self.area}, Perimetro: {self.perimetro}'


class Cuadrado(FiguraCuadrilateros, Visualizacion):
    def __init__(self, lado):
        FiguraCuadrilateros.__init__(self, lado, lado, lado, lado)
        Visualizacion.__init__(self, "Amarillo", "Granito"
                               , "Esto si que es un cuadrado y queremos que se mire la diferencia", "Visualizacion Customizada")
        self.nombre = "Cuadrado"
        self.color = "Negro"
        self.textura = "Granos"
        #self.texto = "Esto es un cuadrado"


class Rectangulo(FiguraCuadrilateros):
    def __init__(self, lado1, lado2):
        super().__init__(lado1, lado2, lado1, lado2)
        self.nombre = "Rectangulo"

class Romboide(FiguraCuadrilateros):
    def __init__(self, lado1, lado2, h):
        super().__init__(lado1, lado2, lado1, lado2)
        self.nombre = "Romboide"
        self.h = h

    def calcularArea(self):
        self.area = self.lado1 * self.h

cua = Cuadrado(5)
cua.calcularArea()
cua.calcularPerimetro()
print(cua.texto)
print(cua)

rec = Rectangulo(2,3)
rec.calcularArea()
rec.calcularPerimetro()
print(rec)

rom = Romboide(4,2,2)
rom.calcularArea()
rom.calcularPerimetro()
print(rom)



"""
figura = FiguraCuadrado(1,2,1,2)

figura.calcularArea()
figura.calcularPerimetro()

print(figura)
class Cuadrado:
    nombre = "Cuadrado"

    def __init__(self, lado):
        self.lado = lado
        self.__color = "negro"

    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color
    def get_area(self):
        self.area = self.lado * self.lado

    def get_perimetro(self):
        self.perimetro = self.lado * 4

    @staticmethod
    def sumarAreas(area1, area2):
        return area2 + area1

    @staticmethod
    def calcularArea(lado, lado2):
        return lado * lado2

    def __str__(self):
        return f'La figura {Cuadrado.nombre} con lado {self.lado}, Area : {self.area}, Perimetro: {self.perimetro}'




fCuadrado = Cuadrado(2)

fCuadrado.get_area()
fCuadrado.get_perimetro()

print(fCuadrado)

print(fCuadrado.getColor())

fCuadrado.setColor("azul")

print(fCuadrado.sumarAreas(2,3))
print(Cuadrado.sumarAreas(4,5))

print(fCuadrado.getColor())
    
"""