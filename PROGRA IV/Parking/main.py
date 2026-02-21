#!/usr/bin/env python3
"""
Sistema de Gestión de Parqueadero
Programación IV - Proyecto Final
"""

import sys
import os

# Agregar el directorio raíz al path para imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.login import LoginWindow
from db.connection import DatabaseConnection

def main():
    """Función principal de la aplicación"""
    try:
        # Inicializar conexión a la base de datos
        db_connection = DatabaseConnection()
        
        # Función callback para cuando el login es exitoso
        def on_login_success(username):
            from gui.dashboard import Dashboard
            dashboard = Dashboard(username)
            dashboard.run()
        
        # Iniciar con la ventana de login
        login_window = LoginWindow(on_login_success)
        login_window.run()
        
    except Exception as e:
        print(f"Error iniciando la aplicación: {e}")
        input("Presione Enter para salir...")
    finally:
        # Cerrar conexión a la base de datos
        if 'db_connection' in locals():
            db_connection.close_connection()

if __name__ == "__main__":
    main()