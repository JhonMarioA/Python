import tkinter as tk
from tkinter import ttk, messagebox
from factory.vehicle_factory import VehicleFactory

class EntryWindow:
    def __init__(self, parent_dashboard, parking_lot):
        self.parent_dashboard = parent_dashboard
        self.parking_lot = parking_lot
        
        self.window = tk.Toplevel(parent_dashboard.root)
        self.window.title("Entrada de Vehículo")
        self.window.geometry("500x450")
        self.window.configure(bg='#ecf0f1')
        self.window.resizable(False, False)
        self.window.transient(parent_dashboard.root)
        self.window.grab_set()
        
        self.setup_ui()
        self.center_window()
    
    def setup_ui(self):
        """Configura la interfaz de entrada"""
        # Frame principal
        main_frame = tk.Frame(self.window, bg='#ecf0f1', padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="REGISTRAR ENTRADA DE VEHÍCULO",
            font=('Arial', 14, 'bold'),
            fg='#2c3e50',
            bg='#ecf0f1'
        )
        title_label.pack(pady=(0, 20))
        
        # Formulario
        form_frame = tk.Frame(main_frame, bg='#ecf0f1')
        form_frame.pack(fill='both', expand=True)
        
        # Tipo de vehículo
        tk.Label(
            form_frame,
            text="Tipo de Vehículo:",
            font=('Arial', 11),
            bg='#ecf0f1'
        ).grid(row=0, column=0, sticky='w', pady=10, padx=(0, 10))
        
        self.vehicle_type = ttk.Combobox(
            form_frame,
            values=VehicleFactory.get_vehicle_types(),
            state='readonly',
            font=('Arial', 11),
            width=20
        )
        self.vehicle_type.grid(row=0, column=1, sticky='w', pady=10)
        self.vehicle_type.set('car')  # Valor por defecto
        self.vehicle_type.bind('<<ComboboxSelected>>', self.on_vehicle_type_change)
        
        # Placa
        tk.Label(
            form_frame,
            text="Placa:",
            font=('Arial', 11),
            bg='#ecf0f1'
        ).grid(row=1, column=0, sticky='w', pady=10, padx=(0, 10))
        
        self.license_plate = tk.Entry(
            form_frame,
            font=('Arial', 11),
            width=22
        )
        self.license_plate.grid(row=1, column=1, sticky='w', pady=10)
        
        # Marca
        tk.Label(
            form_frame,
            text="Marca:",
            font=('Arial', 11),
            bg='#ecf0f1'
        ).grid(row=2, column=0, sticky='w', pady=10, padx=(0, 10))
        
        self.brand = tk.Entry(
            form_frame,
            font=('Arial', 11),
            width=22
        )
        self.brand.grid(row=2, column=1, sticky='w', pady=10)
        
        # Color
        tk.Label(
            form_frame,
            text="Color:",
            font=('Arial', 11),
            bg='#ecf0f1'
        ).grid(row=3, column=0, sticky='w', pady=10, padx=(0, 10))
        
        self.color = tk.Entry(
            form_frame,
            font=('Arial', 11),
            width=22
        )
        self.color.grid(row=3, column=1, sticky='w', pady=10)
        
        # Espacio asignado (automático)
        tk.Label(
            form_frame,
            text="Espacio Asignado:",
            font=('Arial', 11),
            bg='#ecf0f1'
        ).grid(row=4, column=0, sticky='w', pady=10, padx=(0, 10))
        
        self.assigned_spot = tk.Label(
            form_frame,
            text="--",
            font=('Arial', 11, 'bold'),
            bg='#ecf0f1',
            fg='#e74c3c'
        )
        self.assigned_spot.grid(row=4, column=1, sticky='w', pady=10)
        
        # Información de tarifas
        info_frame = tk.LabelFrame(
            form_frame,
            text="Tarifas por Hora",
            font=('Arial', 10, 'bold'),
            bg='#ecf0f1',
            padx=10,
            pady=10
        )
        info_frame.grid(row=5, column=0, columnspan=2, sticky='we', pady=20)
        
        self.rates_label = tk.Label(
            info_frame,
            text="Carro: $2.000 | Moto: $1.000 | Camión: $4.000",
            font=('Arial', 10),
            bg='#ecf0f1'
        )
        self.rates_label.pack()
        
        # Botones
        button_frame = tk.Frame(form_frame, bg='#ecf0f1')
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        # Botón Buscar Espacio
        find_spot_btn = tk.Button(
            button_frame,
            text="BUSCAR ESPACIO",
            font=('Arial', 10, 'bold'),
            bg='#f39c12',
            fg='white',
            width=15,
            command=self.find_available_spot
        )
        find_spot_btn.pack(side='left', padx=5)
        
        # Botón Registrar
        register_btn = tk.Button(
            button_frame,
            text="REGISTRAR ENTRADA",
            font=('Arial', 10, 'bold'),
            bg='#27ae60',
            fg='white',
            width=15,
            command=self.register_entry
        )
        register_btn.pack(side='left', padx=5)
        
        # Botón Cancelar
        cancel_btn = tk.Button(
            button_frame,
            text="CANCELAR",
            font=('Arial', 10, 'bold'),
            bg='#95a5a6',
            fg='white',
            width=15,
            command=self.window.destroy
        )
        cancel_btn.pack(side='left', padx=5)
        
        # Actualizar información inicial
        self.on_vehicle_type_change()
    
    def on_vehicle_type_change(self, event=None):
        """Actualiza la información cuando cambia el tipo de vehículo"""
        vehicle_type = self.vehicle_type.get()
        rates_text = ""
        
        if vehicle_type == 'car':
            rates_text = "Carro: $2.000 por hora"
        elif vehicle_type == 'motorcycle':
            rates_text = "Moto: $1.000 por hora"
        elif vehicle_type == 'truck':
            rates_text = "Camión: $4.000 por hora"
        
        self.rates_label.config(text=rates_text)
    
    def find_available_spot(self):
        """Busca un espacio disponible"""
        if self.parking_lot.available_spots <= 0:
            messagebox.showerror("Error", "No hay espacios disponibles en el parqueadero")
            return
        
        spot = self.parking_lot.get_available_spot()
        if spot:
            self.assigned_spot.config(text=str(spot), fg='#27ae60')
            messagebox.showinfo("Espacio Encontrado", f"Espacio {spot} disponible")
        else:
            self.assigned_spot.config(text="--", fg='#e74c3c')
            messagebox.showerror("Error", "No se encontró espacio disponible")
    
    def register_entry(self):
        """Registra la entrada del vehículo"""
        # Validar campos
        if not all([self.license_plate.get(), self.brand.get(), self.color.get()]):
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return
        
        spot_text = self.assigned_spot.cget('text')
        if spot_text == '--':
            messagebox.showerror("Error", "Por favor busque un espacio disponible primero")
            return
        
        try:
            spot_number = int(spot_text)
            
            # Verificar si la placa ya está registrada
            if self.parking_lot.find_vehicle(self.license_plate.get().upper()):
                messagebox.showerror("Error", "Ya existe un vehículo con esta placa en el parqueadero")
                return
            
            # Crear vehículo usando el Factory
            vehicle = VehicleFactory.create_vehicle(
                self.vehicle_type.get(),
                self.license_plate.get().upper(),
                self.brand.get().title(),
                self.color.get().title()
            )
            
            # Registrar en el parqueadero
            ticket = self.parking_lot.park_vehicle(vehicle, spot_number)
            
            messagebox.showinfo(
                "Éxito", 
                f"Vehículo registrado exitosamente!\n"
                f"Ticket: {ticket.ticket_id}\n"
                f"Espacio: {spot_number}\n"
                f"Hora de entrada: {ticket.entry_time.strftime('%H:%M:%S')}"
            )
            
            # Limpiar formulario, actualizar dashboard y CERRAR VENTANA
            self.clear_form()
            self.parent_dashboard.refresh_dashboard()
            self.window.destroy()  # ← ESTA LÍNEA ES LA QUE FALTABA
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error al registrar: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")

            
    def clear_form(self):
        """Limpia el formulario"""
        self.license_plate.delete(0, tk.END)
        self.brand.delete(0, tk.END)
        self.color.delete(0, tk.END)
        self.assigned_spot.config(text="--", fg='#e74c3c')
        self.license_plate.focus()
    
    def center_window(self):
        """Centra la ventana"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')