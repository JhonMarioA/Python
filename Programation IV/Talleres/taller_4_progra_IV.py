import csv
# Taller 4, Programación IV, Herencia simple y polimorfismo.

# ___________________________________________________________
# 1) Metodos Vehiculo y Coche
def ejercicio_1():

    class Vehiculo:
        galon_ACPM, galon_extra, galon_corriente = 10976, 16293, 19850
        combustible_recomendadoo = ""

        def __init__(self, tipo_vehiculo, color, marca_llantas):
            self.tipo_vehiculo = tipo_vehiculo
            self.color = color
            self.marca_llantas = marca_llantas
            self.mostrar_informacion()
            self.combustible_recomendado()
        
        def mostrar_informacion(self):
            print("Tipo de vehiculo:", self.tipo_vehiculo)
            print("Color:", self.color)

            if self.marca_llantas == "Michelin":
                print(f"Las llantas {self.marca_llantas} pueden durar apróx 5 años.")
            elif self.marca_llantas == "Bridgestone":
                print(f"Las llantas {self.marca_llantas} pueden durar apróx 4 años.")
            elif self.marca_llantas == "Pirelli":
                print(f"Las llantas {self.marca_llantas} pueden durar apróx 4.5 años.")

        def combustible_recomendado(self):
            if self.tipo_vehiculo == "Camión":
                print("Se recomienda usar ACPM.")
                Vehiculo.combustible_recomendadoo = "ACPM"
            elif self.tipo_vehiculo == "Automóvil":
                print("Se recomienda usar gasolina corriente.")
                Vehiculo.combustible_recomendadoo = "Gasolina corriente"
            elif self.tipo_vehiculo == "Moto":
                print("Se recomienda usar gasolina corriente.")
                Vehiculo.combustible_recomendadoo = "Gasolina corriente"


    class Coche(Vehiculo):
        distancias = {
            "Bogotá": 330,
            "Medellín": 215,
            "Cali": 200,
            "Cartagena": 885,
            "Bucaramanga": 560
        }

        def __init__(self, tipo_vehiculo, marca_llantas, color, velocidad_prom, cilindrada):
            super().__init__(tipo_vehiculo, color, marca_llantas)
            self.velocidad_prom = velocidad_prom
            self.cilindrada = cilindrada
            self.tiempo_de_viaje()
            self.gasto_de_combustible()
            self.guardar_en_csv("vehiculos.csv")

        def guardar_en_csv(self, nombre_archivo):

            datos = {
                "tipo_vehiculo": self.tipo_vehiculo,
                "color": self.color,
                "marca_llantas": self.marca_llantas,
                "velocidad_prom": self.velocidad_prom,
                "cilindrada": self.cilindrada,
                "combustible_recomendado": Vehiculo.combustible_recomendadoo
            }
            try:
                import os
                escribir_encabezado = not os.path.exists(nombre_archivo)
                with open(nombre_archivo, mode='a', newline='', encoding='utf-8') as archivo_csv:
                    writer = csv.DictWriter(archivo_csv, fieldnames=datos.keys())
                    if escribir_encabezado:
                        writer.writeheader()
                    writer.writerow(datos)
                print(f"Información guardada en {nombre_archivo}")
            except Exception as e:
                print(f"Error al guardar en CSV: {e}")

        def tiempo_de_viaje(self):
            print("\nTiempo de viaje a 5 lugares diferentes de Colombia, desde Pereira:")
            for lugar, distancia in Coche.distancias.items():
                tiempo = distancia / self.velocidad_prom
                print(f"- El tiempo aprox. para llegar a {lugar} es {tiempo:.2f} horas.")

        def gasto_de_combustible(self):
            precios = {
                "ACPM": Vehiculo.galon_ACPM,
                "Gasolina corriente": Vehiculo.galon_corriente,
                "Gasolina extra": Vehiculo.galon_extra
            }
            precio_combustible = precios.get(Vehiculo.combustible_recomendadoo, 0)
            gasto = (1000/self.cilindrada) * precio_combustible
            print(f"\nEl gasto aprox. de combustible al mes es de ${gasto:,.0f}")

        

    coche1 = Coche("Moto", "Pirelli", "Negro", 80, 600)
    coche2 = Coche("Automóvil", "Michelin", "Rojo", 100, 1600)



# ___________________________________________________________
# 2) 

def ejercicio_2():

    class Vehiculo:
        def __init__(self, color, ruedas):
            self.color = color
            self.ruedas = ruedas
            
    class Coche(Vehiculo):
        def __init__(self, color, ruedas, velocidad, cilindrada):
            super().__init__(color, ruedas)
            self.color = color
            self.velocidad = velocidad
            self.cilindrada = cilindrada

    class Camioneta(Coche):
        def __init__(self, color, ruedas, velocidad, cilindrada, carga):
            super().__init__(color, ruedas, velocidad, cilindrada)
            self.carga = carga

    class Bicicleta(Vehiculo):
        def __init__(self, color, ruedas, tipo):
            super().__init__(color, ruedas)
            self.tipo = tipo

    class Motocicleta(Bicicleta):
        def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
            super().__init__(color, ruedas, tipo)
            self.velocidad = velocidad
            self.cilindrada = cilindrada
    
    coche = Coche("Negro", 4, 100, 1200)
    camioneta = Camioneta("Rojo", 4, 90, 1500, 800)
    bicicleta = Bicicleta("Azul", 2, "Urbana")
    motocicleta = Motocicleta("Negra", 2, "Deportiva", 150, 600)
    vehiculos = [coche, camioneta, bicicleta, motocicleta]

    def catalogar(vehiculos, ruedas=None):
        encontrados = []

        if ruedas is not None:
            for v in vehiculos:
                if v.ruedas == ruedas:
                    encontrados.append(v)
            print(f"Se han encontrado {len(encontrados)} vehículos con {ruedas} ruedas:")
        else:
            encontrados = vehiculos

        for v in encontrados:
            print(f"{v.__class__.__name__}: {vars(v)}")

    catalogar(vehiculos, 0)
    print("___" * 40);
    catalogar(vehiculos, 2)
    print("___" * 40);
    catalogar(vehiculos, 4)
    print("___" * 40);


# ___________________________________________________________
# 3) 

def ejercicio_3():

    class Figura():
        def __init__(self, medida1, medida2 = None):
            self.medida1 = medida1
            self.medida2 = medida2
        
        def area(self):
            pass

    class Rectangulo(Figura):
        def __init__(self, medida1, medida2):
            super().__init__(medida1, medida2)

        def area(self):
            print(f"Área del rectangulo: {self.medida1 * self.medida2}")

    class Triangulo(Figura):
        def __init__(self, medida1, medida2):
            super().__init__(medida1, medida2)

        def area(self):
            print(f"Área del triangulo {(self.medida1 * self.medida2) * 1/2}")

    class Circulo(Figura):
        def __init__(self, medida):
            super().__init__(medida)

        def area(self):
            print(f"Área del circulo {self.medida1 * self.medida1 * 3.14}")

    rectangulo = Rectangulo(2, 4)
    triangulo = Triangulo(3, 3)
    circulo = Circulo(4)

    figuras = [rectangulo, triangulo, circulo]

    for f in figuras:
        f.area()

# ___________________________________________________________
# 4)

def ejercicio_4():

    class Transporte:
        def __init__(self, capacidad, tarifa):
            self.capacidad = capacidad
            self.tarifa = tarifa

        def calcular_pasaje(self, km):
            pass

    class Bus(Transporte):
        def calcular_pasaje(self, km):
            return self.tarifa + (100 * km)

    class Taxi(Transporte):
        def calcular_pasaje(self, km):
            return 500 * km

    class Metro(Transporte):
        def calcular_pasaje(self, km):
            return self.tarifa  
        
    bus = Bus(capacidad=40, tarifa=2000)
    taxi = Taxi(capacidad=4, tarifa=0)  
    metro = Metro(capacidad=200, tarifa=2500)

    transportes = [bus, taxi, metro]

    for t in transportes:
        print(f"{t.__class__.__name__}: ${t.calcular_pasaje(10):,}")

