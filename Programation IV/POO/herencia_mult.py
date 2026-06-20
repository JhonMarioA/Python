
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola")

#Herencia simple

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)       #Heredando atributos de Persona
        self.trabajo = trabajo
        self.salario = salario

class Estudiante (Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)       #Heredando atributos de Persona
        self.notas = notas
        self.universidad = universidad

#Herencia múltiple 
    

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidades(self):
        print(f"Mi habilidad es {self.habilidad}")

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return f"Mi habilidada es: {self.habilidad}"


Karl = EmpleadoArtista("Karl", 22, "Argentino", "Pintar", "Pintuco", 1000)
Juan = Empleado("Juan", 21, "Peruano", "Programador", 1000000)
print(Juan.edad)
Juan.hablar()
print(Juan.salario)

print(Karl.presentarse())
print(issubclass(EmpleadoArtista, Artista))
print(isinstance(Karl, EmpleadoArtista))

