# Practical Machine Learning - EDA Diabetes - Jhon Mario Aguirre Correa

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
url = "diabetes.csv"
df = pd.read_csv(url)
print("Datos cargados correctamente")
print(df.head())

# Understanding Data
print("\n--- Información general ---")
print(df.info())
print("\n--- Estadísticos descriptivos ---")
print(df.describe())

# Detección de valores anómalos
cols_with_zero = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
print("\n--- Conteo de ceros en columnas ---")
print((df[cols_with_zero] == 0).sum())

# Reemplazar ceros por NaN
df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)
print("\nValores nulos después de reemplazar ceros:")
print(df.isnull().sum())

# Imputación de datos usando la mediana
df_imputed = df.fillna(df.median())

# Confirmar imputación
print("\nValores nulos luego de la imputación:")
print(df_imputed.isnull().sum())

# Visualización antes y después
fig, axes = plt.subplots(1, 2, figsize=(12,5))
sns.histplot(df['Glucose'], kde=True, ax=axes[0])
axes[0].set_title("Antes de imputación - Glucose")
sns.histplot(df_imputed['Glucose'], kde=True, ax=axes[1])
axes[1].set_title("Después de imputación - Glucose")
plt.show()

# Correlaciones
plt.figure(figsize=(10,6))
sns.heatmap(df_imputed.corr(), annot=True, cmap='coolwarm')
plt.title("Mapa de correlaciones (tras imputación)")
plt.show()

# Pairplot para relaciones entre variables principales
sns.pairplot(df_imputed, hue="Outcome")
plt.show()
