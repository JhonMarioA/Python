from abc import ABC, abstractmethod
from datetime import datetime

class Vehicle(ABC):
    def __init__(self, license_plate, vehicle_type, brand, color):
        self._license_plate = license_plate
        self._vehicle_type = vehicle_type
        self._brand = brand
        self._color = color
        self._entry_time = None
        self._is_parked = False
    
    # Encapsulamiento: usando propiedades para controlar el acceso
    @property
    def license_plate(self):
        return self._license_plate
    
    @property
    def vehicle_type(self):
        return self._vehicle_type
    
    @property
    def brand(self):
        return self._brand
    
    @property
    def color(self):
        return self._color
    
    @property
    def entry_time(self):
        return self._entry_time
    
    @property
    def is_parked(self):
        return self._is_parked
    
    def park(self):
        """Marca el vehículo como estacionado"""
        self._is_parked = True
        self._entry_time = datetime.now()
    
    def unpark(self):
        """Marca el vehículo como no estacionado"""
        self._is_parked = False
        self._entry_time = None
    
    @abstractmethod
    def calculate_parking_fee(self, hours):
        """Calcula la tarifa de estacionamiento (método abstracto)"""
        pass
    
    def to_dict(self):
        """Convierte el vehículo a diccionario para MongoDB"""
        return {
            'license_plate': self._license_plate,
            'vehicle_type': self._vehicle_type,
            'brand': self._brand,
            'color': self._color,
            'entry_time': self._entry_time,
            'is_parked': self._is_parked
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un vehículo desde un diccionario"""
        vehicle_type = data['vehicle_type']
        if vehicle_type == 'car':
            return Car(data['license_plate'], data['brand'], data['color'])
        elif vehicle_type == 'motorcycle':
            return Motorcycle(data['license_plate'], data['brand'], data['color'])
        elif vehicle_type == 'truck':
            return Truck(data['license_plate'], data['brand'], data['color'])
        else:
            raise ValueError(f"Tipo de vehículo desconocido: {vehicle_type}")

# Herencia: diferentes tipos de vehículos
class Car(Vehicle):
    def __init__(self, license_plate, brand, color):
        super().__init__(license_plate, 'car', brand, color)
    
    # Polimorfismo: implementación específica del método abstracto
    def calculate_parking_fee(self, hours):
        base_rate = 2000  # $2.000 por hora para carros
        return base_rate * hours

class Motorcycle(Vehicle):
    def __init__(self, license_plate, brand, color):
        super().__init__(license_plate, 'motorcycle', brand, color)
    
    # Polimorfismo: implementación específica del método abstracto
    def calculate_parking_fee(self, hours):
        base_rate = 1000  # $1.000 por hora para motos
        return base_rate * hours

class Truck(Vehicle):
    def __init__(self, license_plate, brand, color):
        super().__init__(license_plate, 'truck', brand, color)
    
    # Polimorfismo: implementación específica del método abstracto
    def calculate_parking_fee(self, hours):
        base_rate = 4000  # $4.000 por hora para camiones
        return base_rate * hours