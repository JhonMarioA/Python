
# 8._________________

def signo_zodiacal():
    
    mes = input("Ingrese el mes de nacimiento (ejemplo: Marzo): ")
    dia = int(input("Ahora ingrese el día: ")) 
    
    signos = {
        "Enero": {"Capricornio": (1, 19), "Acuario": (20, 31)}, 
        "Febrero": {"Acuario": (1, 18), "Piscis": (19, 29)}, 
        "Marzo": {"Piscis": (1, 20), "Aries": (21, 31)},
        "Abril": {"Aries": (1, 20), "Tauro": (21, 30)},
        "Mayo": {"Tauro": (1, 20), "Geminis": (21, 31)},
        "Junio": {"Geminis": (1, 20), "Cancer": (21, 30)},
        "Julio": {"Cancer": (1, 22), "Leo": (23, 31)},
        "Agosto": {"Leo": (1, 22), "Virgo": (23, 31)},
        "Septiembre": {"Virgo": (1, 22), "Libra": (23, 30)},
        "Octubre": {"Libra": (1, 22), "Escorpio": (23, 31)},
        "Noviembre": {"Escorpio": (1, 21), "Sagitario": (22, 30)},
        "Diciembre": {"Sagitario": (1, 21), "Capricornio": (22, 31)}
    }

    if mes in signos:
        for signo, (inicio, fin) in signos[mes].items():
            if inicio <= dia <= fin:
                print(f"Su signo zodiacal es: {signo}")
                return
        print("Día inválido para el mes ingresado.")
    else:
        print("Mes inválido.")

#signo_zodiacal()


# 9._________________

def calificacion_empleados():

    calificacion = float(input("Ingrese la calificación: "))

    if calificacion < 0.0 or (calificacion > 0 and calificacion < 0.4) or (calificacion > 0.4 and calificacion < 0.6):
        print(f"Calificación: {calificacion} invalida.")
        return

    if calificacion == 0.0:
        print("Rendimiento es inaceptable")
    elif calificacion == 0.4:
        print("Rendimiento aceptable")
    elif calificacion => 0.6:
        print("Meritorious performance")

    print(f"El aumento del trabajador es ${2400*calificacion}")

calificacion_empleados()