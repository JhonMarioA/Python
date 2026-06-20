
# Polimorfismo y herencia simple

class Animal():
    def hablar (self):
        print("Soy un animal.")

class Perro(Animal):
    def hablar(self):
        print("Woof!")

class Gato(Animal):
    def hablar(self):
        print("Meow!")

animal = Animal() 
perro = Perro()
gato = Gato()

def dar_voz(objeto):
    objeto.hablar()

animales = [Animal(), Perro(), Gato()]

for animal in animales:
    animal.hablar()
