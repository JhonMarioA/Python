import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class ExitWindow:
    def __init__(self, parent_dashboard, parking_lot):
        self.parent_dashboard = parent_dashboard
        self.parking_lot = parking_lot
        self.current_ticket = None
        
        self.window = tk.Toplevel(parent_dashboard.root)
        self.window.title("Salida de Vehículo")
        self.window.geometry("650x650")
        self.window.configure(bg='#ecf0f1')
        self.window.resizable(False, False)
        self.window.transient(parent_dashboard.root)
        self.window.grab_set()
        
        self.setup_ui()
        self.center_window()
    
    def setup_ui(self):
        """Configura la interfaz de salida"""
        # Frame principal
        main_frame = tk.Frame(self.window, bg='#ecf0f1', padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="REGISTRAR SALIDA DE VEHÍCULO",
            font=('Arial', 14, 'bold'),
            fg='#2c3e50',
            bg='#ecf0f1'
        )
        title_label.pack(pady=(0, 20))
        
        # Búsqueda por placa
        search_frame = tk.Frame(main_frame, bg='#ecf0f1')
        search_frame.pack(fill='x', pady=10)
        
        tk.Label(
            search_frame,
            text="Buscar por Placa:",
            font=('Arial', 11),
            bg='#ecf0f1'
        ).pack(side='left', padx=(0, 10))
        
        self.search_entry = tk.Entry(
            search_frame,
            font=('Arial', 11),
            width=15
        )
        self.search_entry.pack(side='left', padx=(0, 10))
        self.search_entry.bind('<Return>', lambda e: self.search_vehicle())
        
        search_btn = tk.Button(
            search_frame,
            text="BUSCAR",
            font=('Arial', 10, 'bold'),
            bg='#3498db',
            fg='white',
            command=self.search_vehicle
        )
        search_btn.pack(side='left')
        
        # Información del vehículo
        info_frame = tk.LabelFrame(
            main_frame,
            text="Información del Vehículo",
            font=('Arial', 11, 'bold'),
            bg='#ecf0f1',
            padx=15,
            pady=15
        )
        info_frame.pack(fill='x', pady=10)
        
        # Campos de información
        info_grid = tk.Frame(info_frame, bg='#ecf0f1')
        info_grid.pack(fill='x')
        
        labels = ['Placa:', 'Tipo:', 'Marca:', 'Color:', 'Espacio:', 'Hora Entrada:']
        self.info_labels = {}
        
        for i, label_text in enumerate(labels):
            # Etiqueta
            tk.Label(
                info_grid,
                text=label_text,
                font=('Arial', 10, 'bold'),
                bg='#ecf0f1',
                width=12,
                anchor='w'
            ).grid(row=i, column=0, sticky='w', pady=5)
            
            # Valor
            value_label = tk.Label(
                info_grid,
                text="--",
                font=('Arial', 10),
                bg='#ecf0f1',
                fg='#2c3e50'
            )
            value_label.grid(row=i, column=1, sticky='w', pady=5)
            self.info_labels[label_text[:-1].lower().replace(' ', '_')] = value_label
        
        # Información de pago
        payment_frame = tk.LabelFrame(
            main_frame,
            text="Información de Pago",
            font=('Arial', 11, 'bold'),
            bg='#ecf0f1',
            padx=15,
            pady=15
        )
        payment_frame.pack(fill='x', pady=10)
        
        payment_grid = tk.Frame(payment_frame, bg='#ecf0f1')
        payment_grid.pack(fill='x')
        
        payment_labels = ['Tiempo Estacionado:', 'Tarifa por Hora:', 'Total a Pagar:']
        self.payment_labels = {}
        
        for i, label_text in enumerate(payment_labels):
            # Etiqueta
            tk.Label(
                payment_grid,
                text=label_text,
                font=('Arial', 10, 'bold'),
                bg='#ecf0f1',
                width=15,
                anchor='w'
            ).grid(row=i, column=0, sticky='w', pady=5)
            
            # Valor
            value_label = tk.Label(
                payment_grid,
                text="--",
                font=('Arial', 10),
                bg='#ecf0f1',
                fg='#e74c3c'
            )
            value_label.grid(row=i, column=1, sticky='w', pady=5)
            self.payment_labels[label_text[:-1].lower().replace(' ', '_')] = value_label
        
        # Botones
        button_frame = tk.Frame(main_frame, bg='#ecf0f1')
        button_frame.pack(pady=20)
        
        # Botón Calcular
        calculate_btn = tk.Button(
            button_frame,
            text="CALCULAR PAGO",
            font=('Arial', 10, 'bold'),
            bg='#f39c12',
            fg='white',
            width=15,
            command=self.calculate_payment
        )
        calculate_btn.pack(side='left', padx=5)
        
        # Botón Registrar Salida
        register_btn = tk.Button(
            button_frame,
            text="REGISTRAR SALIDA",
            font=('Arial', 10, 'bold'),
            bg='#27ae60',
            fg='white',
            width=15,
            command=self.register_exit
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
    
    def search_vehicle(self):
        """Busca un vehículo por placa"""
        license_plate = self.search_entry.get().strip().upper()
        
        if not license_plate:
            messagebox.showerror("Error", "Por favor ingrese una placa")
            return
        
        ticket = self.parking_lot.find_vehicle(license_plate)
        
        if not ticket:
            messagebox.showerror("Error", "Vehículo no encontrado en el parqueadero")
            self.clear_info()
            return
        
        self.current_ticket = ticket
        self.display_vehicle_info(ticket)
    
    def display_vehicle_info(self, ticket):
        """Muestra la información del vehículo"""
        vehicle = ticket.vehicle
        
        # Información del vehículo
        self.info_labels['placa'].config(text=vehicle.license_plate)
        self.info_labels['tipo'].config(text=vehicle.vehicle_type.upper())
        self.info_labels['marca'].config(text=vehicle.brand)
        self.info_labels['color'].config(text=vehicle.color)
        self.info_labels['espacio'].config(text=ticket.spot_number)
        self.info_labels['hora_entrada'].config(
            text=ticket.entry_time.strftime('%H:%M:%S') if ticket.entry_time else 'N/A'
        )
    
    def calculate_payment(self):
        """Calcula el pago del estacionamiento"""
        if not self.current_ticket:
            messagebox.showerror("Error", "Primero busque un vehículo")
            return
        
        try:
            # Calcular tiempo y monto
            ticket = self.current_ticket
            ticket.calculate_amount()
            
            # Mostrar información de pago
            time_parked = ticket.exit_time - ticket.entry_time
            hours = max(1, time_parked.total_seconds() / 3600)
            
            # Determinar tarifa por hora
            vehicle_type = ticket.vehicle.vehicle_type
            if vehicle_type == 'car':
                rate_per_hour = 2000
            elif vehicle_type == 'motorcycle':
                rate_per_hour = 1000
            else:  # truck
                rate_per_hour = 4000
            
            self.payment_labels['tiempo_estacionado'].config(
                text=f"{hours:.1f} horas"
            )
            self.payment_labels['tarifa_por_hora'].config(
                text=f"${rate_per_hour:,}"
            )
            self.payment_labels['total_a_pagar'].config(
                text=f"${ticket.total_amount:,}",
                fg='#e74c3c',
                font=('Arial', 10, 'bold')
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular pago: {str(e)}")
    
    def register_exit(self):
        """Registra la salida del vehículo"""
        if not self.current_ticket:
            messagebox.showerror("Error", "Primero busque y calcule el pago de un vehículo")
            return
        
        try:
            # Registrar salida
            ticket = self.parking_lot.unpark_vehicle(
                self.current_ticket.vehicle.license_plate
            )
            
            messagebox.showinfo(
                "Éxito",
                f"Salida registrada exitosamente!\n"
                f"Vehículo: {ticket.vehicle.license_plate}\n"
                f"Total pagado: ${ticket.total_amount:,}\n"
                f"Hora de salida: {ticket.exit_time.strftime('%H:%M:%S')}"
            )
            
            # Limpiar y actualizar
            self.clear_info()
            self.search_entry.delete(0, tk.END)
            
            # ACTUALIZAR DASHBOARD Y CERRAR VENTANA
            self.parent_dashboard.refresh_dashboard()
            self.window.destroy()  
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar salida: {str(e)}")


    def clear_info(self):
        """Limpia la información mostrada"""
        for label in self.info_labels.values():
            label.config(text="--")
        
        for label in self.payment_labels.values():
            label.config(text="--", fg='#e74c3c', font=('Arial', 10))
        
        self.current_ticket = None
    
    def center_window(self):
        """Centra la ventana"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')