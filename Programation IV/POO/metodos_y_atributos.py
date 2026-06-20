
#clase
class Celular: 
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self): #metodo
        print(f"Estás haciendo un llamado desde un: {self.modelo}")

    def cortar(self): #metodo
        print(f"Cortaste la llamada desde un: {self.modelo}")

#objetos - atributos
celular1 = Celular("Xiaomi", "Redmi Note 12", "48MP")
celular2 = Celular("Apple", "Iphone 13", "48MP")


print(celular1.marca)
print(celular2.marca)

celular1.llamar()