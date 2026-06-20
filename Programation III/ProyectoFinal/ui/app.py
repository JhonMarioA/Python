# ui/app.py
import tkinter as tk
from model_ml.predictor import ModelPredictor

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Farming Classifier")

        # Cargar modelo Random Forest 
        self.predictor = ModelPredictor("model_ml/model_rf.pkl")

        tk.Label(root, text="Ingrese valores separados por coma:").pack()

        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        tk.Button(root, text="Predecir", command=self.make_prediction).pack()

        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack()

    def make_prediction(self):
        raw = self.entry.get()
        try:
            values = list(map(float, raw.split(",")))
            pred = self.predictor.predict_from_csv_row(raw)
            self.result_label.config(text=f"Predicción: {pred}")
        except Exception as e:
            self.result_label.config(text=f"Error: {e}", fg="red")
