

# 2) Sistema de gestión de reservas de habitaciones en un hotel

class Habitacion:
    def __init__(self, numero, precio, estado):
        self.__numero = numero
        self.__precio = precio
        self.__estado = estado

    def get_numero(self):
        return self.__numero
    
    def get_precio(self):
        return self.__precio
    
    def get_estado(self):
        return self.__estado
    

class HabitacionSimple(Habitacion):
    pass

class HabitacionDoble(Habitacion):
    def __init___(self, servicio):
        super().__init__(self)
        self.__servicio = servicio

    def get_servicio(self):
        return self.__servicio


class Suite(Habitacion):
    def __init__(self, servicio):
        super().__init__(self)
        self.__servicio = servicio

    def get_servicio(self):
        return self.__servicio

#__________________________________________________


def habitaciones_disponibles():
    print("Bienvenido al servicio de reservas del hotel!!!\n")
    # funcion para mostrar habitacioens disponibles

def reservar():
    print("Opciones: ")
    print("1) Reservar habitación simple.\n2) Reservar habitación doble. 3\n) Reservar suite.")

def precio_total():
    pass

def recepción():
    pass

