# ENCAPSULAMIENTO

class MiClase:
    def __init__(self):
        self.__atributo_privado = "valor"

    def __hablar(self):
        print("hello")


objeto = MiClase()
# print(objeto.__atributo_privado)
# print(objeto.__hablar())


# SETTERS & GETTERS

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre            
        self.__edad = edad
    
    def get_nombre(self):    # Getter
        return self.__nombre

    def set_nombre(self, new_nombre):    # Setter
        self.__nombre = new_nombre

Jhon = Persona("Mario", 18)
nombre = Jhon.get_nombre()
print(nombre)

Jhon.set_nombre("Messi")
nombre = Jhon.get_nombre()
print(nombre)





