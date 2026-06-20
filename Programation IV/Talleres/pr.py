class Padre:
    def saludar(self):
        print("saludo desde la clase Padre")

class Hija(Padre):
    def saludar(self):
        print("saludo desde la clase Hija")
        super().saludar()


hija = Hija() 
hija.saludar()
