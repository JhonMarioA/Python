# Jhon Mario Aguirre Correa, Taller 2, Programación IV
from io import *


# 1. ___________________________________

class Numero:

    entero = 123

    def suma(self):

        total = 0
        numero_lista = list(str(self.entero))

        for i in range(len(numero_lista)):
            total += int(numero_lista[i])

        return total

    def numeros_txt(self):
        archivo = open(r"C:\PROGRAMACIÓN\PYTHON\PROGRA IV\numeros.txt", "w+")
        archivo.write(str(self.entero) + "\n")
        invertido = str(self.entero)[::-1]
        archivo.write(str(invertido))

""" numero = Numero()
numero.numeros_txt()
total = numero.suma()
print(total) 
"""


# 2. ___________________________________ 

class Frase:
    def __init__(self, texto, autor):
        self.texto = texto
        self.autor = autor

    @staticmethod
    def cuenta_palabras(lista_objetos, palabra_buscar):
        cantidad = 0
        for objeto in lista_objetos:
            lista_palabras = objeto.texto.split()  
            for palabra in lista_palabras:
                if palabra == palabra_buscar:
                    cantidad += 1

        with open("frases.txt", "a") as file:
            file.write(f"La cantidad de veces que aparece la palabra '{palabra_buscar}' es {cantidad}")
        
def ingresar_datos_2():
    lista_objetos = []

    for i in range(2):
        texto = input("Ingrese el texto: ")
        autor = input("Ingrese el autor: ")
        nuevo_objeto = Frase(texto, autor)
        lista_objetos.append(nuevo_objeto)
    
    palabra_buscar = input("Ingrese la palabra a buscar: ")
    Frase.cuenta_palabras(lista_objetos, palabra_buscar)

# ingresar_datos_2()



# 3. ___________________________________ 


class Cadena:
    def __init__(self, texto):
        self.texto = texto

    lista_cadenas = []
    lista_organizada = []
    lista_vocales = ["a", "e", "i", "o", "u"]

    @staticmethod
    def llenar_lista():
        for i in range(3):
            texto = input("Ingrese el texto: ")
            cadena = Cadena(texto)
            Cadena.lista_cadenas.append(cadena)
        return Cadena.lista_cadenas

    @staticmethod
    def organizar():
        for cadena in Cadena.lista_cadenas:
            if cadena.texto[0].lower() in Cadena.lista_vocales:  
                Cadena.lista_organizada.append(cadena)
                
    @staticmethod
    def guardar_lista():
        
        archivo = open("nuevoarchivo.txt", "w+")
        for cadena in Cadena.lista_organizada:
            archivo.write(cadena.texto + "\n")


"""
Cadena.llenar_lista()
Cadena.organizar()
Cadena.guardar_lista()
"""

# 4. ___________________________________

class Cliente():
    
    def __init__(self, identificacion, edad, ciudad, saldo):
        self.identificacion = identificacion
        self.edad = edad
        self.ciudad = ciudad 
        self.saldo = saldo
        self.guardar_cliente()
        self.informacion()
    
    def guardar_cliente(self):
        with open("clientes.txt", "a") as file:
            file.write(str(self.identificacion) +" "+ str(self.edad) +" "+ self.ciudad +" "+ str(self.saldo) + "\n")
            
    def informacion(self):
        with open("clientes.txt", "r") as file:
            for linea in file:
                datos = linea.strip().split()
                saldo = float(datos[-1])  
                if saldo < 0:
                    print(linea.strip())

"""cliente = Cliente(102, 18, "Pereira", 291000)
cliente2 = Cliente(101, 31, "Cartago", -10000)"""


# 5. ___________________________________

class Electrodomestico():
    
    lista_electrodomesticos = []
    
    def __init__(self, nombre, marca, consumo):
        self.nombre = nombre
        self.marca = marca
        self.consumo = consumo
        self.clasificar()
        self.guardar()
        
    def clasificar(self):
        if self.consumo < 500:
            lista_electrodomestico = [self.nombre, self.marca, self.consumo, "Bajo consumo"]
            self.lista_electrodomesticos.append(lista_electrodomestico)
        else:
            lista_electrodomestico = [self.nombre, self.marca, self.consumo, "Alto consumo"]
            self.lista_electrodomesticos.append(lista_electrodomestico)
    def guardar(self):
        with open("electrodomesticos.txt", "w") as file:
            
            for electrodomestico in self.lista_electrodomesticos:
                file.write(str(electrodomestico) + "\n")
            

""" electrodomestico1 = Electrodomestico("Televisor", "Sansumg", 700)
 electrodomestico2 = Electrodomestico("Televisor", "Kalley", 480) """

#6. ______________________________

class Animal:
    
    lista_animales = []
    
    def __init__(self, especie, nombre, edad):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
        self.guardar()
        self.mostrar_animales()
        
    def guardar(self):
        datos_animal = [self.especie, self.nombre, self.edad]
        Animal.lista_animales.append(datos_animal)
        
        with open("animales.txt", "a") as file:
            file.write(f"{self.especie},{self.nombre},{self.edad}\n")
        
    def promedio_edades(self):
        if len(Animal.lista_animales) == 0:
            return 0
        total = sum(animal[2] for animal in Animal.lista_animales)
        return total / len(Animal.lista_animales)
        
    def mostrar_animales(self):
        promedio = self.promedio_edades()
        
        print("\nAnimales con edad mayor al promedio:")
        with open("animales.txt") as file:
            for linea in file:
                datos = linea.strip().split(",")
                especie, nombre, edad = datos[0], datos[1], int(datos[2])
                
                if edad > promedio:
                    print(especie, nombre, edad)
        
"""animal1 = Animal("Perro", "Max", 17)
animal2 = Animal("Gato", "Bov", 12)"""


#7. _______________________________

class Producto():
    
    
    def __init__(self, codigo, nombre, cantidad, precio, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria
        self.guardar()
        
    def guardar(self):
       
        
        with open("almacen.txt", "a") as file:
            file.write(f"{self.codigo}, {self.nombre}, {self.cantidad}, {self.precio}, {self.categoria}\n")
   
    @staticmethod
    def mostrar_datos():
        
        with open("almacen.txt") as file:
            for linea in file:
                datos = linea.strip().split(",")
                
                stock, valor, categoria = datos[2], datos[3], datos[4]
                print(f"Categoria: {categoria}, valor total en stock {int(stock) * int(valor)}")
                
                
    
"""  
producto1 = Producto(1001, "arroz", 10, 4000, "varios")
producto2 = Producto(1002, "lentejas", 15, 4000, "varios")
Producto.mostrar_datos()"""
                
        
        
#8. _______________________________


from datetime import datetime, date, timedelta

class Evento:
    def __init__(self, titulo, fecha, hora, lugar, responsable):
        self.titulo = titulo
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.responsable = responsable
        self.guardar()
    
    def guardar(self):
        with open("agenda.txt", "a") as file:
            file.write(f"{self.titulo},{self.fecha},{self.hora},{self.lugar},{self.responsable}\n")
    
    @staticmethod
    def mostrar_eventos_proxima_semana():
        hoy = date.today()
        dentro_de_una_semana = hoy + timedelta(days=7)
        
        print("\nEventos de la próxima semana:\n")
        
        with open("agenda.txt", "r") as file:
            for linea in file:
                titulo, fecha_str, hora, lugar, responsable = linea.strip().split(",")
                fecha_evento = datetime.strptime(fecha_str, "%Y-%m-%d").date()
                
                if hoy <= fecha_evento <= dentro_de_una_semana:
                    print(f"Título: {titulo}")
                    print(f"Fecha: {fecha_evento}")
                    print(f"Hora: {hora}")
                    print(f"Lugar: {lugar}")
                    print(f"Responsable: {responsable}")
                    print("-" * 30)

"""
evento1 = Evento("Conferencia Python", "2025-09-01", "15:00", "Auditorio A", "Profesor Juan")
evento2 = Evento("Taller de IA", "2025-09-05", "09:00", "Sala 3", "Profesor Pedro")

Evento.mostrar_eventos_proxima_semana()"""
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        