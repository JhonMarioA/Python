# =====================================================
# Sistema de gestión de reservas de habitaciones en un hotel
# =====================================================

class Habitacion:
    def __init__(self, numero, precio, estado="Disponible"):
        self.__numero = numero
        self.__precio = precio
        self.__estado = estado

    def get_numero(self):
        return self.__numero
    
    def get_precio(self):
        return self.__precio
    
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    def tipo(self):
        return type(self).__name__

    def __str__(self):
        return f"{self.tipo()} {self.__numero} - ${self.__precio} - {self.__estado}"


# ------------------------------------------------------

class HabitacionSimple(Habitacion):
    pass


class HabitacionDoble(Habitacion):
    def __init__(self, numero, precio, estado="Disponible", servicio=None, costo_servicio=0):
        super().__init__(numero, precio, estado)
        self.__servicio = servicio
        self.__costo_servicio = costo_servicio

    def get_servicio(self):
        return self.__servicio
    
    def get_costo_servicio(self):
        return self.__costo_servicio

    def set_servicio(self, servicio, costo):
        self.__servicio = servicio
        self.__costo_servicio = costo


class Suite(Habitacion):
    def __init__(self, numero, precio, estado="Disponible", servicio=None, costo_servicio=0):
        super().__init__(numero, precio, estado)
        self.__servicio = servicio
        self.__costo_servicio = costo_servicio

    def get_servicio(self):
        return self.__servicio
    
    def get_costo_servicio(self):
        return self.__costo_servicio

    def set_servicio(self, servicio, costo):
        self.__servicio = servicio
        self.__costo_servicio = costo

# ------------------------------------------------------

habitaciones = {}

# ------------------------------------------------------

def habitaciones_disponibles():
    disponibles = [h for h in habitaciones.values() if h.get_estado() == "Disponible"]
    if not disponibles:
        print("No hay habitaciones disponibles.")
    else:
        print("\nHabitaciones disponibles:")
        for h in disponibles:
            print(h)

# ------------------------------------------------------

def habitaciones_reservadas(numero_habitacion):
    if numero_habitacion in habitaciones and habitaciones[numero_habitacion].get_estado() == "Reservado":
        print("La habitación seleccionada ya está reservada.")
        return True
    return False

# ------------------------------------------------------

def servicios_adicionales():
    try:
        opc2 = int(input("¿Desea agregar servicios adicionales?\n1. Sí\n2. No\n> "))
        if opc2 == 1:
            opc3 = int(input("Seleccione un servicio:\n1. Desayuno (+30.000)\n2. Spa (+80.000)\n> "))
            if opc3 == 1:
                return "Desayuno", 30000
            elif opc3 == 2:
                return "Spa", 80000
        elif opc2 == 2:
            return None, 0
    except ValueError:
        print("Opción inválida.")
    return None, 0

# ------------------------------------------------------

def reservar():
    print("\nOpciones: ")
    try:
        opc = int(input("1) Habitación Simple\n2) Habitación Doble\n3) Suite\n> "))
    except ValueError:
        print("Opción inválida.")
        return

    numero_habitacion = input("Ingrese el número de la habitación: ")

    # Verificar que exista la habitación
    if numero_habitacion not in habitaciones:
        print("La habitación ingresada no existe en el sistema.")
        return

    existente = habitaciones[numero_habitacion]

    # Verificar si ya está reservada
    if existente.get_estado() == "Reservado":
        print("Esa habitación ya está reservada.")
        return

    # Verificar que el tipo seleccionado corresponda
    expected_cls = {1: HabitacionSimple, 2: HabitacionDoble, 3: Suite}.get(opc)
    if expected_cls is None:
        print("Opción inválida.")
        return

    if not isinstance(existente, expected_cls):
        print(f"Tipo inválido: la habitación {numero_habitacion} es {existente.tipo()} "
              f"y usted seleccionó {expected_cls.__name__}.")
        return

    # Reservar
    if isinstance(existente, HabitacionSimple):
        existente.set_estado("Reservado")
        print(f"Habitación {numero_habitacion} (Simple) reservada. Total: ${existente.get_precio()}")

    else:
        servicio, valor = servicios_adicionales()
        existente.set_precio(existente.get_precio() + valor)
        if servicio:
            existente.set_servicio(servicio, valor)
        existente.set_estado("Reservado")
        print(f"Habitación {numero_habitacion} ({existente.tipo()}) reservada. Total: ${existente.get_precio()}")

# ------------------------------------------------------

def precio_total():
    numero_habitacion = input("Ingrese el número de la habitación: ")

    if numero_habitacion not in habitaciones:
        print("La habitación ingresada no está reservada aún.")
        return

    h = habitaciones[numero_habitacion]
    print(f"\nHabitación {h.get_numero()} - Estado: {h.get_estado()}")
    print(f"Tipo: {h.tipo()}")
    print(f"Precio total: ${h.get_precio()}")

# ------------------------------------------------------

def recepcion():
    while True:
        print("\n=== Sistema de Reservas del Hotel ===")
        print("1) Ver habitaciones disponibles")
        print("2) Reservar habitación")
        print("3) Calcular precio total")
        print("4) Salir")
        opc = input("> ")

        if opc == "1":
            habitaciones_disponibles()
        elif opc == "2":
            reservar()
        elif opc == "3":
            precio_total()
        elif opc == "4":
            print("Gracias por usar el sistema. Hasta pronto.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# ------------------------------------------------------

# Inicializamos habitaciones disponibles
habitaciones["101"] = HabitacionSimple("101", 300000, "Disponible")
habitaciones["102"] = HabitacionDoble("102", 500000, "Disponible")
habitaciones["201"] = Suite("201", 800000, "Disponible")

recepcion()
