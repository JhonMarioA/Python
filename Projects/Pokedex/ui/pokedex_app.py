from api.pockeapi_client import get_pokemon_data, extrac_info
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class PokedexApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokédex")

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.label_name = tk.Label(self.root, text="", font=("Arial", 16, "bold"))
        self.label_name.pack()

        self.label_image = tk.Label(self.root)
        self.label_image.pack(pady=10)

        self.label_info = tk.Label(self.root, text="", font=("Arial", 12))
        self.label_info.pack()

        btn_search = tk.Button(self.root, text="Buscar", relief="solid", cursor="cross", command=self.search_pokemon)
        btn_search.pack()

        self.root.mainloop()

    def search_pokemon(self):
        name = self.entry.get()
        try:
            data = extrac_info(get_pokemon_data(name))
            self.label_name.config(text=data["name"].capitalize())
            self.label_info.config(
                text=f"Type: {', '.join(data['types'])}\nAbilities: {', '.join(data['abilities'])}"
            )
            img_bytes = requests.get(data["image"]).content
            img = Image.open(BytesIO(img_bytes)).resize((200, 200))
            photo = ImageTk.PhotoImage(img)
            self.label_image.config(image=photo)
            self.label_image.image = photo
        except Exception as e:
            messagebox.showerror("Error", str(e))
