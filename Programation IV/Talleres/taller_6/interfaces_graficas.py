
# 1) Tkinter
import tkinter as tk

#Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo con Tkinter")
root.geometry("300x200")

#Crear una etiqueta
label = tk.Label(root, text="Hola mundo desde Tkinter!!!", font=("Arial", 14))
label.pack(pady=20)

#Función que cambia el texto():

def cambiar_texto():
    label.config(text="Has presionado el botón!!!")


#Crear un botón 
button = tk.Button(root, text="Presionar", command=cambiar_texto)
button.pack(pady=10)

#Iniciar el b(ucle principal
root.mainloop()


# 2) PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

class VentanaEjemplo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo con PyQt5")
        self.setGeometry(100, 100, 300, 200)

        # Crear widgets
        self.label = QLabel("¡Hola desde PyQt5!", self)
        self.boton = QPushButton("Presionar", self)
        self.boton.clicked.connect(self.cambiar_texto)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.boton)
        self.setLayout(layout)

    def cambiar_texto(self):
        self.label.setText("¡Has presionado el botón!")

# Ejecutar la aplicación
app = QApplication(sys.argv)
ventana = VentanaEjemplo()
ventana.show()
sys.exit(app.exec_())
