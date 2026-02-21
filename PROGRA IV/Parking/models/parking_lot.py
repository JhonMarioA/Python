from db.connection import get_db_connection
from models.ticket import Ticket

class ParkingLot:
    def __init__(self, total_spots=50):
        self._total_spots = total_spots
        self._available_spots = total_spots
        self._occupied_spots = {}
        self._db = get_db_connection()
        self._tickets_collection = self._db.get_collection('tickets')
    
    @property
    def total_spots(self):
        return self._total_spots
    
    @property
    def available_spots(self):
        return self._available_spots
    
    @property
    def occupied_spots(self):
        return self._occupied_spots
    
    def park_vehicle(self, vehicle, spot_number):
        """Estaciona un vehículo en un espacio específico"""
        if spot_number < 1 or spot_number > self._total_spots:
            raise ValueError("Número de espacio inválido")
        
        if spot_number in self._occupied_spots:
            raise ValueError("El espacio ya está ocupado")
        
        if self._available_spots <= 0:
            raise ValueError("No hay espacios disponibles")
        
        # Crear ticket y guardar en MongoDB
        ticket = Ticket(vehicle, spot_number)
        vehicle.park()
        
        self._occupied_spots[spot_number] = ticket
        self._available_spots -= 1
        
        # Guardar en base de datos
        self._tickets_collection.insert_one(ticket.to_dict())
        
        return ticket
    
    def unpark_vehicle(self, license_plate):
        """Retira un vehículo del parqueadero"""
        ticket = None
        spot_number = None
        
        # Buscar el ticket por placa
        for spot, tkt in self._occupied_spots.items():
            if tkt.vehicle.license_plate == license_plate:
                ticket = tkt
                spot_number = spot
                break
        
        if ticket is None:
            raise ValueError("Vehículo no encontrado en el parqueadero")
        
        # Calcular monto y actualizar ticket
        ticket.calculate_amount()
        ticket.mark_as_paid()
        ticket.vehicle.unpark()
        
        # Liberar espacio
        del self._occupied_spots[spot_number]
        self._available_spots += 1
        
        # Actualizar en base de datos
        self._tickets_collection.update_one(
            {'ticket_id': ticket.ticket_id},
            {'$set': {
                'exit_time': ticket.exit_time,
                'total_amount': ticket.total_amount,
                'is_paid': ticket.is_paid,
                'vehicle.is_parked': False,
                'vehicle.entry_time': None
            }}
        )
        
        return ticket
    
    def find_vehicle(self, license_plate):
        """Busca un vehículo por placa"""
        for ticket in self._occupied_spots.values():
            if ticket.vehicle.license_plate == license_plate:
                return ticket
        return None
    
    def get_available_spot(self):
        """Encuentra el primer espacio disponible"""
        for spot in range(1, self._total_spots + 1):
            if spot not in self._occupied_spots:
                return spot
        return None
    
    def load_parked_vehicles(self):
        """Carga vehículos estacionados desde la base de datos"""
        print(" Cargando vehículos desde MongoDB...")
        
        # LIMPIAR EL ESTADO ACTUAL ANTES DE CARGAR
        self._occupied_spots = {}
        self._available_spots = self._total_spots
        
        # Buscar tickets activos en MongoDB
        parked_tickets = self._tickets_collection.find({
            'is_paid': False,
            'exit_time': None
        })
        
        loaded_count = 0
        for ticket_data in parked_tickets:
            try:
                ticket = Ticket.from_dict(ticket_data)
                spot_number = ticket.spot_number
                
                # Solo agregar si el espacio no está ya ocupado
                if spot_number not in self._occupied_spots:
                    self._occupied_spots[spot_number] = ticket
                    self._available_spots -= 1
                    loaded_count += 1
                    print(f"    Cargado: {ticket.vehicle.license_plate} en espacio {spot_number}")
                else:
                    print(f"     Espacio {spot_number} duplicado en BD")
                    
            except Exception as e:
                print(f"    Error cargando ticket: {e}")
    
        print(f" Carga completada: {loaded_count} vehículos, {self._available_spots} espacios disponibles")