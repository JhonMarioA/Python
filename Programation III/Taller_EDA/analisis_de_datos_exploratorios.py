# ==========================================
# Librerías
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración opcional para que los gráficos se vean mejor
sns.set(style="whitegrid")  # estilo de seaborn
plt.rcParams["figure.figsize"] = (10, 6)  # tamaño por defecto de las gráficas


# ==========================================
# 1. Entendiendo el dataset
# ==========================================
# 1.1 Cargando y mostrando información general del dataset:


# Cargando datos
ruta = "data/train.csv"
df = pd.read_csv(ruta)


# Información general
print(df.head())
print(df.info(), "\n")
print("Shape", df.shape, "\n") #Existen 891 pasajeros (filas) y existen 12 variables (columnas), float64(2) - int64(5) - object(5)


# 1.2 Estadísticas descriptivas:

# Resumen estadistico de variables númericas
print(df[["Age", "Fare"]].describe())

print(df["Survived"].value_counts())


# Preguntas:

print("\nEdad promedio: ", df["Age"].mean()) # 27 años
print("Tarifa más cara: ", df["Fare"].max()) # 512
print("Edad mediana: ", df["Age"].median()) # 28 años

rango_fare = df["Fare"].max() - df["Fare"].min()
print("Rango de tarifas: ", rango_fare) 

print("Desveciación estandar de edad: ", df["Age"].std())
print("Desviación estandar de precios de boletos: ", df["Fare"].std()) # La desviación estandar en los precios es mucho mayor, ya que los precios varían drasticamente

print("Edad mínima: ", df["Age"].min()) # 0.4 años
print("Edad máxima: ", df["Age"].max()) # 80 años

print("\n", df["Sex"].value_counts()) # Habían más hombres
print("\n", df["Embarked"].value_counts()) # Desde Q solo embarcarón 77 personas



# ==========================================
# 2. Combinando variables
# ==========================================
# Preguntas:

print("\n", df.groupby("Pclass")["Fare"].mean()) # La clase 3 paga menos más que la clase 1
print("\n", df.groupby("Sex")["Age"].mean()) # La diferencia en edades es poco significativa, solo 3 años
print("\n", df.groupby("Pclass")["Age"].mean()) # Efectivamente los pasajeros de la clase 1 son generalemnte mayores


# ==========================================
# 3. Detección de problemas y limpieza rápida
# ==========================================

# 3.1 Busqueda de valores nulos
print("\n", df.isnull().sum()) # Las columnas con valores nulos son "Age", "Cabin" y "Embarked", el mayor número de valores faltantes lo tiene "Cabin" con 687 valores faltantes

# 3.2 Identificación de duplicados
print("\n", df.duplicated().sum()) # No hay filas duplicadas en el conjunto de datos


# ==========================================
# 4. Visulización y relación entre variables, pensado para ser ejecutado en Google Colab
# ==========================================

# 4.1 Visualización de uan sola variable

# Histograma de Age
plt.hist(df["Age"].dropna(), bins=20, color="skyblue", edgecolor="black")
plt.title("Distribución de edades (Age)")
plt.xlabel("Edad")
plt.ylabel("Número de pasajeros")
plt.show()

# KDE de Age
sns.kdeplot(df["Age"].dropna(), fill=True, color="orange")
plt.title("Distribución de edades (KDE)")
plt.xlabel("Edad")
plt.ylabel("Densidad")
plt.show()

# Violin plot de Fare
sns.violinplot(y="Fare", data=df, color="lightgreen")
plt.title("Distribución de tarifas (Fare)")
plt.ylabel("Tarifa")
plt.show()

# Gráfico de barras de Sex
sns.countplot(x="Sex", data=df, palette="pastel")
plt.title("Distribución de género")
plt.xlabel("Género")
plt.ylabel("Número de pasajeros")
plt.show()


# 4.2 Relación entre supervivencía y otras variables 

# Gráfico de barras
sns.countplot(x="Sex", hue="Survived", data=df, palette="Set2")
plt.title("Supervivencia por género")
plt.xlabel("Género")
plt.ylabel("Número de pasajeros")
plt.legend(title="Supervivencia", labels=["No", "Sí"])
plt.show()

# Gráfico de barras
sns.countplot(x="Pclass", hue="Survived", data=df, palette="Set3")
plt.title("Supervivencia por clase")
plt.xlabel("Clase")
plt.ylabel("Número de pasajeros")
plt.legend(title="Supervivencia", labels=["No", "Sí"])
plt.show()

# Gráfico box plot
sns.boxplot(x="Survived", y="Age", data=df, palette="coolwarm")
plt.title("Edad vs Supervivencia")
plt.xlabel("Supervivencia (0=No, 1=Sí)")
plt.ylabel("Edad")
plt.show()