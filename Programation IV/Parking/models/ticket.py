from datetime import datetime
from models.vehicle import Vehicle

class Ticket:
    def __init__(self, vehicle, spot_number):
        self._ticket_id = f"TKT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self._vehicle = vehicle
        self._spot_number = spot_number
        self._entry_time = datetime.now()
        self._exit_time = None
        self._total_amount = 0
        self._is_paid = False
    
    # Encapsulamiento
    @property
    def ticket_id(self):
        return self._ticket_id
    
    @property
    def vehicle(self):
        return self._vehicle
    
    @property
    def spot_number(self):
        return self._spot_number
    
    @property
    def entry_time(self):
        return self._entry_time
    
    @property
    def exit_time(self):
        return self._exit_time
    
    @property
    def total_amount(self):
        return self._total_amount
    
    @property
    def is_paid(self):
        return self._is_paid
    
    def calculate_amount(self):
        """Calcula el monto total a pagar"""
        if self._exit_time is None:
            self._exit_time = datetime.now()
        
        time_parked = self._exit_time - self._entry_time
        hours = max(1, time_parked.total_seconds() / 3600)  # Mínimo 1 hora
        
        self._total_amount = self._vehicle.calculate_parking_fee(hours)
        return self._total_amount
    
    def mark_as_paid(self):
        """Marca el ticket como pagado"""
        self._is_paid = True
    
    def to_dict(self):
        """Convierte el ticket a diccionario para MongoDB"""
        return {
            'ticket_id': self._ticket_id,
            'vehicle': self._vehicle.to_dict(),
            'spot_number': self._spot_number,
            'entry_time': self._entry_time,
            'exit_time': self._exit_time,
            'total_amount': self._total_amount,
            'is_paid': self._is_paid
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un ticket desde un diccionario"""
        vehicle = Vehicle.from_dict(data['vehicle'])
        ticket = cls(vehicle, data['spot_number'])
        ticket._ticket_id = data['ticket_id']
        ticket._entry_time = data['entry_time']
        ticket._exit_time = data['exit_time']
        ticket._total_amount = data['total_amount']
        ticket._is_paid = data['is_paid']
        return ticket