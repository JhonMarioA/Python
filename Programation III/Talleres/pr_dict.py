

 
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

mes = "Noviembre"


for signo, (mini, maxi) in signos[mes].items():
    print(signo, mini, maxi)
        