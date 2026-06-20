import json
import os
from datetime import date, timedelta
import tkinter as tk
from tkinter import messagebox


DATA_FILE = "streak_data.json"


def load_data():
    """Lee los datos desde el archivo JSON, o crea uno nuevo si no existe."""
    if not os.path.exists(DATA_FILE):
        data = {"last_date": str(date.today()), "streak": 1}
        save_data(data)
        return data
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    """Guarda los datos actualizados en el archivo JSON."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def update_streak():
    """Actualiza la racha según la última fecha registrada."""
    data = load_data()
    last_date = date.fromisoformat(data["last_date"])
    today = date.today()

    if today == last_date:
        message = "Ya contaste este día "
    elif today == last_date + timedelta(days=1):
      
        data["streak"] += 1
        data["last_date"] = str(today)
        save_data(data)
        message = "¡Racha incrementada!"
    else:
      
        data["streak"] = 1
        data["last_date"] = str(today)
        save_data(data)
        message = "Racha reiniciada"

    return data, message



# Interfaz gráfica (Tkinter)


def create_ui():
    """Crea la interfaz gráfica principal."""
    root = tk.Tk()
    root.title("Racha")
    root.geometry("300x200")
    root.resizable(False, False)

    # Colores y fuente
    root.config(bg="#121212")
    font_main = ("Helvetica", 14, "bold")
    font_small = ("Helvetica", 10)

    # Cargar datos al iniciar
    data = load_data()

    # Texto principal
    label_title = tk.Label(root, text="Tu racha actual:", bg="#121212", fg="white", font=font_small)
    label_title.pack(pady=10)

    label_streak = tk.Label(root, text=f"{data['streak']} 🔥", bg="#121212", fg="#00FF9C", font=("Helvetica", 30, "bold"))
    label_streak.pack(pady=10)

    # Botón para actualizar
    def on_update():
        new_data, msg = update_streak()
        label_streak.config(text=f"{new_data['streak']} 🔥")
        messagebox.showinfo("Estado", msg)

    btn_update = tk.Button(root, text="Actualizar racha", command=on_update, bg="#00FF9C", fg="black", font=font_main)
    btn_update.pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    create_ui()
