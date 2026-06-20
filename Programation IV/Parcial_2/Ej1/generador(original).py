# 1. Se importa la librería JSON.
import json

# 2. Se inicia una función llamada "generar_json", que recibe una ruta de archivos, y un diccionario con datos.
def generar_json(direccion_archivo,datos):

    # 3. Se trata de abrir el archivo indicado en la función como "archivo_json"
    try:
        with open(direccion_archivo,'w') as archivo_json:
            # 4. Se usa la función "json.dump" para crear un archivo JSON con los datos del diccionario, en la ruta abierta, y con una identación de 4 espacios.
            json.dump(datos,archivo_json,indent=4)
        # 5. Se imprime un mensaje de éxito.
        print("El archivo se ha generado con exito.")
    # 6. Si no se puede abrir el archivo, se hace una excepción y se muestra el error
    except Exception as e:
        print(f"Ocurrio un error: {e}")

# 7. Se crea un diccionario de ejemplo con muchos datos
datos = {
    "nombre":"Andres Felipe",
    "edad":33,
    "profesion": "Ingeniero",
    "habilidades":["Python","Java","SCRUM","Redes"],
    "proyecto":[
        {"nombre":"Procesamiento de datos","Universidad":"UTP"},
        {"nombre":"Articulo Q1","Universidad":"CIAF"}
    ]
}

# 8. Se elige la dirección (Fue cambiada a una ruta relativa)
direccion="docente.json"

# 9. Finalmente, se llama la función para generar el archivo
generar_json(direccion,datos)