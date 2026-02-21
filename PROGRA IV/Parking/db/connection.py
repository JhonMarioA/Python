from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance
    
    def _initialize_connection(self):
        """Inicializa la conexión a MongoDB Atlas"""
        try:
            # Obtener cadena de conexión desde variables de entorno
            connection_string = os.getenv('MONGODB_URI')
            
            if not connection_string:
                raise ValueError("MONGODB_URI no encontrada en variables de entorno")
            
            self.client = MongoClient(connection_string)
            
            # Test the connection
            self.client.admin.command('ping')
            self.db = self.client['parking_system']
            
            print("Conexión a MongoDB Atlas establecida exitosamente")
            print(f"Base de datos: {self.db.name}")
            
        except Exception as e:
            print(f"Error conectando a MongoDB Atlas: {e}")
            raise e
    
    def get_collection(self, collection_name):
        """Retorna una colección de la base de datos"""
        return self.db[collection_name]
    
    def close_connection(self):
        """Cierra la conexión a MongoDB"""
        if self.client:
            self.client.close()
            print("Conexión a MongoDB cerrada")

def get_db_connection():
    return DatabaseConnection()