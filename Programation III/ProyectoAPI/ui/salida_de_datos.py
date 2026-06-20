

def mostrar_registros(registros_listos):
    
    if not registros_listos:
        print("\nNo se encontraron registros.")
        return
    
    for registro in registros_listos:
        print(registro)
    