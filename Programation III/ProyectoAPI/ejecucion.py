from ui.entrada_de_datos import pedir_datos_usuario
from api.obtener_datos import conectar_api 
from api.procesar_datos import filtrar_registros, convertir_registros
from ui.salida_de_datos import mostrar_registros

def ejecucion():

    departamento, cantidad_de_registros = pedir_datos_usuario()
    registros = conectar_api(departamento, cantidad_de_registros)
    registros_filtrados = filtrar_registros(registros, [
        "ciudad_municipio_nom",
        "departamento_nom",
        "edad",
        "tipo",
        "estado",
        "pais_viajo_1_nom"
    ])
    registros_listos = convertir_registros(registros_filtrados)
    mostrar_registros(registros_listos)


ejecucion()


