import tkinter as tk
from tkinter import ttk, messagebox
from models.parking_lot import ParkingLot

class Dashboard:
    def __init__(self, username):
        self.username = username
        self.parking_lot = ParkingLot()
        self.parking_lot.load_parked_vehicles()
        
        self.root = tk.Tk()
        self.root.title(f"Sistema de Parqueadero - Bienvenido {username}")
        self.root.geometry("800x600")
        self.root.configure(bg='#ecf0f1')
        
        # Variables para las métricas (las hacemos dinámicas)
        self.total_label = None
        self.available_label = None
        self.occupied_label = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configura la interfaz del dashboard"""
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill='x', side='top')
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text=f"SISTEMA DE PARQUEADERO - Usuario: {self.username}",
            font=('Arial', 16, 'bold'),
            fg='white',
            bg='#2c3e50'
        ).pack(expand=True)
        
        # Contenedor principal
        main_container = tk.Frame(self.root, bg='#ecf0f1')
        main_container.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Panel de información
        info_frame = tk.LabelFrame(
            main_container,
            text="Información del Parqueadero",
            font=('Arial', 12, 'bold'),
            bg='#ecf0f1',
            padx=15,
            pady=15
        )
        info_frame.pack(fill='x', pady=(0, 20))
        
        # Métricas - LABELS DINÁMICOS
        metrics_frame = tk.Frame(info_frame, bg='#ecf0f1')
        metrics_frame.pack(fill='x')
        
        # Total espacios (fijo)
        tk.Label(
            metrics_frame,
            text="Total Espacios:",
            font=('Arial', 12, 'bold'),
            bg='#ecf0f1',
            fg='#2c3e50'
        ).pack(side='left', padx=(20, 5))
        
        self.total_label = tk.Label(
            metrics_frame,
            text=str(self.parking_lot.total_spots),
            font=('Arial', 12, 'bold'),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        self.total_label.pack(side='left', padx=(0, 20))
        
        # Espacios disponibles (dinámico)
        tk.Label(
            metrics_frame,
            text="Disponibles:",
            font=('Arial', 12, 'bold'),
            bg='#ecf0f1',
            fg='#27ae60'
        ).pack(side='left', padx=(20, 5))
        
        self.available_label = tk.Label(
            metrics_frame,
            text=str(self.parking_lot.available_spots),
            font=('Arial', 12, 'bold'),
            bg='#ecf0f1',
            fg='#27ae60'
        )
        self.available_label.pack(side='left', padx=(0, 20))
        
        # Espacios ocupados (dinámico)
        tk.Label(
            metrics_frame,
            text="Ocupados:",
            font=('Arial', 12, 'bold'),
            bg='#ecf0f1',
            fg='#e74c3c'
        ).pack(side='left', padx=(20, 5))
        
        self.occupied_label = tk.Label(
            metrics_frame,
            text=str(self.parking_lot.total_spots - self.parking_lot.available_spots),
            font=('Arial', 12, 'bold'),
            bg='#ecf0f1',
            fg='#e74c3c'
        )
        self.occupied_label.pack(side='left', padx=(0, 20))
        
        # Botón de actualizar
        refresh_btn = tk.Button(
            metrics_frame,
            text="🔄",
            font=('Arial', 10),
            bg='#3498db',
            fg='white',
            width=3,
            command=self.refresh_dashboard
        )
        refresh_btn.pack(side='right', padx=10)
        
        # Botones de acción
        actions_frame = tk.Frame(main_container, bg='#ecf0f1')
        actions_frame.pack(fill='x', pady=10)
        
        # Botón Entrada
        entry_btn = tk.Button(
            actions_frame,
            text="ENTRADA DE VEHÍCULO",
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            width=20,
            height=2,
            command=self.open_entry_window
        )
        entry_btn.pack(side='left', padx=10)
        
        # Botón Salida
        exit_btn = tk.Button(
            actions_frame,
            text="SALIDA DE VEHÍCULO",
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            width=20,
            height=2,
            command=self.open_exit_window
        )
        exit_btn.pack(side='left', padx=10)
        
        # Botón ver vehículos
        view_btn = tk.Button(
            actions_frame,
            text="ACTUALIZAR LISTA",
            font=('Arial', 12, 'bold'),
            bg='#f39c12',
            fg='white',
            width=20,
            height=2,
            command=self.refresh_dashboard
        )
        view_btn.pack(side='left', padx=10)
        
        # Lista de vehículos estacionados
        self.setup_vehicle_list(main_container)
        
        # Centrar ventana
        self.center_window()
    
    def setup_vehicle_list(self, parent):
        """Configura la lista de vehículos estacionados"""
        list_frame = tk.LabelFrame(
            parent,
            text="Vehículos Estacionados",
            font=('Arial', 12, 'bold'),
            bg='#ecf0f1',
            padx=15,
            pady=15
        )
        list_frame.pack(expand=True, fill='both', pady=(10, 0))
        
        # Treeview para mostrar vehículos
        columns = ('Placa', 'Tipo', 'Marca', 'Color', 'Espacio', 'Hora Entrada')
        self.vehicle_tree = ttk.Treeview(
            list_frame, 
            columns=columns, 
            show='headings',
            height=12
        )
        
        # Configurar columnas
        for col in columns:
            self.vehicle_tree.heading(col, text=col)
            self.vehicle_tree.column(col, width=120)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.vehicle_tree.yview)
        self.vehicle_tree.configure(yscrollcommand=scrollbar.set)
        
        self.vehicle_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Actualizar lista
        self.update_vehicle_list()
    
    def update_vehicle_list(self):
        """Actualiza la lista de vehículos estacionados"""
        # Limpiar treeview
        for item in self.vehicle_tree.get_children():
            self.vehicle_tree.delete(item)
        
        # Agregar vehículos
        for spot_number, ticket in self.parking_lot.occupied_spots.items():
            vehicle = ticket.vehicle
            entry_time = ticket.entry_time.strftime('%H:%M:%S') if ticket.entry_time else 'N/A'
            
            self.vehicle_tree.insert('', 'end', values=(
                vehicle.license_plate,
                vehicle.vehicle_type.upper(),
                vehicle.brand,
                vehicle.color,
                spot_number,
                entry_time
            ))
    
    def open_entry_window(self):
        """Abre la ventana de entrada de vehículos"""
        from gui.entry import EntryWindow
        entry_window = EntryWindow(self, self.parking_lot)
        # Esperar a que la ventana se cierre para actualizar
        self.root.wait_window(entry_window.window)
        self.refresh_dashboard()
    
    def open_exit_window(self):
        """Abre la ventana de salida de vehículos"""
        from gui.exit import ExitWindow
        exit_window = ExitWindow(self, self.parking_lot)
        # Esperar a que la ventana se cierre para actualizar
        self.root.wait_window(exit_window.window)
        self.refresh_dashboard()
    
    def show_parked_vehicles(self):
        """Muestra los vehículos estacionados"""
        self.refresh_dashboard()
        messagebox.showinfo("Información", "Lista de vehículos actualizada")
    
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def refresh_dashboard(self):
        """Actualiza TODA la información del dashboard"""
        print("\n" + "="*50)
        print(" INICIANDO ACTUALIZACIÓN DEL DASHBOARD")
        print("="*50)
        
        print(f" Estado ANTES de actualizar:")
        print(f"   - Vehículos en memoria: {len(self.parking_lot.occupied_spots)}")
        print(f"   - Espacios disponibles: {self.parking_lot.available_spots}")
        
        # Recargar datos desde la base de datos
        self.parking_lot.load_parked_vehicles()
        
        print(f"📊 Estado DESPUÉS de actualizar:")
        print(f"   - Vehículos en memoria: {len(self.parking_lot.occupied_spots)}")
        print(f"   - Espacios disponibles: {self.parking_lot.available_spots}")
        
        # Actualizar métricas
        self.update_metrics()
        
        # Actualizar lista de vehículos
        self.update_vehicle_list()
        
        print(" DASHBOARD ACTUALIZADO CORRECTAMENTE")
        print("="*50 + "\n")
    
    def update_metrics(self):
        """Actualiza las métricas en tiempo real"""
        if self.available_label and self.occupied_label:
            available = self.parking_lot.available_spots
            occupied = self.parking_lot.total_spots - available
            
            self.available_label.config(text=str(available))
            self.occupied_label.config(text=str(occupied))
            
            # Cambiar color según disponibilidad
            if available <= 5:
                self.available_label.config(fg='#e74c3c')  # Rojo si hay pocos espacios
            else:
                self.available_label.config(fg='#27ae60')  # Verde si hay suficientes
    
    def run(self):
        """Inicia el dashboard"""
        self.root.mainloop()