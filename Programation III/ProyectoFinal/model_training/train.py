# ---------------------------
# IMPLEMENTACIÓN COMPLETA
# Smart Farming - RandomForest vs SVM (multiclase)
# ---------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    accuracy_score, f1_score, cohen_kappa_score,
    roc_curve, auc, roc_auc_score, classification_report, confusion_matrix
)
from sklearn.preprocessing import label_binarize

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import joblib
import os

# ---------------------------
# 1) Cargar datos
# ---------------------------
df = pd.read_csv("smart_farming_data.csv")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

# ---------------------------
# 2) Objetivo y características
# ---------------------------
# El objetivo es la columna 'label'
target_col = "label"
if target_col not in df.columns:
    raise ValueError(f"No se encontró la columna objetivo '{target_col}' en el dataset.")

# Opcional: eliminar filas con NaN 
df = df.dropna().reset_index(drop=True)
print("Shape after dropna:", df.shape)

# Separar X e y
y = df[target_col]
X = df.drop(columns=[target_col])

# ---------------------------
# 3) Detectar y codificar variables categóricas
# ---------------------------
cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()
print("Categorical columns:", cat_cols)

if len(cat_cols) > 0:
    # One-hot encoding 
    X = pd.get_dummies(X, columns=cat_cols, drop_first=True)
    print("New shape after get_dummies:", X.shape)

# ---------------------------
# 4) Escalado de features numéricos
# ---------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------------------------
# 5) Codificar label (target)
# ---------------------------
le = LabelEncoder()
y_encoded = le.fit_transform(y)
classes = le.classes_
print("Classes:", classes)

# ---------------------------
# 6) División entreno/test 
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)
print("Train shape:", X_train.shape, "Test shape:", X_test.shape)

# ---------------------------
# 7) Setup de Cross-Validation
# ---------------------------
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# ---------------------------
# 8) GridSearch para RandomForest
# ---------------------------
rf_param_grid = {
    "n_estimators": [100, 200],        
    "max_depth": [None, 15],           # None o profundidad limitada
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2],
    "max_features": ["sqrt"]
}

rf = RandomForestClassifier(random_state=42)

print("\n--- Buscando hiperparámetros RandomForest ---")
t0 = time.time()
grid_rf = GridSearchCV(
    rf, rf_param_grid, cv=cv, scoring="f1_macro", n_jobs=-1, verbose=1
)
grid_rf.fit(X_train, y_train)
t1 = time.time()
print("RF GridSearch tiempo (s):", round(t1 - t0, 1))
print("Mejores RF params:", grid_rf.best_params_)

best_rf = grid_rf.best_estimator_

# ---------------------------
# 9) GridSearch para SVM 
# ---------------------------

svm_param_grid = {
    "C": [0.1, 1],         
    "gamma": ["scale", 0.01],
    "kernel": ["rbf"]       # rbf es representativo; poly suele ser mucho más costoso
}

svm = SVC(probability=True, random_state=42)

print("\n--- Buscando hiperparámetros SVM ---")
t0 = time.time()
grid_svm = GridSearchCV(
    svm, svm_param_grid, cv=cv, scoring="f1_macro", n_jobs=-1, verbose=1
)
grid_svm.fit(X_train, y_train)
t1 = time.time()
print("SVM GridSearch tiempo (s):", round(t1 - t0, 1))
print("Mejores SVM params:", grid_svm.best_params_)

best_svm = grid_svm.best_estimator_

# ---------------------------
# 10) Evaluación en Test 
# ---------------------------
models = {
    "RandomForest": best_rf,
    "SVM": best_svm
}

results = {}

for name, model in models.items():
    print(f"\n--- Evaluando {name} ---")
    y_pred = model.predict(X_test)

    if hasattr(model, "predict_proba"):
        y_proba = model.predict_proba(X_test)
    else:
        # fallback a decision_function (SVM con probability=False) 
        try:
            df_scores = model.decision_function(X_test)
            # para multiclass decision_function shape = (n_samples, n_classes)
            # convertir a probabilidades con softmax 
            exp_scores = np.exp(df_scores)
            y_proba = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        except Exception as e:
            raise RuntimeError("No hay método para obtener scores probabilísticos.") from e

    acc = accuracy_score(y_test, y_pred)
    f1m = f1_score(y_test, y_pred, average="macro")
    kappa = cohen_kappa_score(y_test, y_pred)

    # Binarizar y_test para AUC multiclas
    y_test_bin = label_binarize(y_test, classes=np.arange(len(classes)))
    # y_proba shape debe ser (n_samples, n_classes)
    if y_proba.shape[1] != y_test_bin.shape[1]:
        raise ValueError("Número de columnas en y_proba y y_test_bin no coincide.")

    # AUC por clase + micro + macro (One-vs-Rest)
    auc_per_class = dict()
    fpr = dict()
    tpr = dict()
    for i in range(len(classes)):
        fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, i], y_proba[:, i])
        auc_per_class[i] = auc(fpr[i], tpr[i])

    auc_micro = roc_auc_score(y_test_bin, y_proba, average="micro", multi_class="ovr")
    auc_macro = roc_auc_score(y_test_bin, y_proba, average="macro", multi_class="ovr")

    results[name] = {
        "accuracy": acc,
        "f1_macro": f1m,
        "kappa": kappa,
        "auc_macro": auc_macro,
        "auc_micro": auc_micro,
        "auc_per_class": auc_per_class,
        "fpr": fpr,
        "tpr": tpr
    }

    print("Accuracy:", round(acc,4))
    print("F1 (macro):", round(f1m,4))
    print("Kappa:", round(kappa,4))
    print("AUC macro:", round(auc_macro,4))
    print("AUC micro:", round(auc_micro,4))
    print("Classification report:\n", classification_report(y_test, y_pred, target_names=classes))

# ---------------------------
# 11) Comparación y tabla resumen
# ---------------------------
summary = []
for name, info in results.items():
    summary.append({
        "model": name,
        "accuracy": info["accuracy"],
        "f1_macro": info["f1_macro"],
        "kappa": info["kappa"],
        "auc_macro": info["auc_macro"],
        "auc_micro": info["auc_micro"]
    })
summary_df = pd.DataFrame(summary).sort_values(by="f1_macro", ascending=False).reset_index(drop=True)
print(summary_df)

# ---------------------------
# 12) Graficar curvas ROC multiclase (por modelo)
# ---------------------------
for name, info in results.items():
    plt.figure(figsize=(9,6))
    for i in range(len(classes)):
        plt.plot(info["fpr"][i], info["tpr"][i],
                 label=f"Clase {classes[i]} (AUC={info['auc_per_class'][i]:.2f})")
    # micro-average ROC curve 
    plt.plot([0,1],[0,1],"--", color="gray")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"ROC Multiclase - {name} (macro AUC={info['auc_macro']:.3f}, micro AUC={info['auc_micro']:.3f})")
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
    plt.grid()
    plt.tight_layout()
    plt.show()

# ---------------------------
# 13) Selección del mejor modelo
# ---------------------------
# Criterio: f1_macro (principal), luego auc_macro y accuracy
best_model_name = summary_df.loc[0, "model"]
print("Mejor modelo por F1_macro:", best_model_name)



# Guardar columnas finales (después del one-hot)
joblib.dump(list(X.columns), "../model_ml/columns.pkl")

# Guardar scaler
joblib.dump(scaler, "../model_ml/scaler.pkl")

# Guardar encoder de labels (por si lo necesitas)
joblib.dump(le, "../model_ml/label_encoder.pkl")

# Guardar columnas categóricas originales
joblib.dump(cat_cols, "../model_ml/categorical_cols.pkl")


joblib.dump(best_rf, "../model_ml/model_rf.pkl")
joblib.dump(best_svm, "../model_ml/model_svm.pkl")

print("Modelos guardados exitosamente en /model_ml/")