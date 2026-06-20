import tkinter as tk
from tkinter import messagebox
import hashlib

class LoginWindow:
    def __init__(self, on_login_success):
        self.on_login_success = on_login_success
        self.root = tk.Tk()
        self.root.title("Sistema de Parqueadero - Login")
        self.root.geometry("400x300")
        self.root.configure(bg='#2c3e50')
        
        # Usuarios predefinidos 
        self.users = {
            'admin': hashlib.md5('admin123'.encode()).hexdigest(),
            'operario': hashlib.md5('operario123'.encode()).hexdigest()
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#2c3e50', padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        title_label = tk.Label(
            main_frame, 
            text="SISTEMA DE PARQUEADERO", 
            font=('Arial', 16, 'bold'),
            fg='white',
            bg='#2c3e50'
        )
        title_label.pack(pady=20)
        
        # Frame de formulario
        form_frame = tk.Frame(main_frame, bg='#34495e', padx=20, pady=20)
        form_frame.pack(expand=True, fill='both')
        
        # Usuario
        tk.Label(
            form_frame, 
            text="Usuario:", 
            font=('Arial', 12),
            fg='white',
            bg='#34495e'
        ).grid(row=0, column=0, sticky='w', pady=10)
        
        self.username_entry = tk.Entry(form_frame, font=('Arial', 12), width=20)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.username_entry.bind('<Return>', lambda e: self.password_entry.focus())
        
        # Contraseña
        tk.Label(
            form_frame, 
            text="Contraseña:", 
            font=('Arial', 12),
            fg='white',
            bg='#34495e'
        ).grid(row=1, column=0, sticky='w', pady=10)
        
        self.password_entry = tk.Entry(form_frame, show='*', font=('Arial', 12), width=20)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        self.password_entry.bind('<Return>', lambda e: self.login())
        
        # Botón de login
        login_btn = tk.Button(
            form_frame,
            text="INGRESAR",
            font=('Arial', 12, 'bold'),
            bg='#27ae60',
            fg='white',
            width=15,
            command=self.login
        )
        login_btn.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Información de usuarios
        info_label = tk.Label(
            main_frame,
            text="Usuarios: admin/admin123 | operario/operario123",
            font=('Arial', 9),
            fg='#bdc3c7',
            bg='#2c3e50'
        )
        info_label.pack(pady=10)
        
        # Centrar la ventana
        self.center_window()
    
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def login(self):
        """Maneja el proceso de login"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor ingrese usuario y contraseña")
            return
        
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        
        if username in self.users and self.users[username] == hashed_password:
            messagebox.showinfo("Éxito", f"Bienvenido {username}!")
            self.root.destroy()
            self.on_login_success(username)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus()
    
    def run(self):
        """Inicia la aplicación"""
        self.root.mainloop()