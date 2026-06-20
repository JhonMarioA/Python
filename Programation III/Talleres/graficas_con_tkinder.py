import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tabla de personas")

# Crear tabla
tabla = ttk.Treeview(root, columns=("Estatura", "Peso"), show="headings")
tabla.heading("Estatura", text="Estatura (m)")
tabla.heading("Peso", text="Peso (kg)")

# Agregar datos
datos = [("Juan", 1.75, 70), ("Ana", 1.65, 60), ("Pedro", 1.80, 85)]
for nombre, estatura, peso in datos:
    tabla.insert("", "end", values=(estatura, peso))

tabla.pack()
root.mainloop()
