# model_ml/predictor.py

import joblib
import numpy as np
import pandas as pd

class ModelPredictor:

    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.columns = joblib.load("model_ml/columns.pkl")
        self.scaler = joblib.load("model_ml/scaler.pkl")
        self.cat_cols = joblib.load("model_ml/categorical_cols.pkl")
        self.label_encoder = joblib.load("model_ml/label_encoder.pkl")

    def predict_from_csv_row(self, csv_row):
        """
        csv_row: string con los valores separados por coma
        Ejemplo:
        "90,42,43,20.8,82,6.5,202.9,..."
        """

        # Convertir string → lista
        values = csv_row.split(",")
        values = [v.strip() for v in values]

        # Cargar la fila como dataframe UNA SOLA FILA
        # Nombres de columnas originales del CSV
        original_cols = [c for c in self.columns if not any(c.startswith(cc + "_") for cc in self.cat_cols)]

        if len(values) != len(original_cols):
            raise ValueError(f"Se esperaban {len(original_cols)} valores, pero recibí {len(values)}")

        temp_df = pd.DataFrame([values], columns=original_cols)

        # Convertir columnas numéricas
        for col in temp_df.columns:
            try:
                temp_df[col] = temp_df[col].astype(float)
            except:
                pass  

        # Aplicar get_dummies igual que en entrenamiento
        temp_df = pd.get_dummies(temp_df, columns=self.cat_cols, drop_first=True)

        # Alinear columnas con las del entrenamiento
        for col in self.columns:
            if col not in temp_df.columns:
                temp_df[col] = 0  # columna faltante

        # Reordenar
        temp_df = temp_df[self.columns]

        # Escalar
        X_scaled = self.scaler.transform(temp_df)

        # Predecir
        pred_encoded = self.model.predict(X_scaled)[0]

        # Decodificar label original
        pred_label = self.label_encoder.inverse_transform([pred_encoded])[0]

        return pred_label
