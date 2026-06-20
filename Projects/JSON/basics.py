import json

producto = {
    "nombre": "Celular",
    "precio": 1000000,
    "caracteristicas": ["8GB RAM", "12MPX"],
    "en_stock": True
}

# Convertir un dic en un json
texto_json = json.dumps(producto, indent=3)
print(texto_json)

# Guardar en un archivo .json
with open("producto.json", "w", encoding="utf-8") as f:
    json.dump(producto, f, indent=3)

# Convertir de un json a dic
with open("producto.json", "r", encoding="utf-8") as f:
    info_del_json = json.load(f)

print(info_del_json["precio"])


producto2 = '{"nombre": "Celular","precio": 1000000,"caracteristicas": ["8GB RAM", "12MPX"],"en_stock": true}'

# Convetir de texto json a dict de Python
dic = json.loads(producto2)
print(dic)