from models.vehicle import Car, Motorcycle, Truck

class VehicleFactory:
    """Patrón Factory para crear vehículos"""
    
    @staticmethod
    def create_vehicle(vehicle_type, license_plate, brand, color):
        """
        Crea un vehículo basado en el tipo
        
        Args:
            vehicle_type (str): 'car', 'motorcycle', o 'truck'
            license_plate (str): Placa del vehículo
            brand (str): Marca del vehículo
            color (str): Color del vehículo
            
        Returns:
            Vehicle: Instancia del vehículo correspondiente
        """
        vehicle_type = vehicle_type.lower()
        
        if vehicle_type == 'car':
            return Car(license_plate, brand, color)
        elif vehicle_type == 'motorcycle':
            return Motorcycle(license_plate, brand, color)
        elif vehicle_type == 'truck':
            return Truck(license_plate, brand, color)
        else:
            raise ValueError(f"Tipo de vehículo no válido: {vehicle_type}")
    
    @staticmethod
    def get_vehicle_types():
        """Retorna los tipos de vehículos disponibles"""
        return ['car', 'motorcycle', 'truck']