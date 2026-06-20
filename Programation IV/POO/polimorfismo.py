

class Animal():
    def sonido(self):
        pass

class Cat(Animal):
    def sound(self):
        return "Miau"

class Dog(Animal):
    def sound(self):
        return "Guao"

def make_sound(Animal):
    print(Animal.sound())

cat = Cat()
dog = Dog()

make_sound(cat)
