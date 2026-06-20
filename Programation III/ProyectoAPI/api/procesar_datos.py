

def filtrar_registros(registros, claves):
    
    registros_filtrados = []

    for registro in registros: #registros es una lista de dic, registro es un dic
        registro_modificado = {clave: registro.get(clave, "N/A") for clave in claves} #para cada elemento del iterable, creo una nueva clave y le asigno un valor
                                                                                                      #registro.get(clave, "N/A) -> si en el diccionario "registro" exista la clave "clave" devuelve su valor o "N/A"
        registros_filtrados.append(registro_modificado)

    return registros_filtrados


def convertir_registros(registros_filtrados):
    
    registros_listos = []

    for i, r in enumerate(registros_filtrados, start=1):

        registro = (
            "{i}. Ciudad: {ciudad}, Departamento: {departamento}, Edad: {edad}, "
            "Tipo: {tipo}, Estado: {estado}, País: {pais}"
        ).format(
            i = i,
            ciudad = r.get("ciudad_municipio_nom", "N/A"),
            departamento = r.get("departamento_nom", "N/A"),
            edad = r.get("edad", "N/A"),
            tipo = r.get("tipo", "N/A"),
            estado = r.get("estado", "N/A"),
            pais = r.get("pais_viajo_1_nom", "N/A")
        )

        registros_listos.append(registro)

    return registros_listos
    