# TALLER 6
# Encapsulamiento

#1) __________________________________________

class Figura():
    def __init__(self, medida1, medida2=None):
        self.__medida1 = medida1
        self.__medida2 = medida2

    def set_medida1(self, nueva_medida):
        if isinstance(nueva_medida, (int, float)) and nueva_medida > 0:
            self.__medida1 = nueva_medida

    def set_medida2(self, nueva_medida2):
        if isinstance(nueva_medida2, (int, float)) and nueva_medida2 > 0:
            self.__medida2 = nueva_medida2
        
    def get_medida1(self):
        return self.__medida1
    
    def get_medida2(self):
        return self.__medida2


class Circulo(Figura):

    def __init__(self, medida1):
        super().__init__(medida1)

    def calcular_area(self):
        medida1 = self.get_medida1()
        print(f"El área del círculo es {medida1 ** 2 * 3.14}cm²." )

class Triangulo(Figura):

    def __init__(self, medida1, medida2):
        super().__init__(medida1, medida2)

    def calcular_area(self):
        medida1 = self.get_medida1()
        medida2 = self.get_medida2()
        print(f"El área del triángulo es {medida1 * medida2 * 0.5}cm².")

class Cuadrado(Figura):

    def __init__(self, medida1):
        super().__init__(medida1)

    def calcular_area(self):
        medida1= self.get_medida1()
        print(f"El área del cuadrado es {medida1 ** 2}cm².")

class Rectangulo(Figura):
    def __init__(self, medida1, medida2):
        super().__init__(medida1, medida2)

    def calcular_area(self):
        medida1= self.get_medida1()
        medida2= self.get_medida2()
        print(f"El área del rectángulo es {medida1 * medida2}cm².")


figuras = [
    Circulo(5),
    Triangulo(10, 8),
    Cuadrado(4),
    Rectangulo(6, 3)
]

for f in figuras:
    f.calcular_area()





