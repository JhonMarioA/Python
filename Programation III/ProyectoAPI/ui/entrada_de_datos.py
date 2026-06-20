

def pedir_datos_usuario():

    print(f"\nBIENVENIDO\nPor favor ingrese la información a consultar:\n")
    nombre_departamento = input("Departamento: ").upper()
    cantidad_de_registros = int(input("Cantidad máxima de registros a mostrar (máx 10000): "))
    if cantidad_de_registros >= 10000 or cantidad_de_registros <= 0:
        print("Cantidad de registros invalida.")
        return

    return nombre_departamento, cantidad_de_registros


