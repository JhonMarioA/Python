
# 1. ____________________

def punto_1():
    estatura = float(input("Ingrese la estatura (0 para salir): "))
    sumatoria = 0
    cantidad = 0

    if estatura == 0:
        print("Error. El primer valor no debe ser 0.")
        return  

    while True:
        sumatoria += estatura
        cantidad += 1

        estatura = float(input("Estatura (0 para salir): "))
        if estatura == 0:
            break

    print(f"El promedio de estatura es {(sumatoria / cantidad)}.")

# punto_1()



# 2. _____________________


def punto_2():

    estatura = float(input("Ingrese la estatura: "))
    sumatoria = 0
    cantidad = 0

    while True:
        sumatoria += estatura
        cantidad += 1

        continuar = (input("Desea ingresar más estatura [S/N]: "))

        if continuar == "N":
            break
        
        estatura = float(input("Estatura: "))

    print(f"El promedio de estatura es {(sumatoria / cantidad)}.")


# punto_2()


# 3. _______________________ (Toca con librería)

def conversion(C):
    F = (C * 9/5) + 32
    return F

def punto_3():
    
    Celsius = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    print("| CELSIUS | FAHRENHEIT |")

    for i in range(10):
        print(f"|    {Celsius[i]}   |     {conversion(Celsius[i])}   |")

# punto_3()


# 4. ________________________

def punto_4():

    cantidad_pasajeros = int(input("Ingrese la cantida de pasajeros: "))
    total = 0

    for i in range(cantidad_pasajeros):
        rango = int(input(f"Ingrese la edad {i}: "))
        
        if rango <= 3:
            pass
        elif rango > 3 and rango < 11:
            total += 16000
        elif rango >= 11 and rango <= 50:
            total += 34000
        else:
            total += 40000

    print(total)

# punto_4()

# 5. _______________________

def punto_5():

    lista_registros = ['ref-010', 'ac-090','ref-010','xp-89','as-65','kj-11','xp-89', 'wx-23','rk-87','as-65']
    print(f"Lista original: {lista_registros}")
    lista_registros = set(lista_registros)
    print(f"Lista sin repetidos: {lista_registros}")

# punto_5()


# 6. ______________________

def punto_6():

    palabra = input("Ingrese la palabra: ")
    lista_consonantes = []
    lista_vocales = ["a", "e", "i", "o", "u"]
    
    for i in palabra:
        if i in lista_vocales:
            pass 
        else:
            lista_consonantes.append(i)

    print(f"Palabra original: {palabra}\n Lista de consonantes: {lista_consonantes}")

#punto_6()


#7. _______________________

def punto_7():

    lista_progra_III = ["Daniel", "Pedro", "María", "Juan"]
    lista_progra_IV = ["Daniel", "Yeremaia", "David Ospina", "Botero", "Pedro"]
    lista_III_IV = []
    tamaño = 0

    for i in lista_progra_III:
        if i in lista_progra_IV:
            lista_III_IV.append(i)

    print(f"Lista programación III {lista_progra_III}\nLista programación IV: {lista_progra_IV}")
    print(f"Personas que estan en ambas listas: {lista_III_IV}")

#punto_7()
        

#8. ________________________

def punto_8():

    lista = ["ls", 45, "cat", ["cd", "touch"]]

    sub_lista = any(isinstance(elemento, list) for elemento in lista)
    if sub_lista:
        print("Existe almenos una sub-lista.")
    else:
        print("No existen sub-listas.")

#punto_8()

    
#9. _______________________

def punto_9():

    productos = {
    "Brocha": 500,
    "Espatula": 2000,
    "Pala": 54000,
    "Carretilla": 300000,
    "Casco": 55000,
    "Soldador": 230000,
    "Alicate": 10000,
    "Destornillador": 3000,
    "Maza": 60000,
    "Nivel": 24000,
    "Flexometro": 76000,
    "Hacha": 32000,
    "Pico": 74000,
    "Rastrillos": 56000
    }

    productos_ordenados = dict(sorted(productos.items()))
    print(productos)
    print("\n")
    print(productos_ordenados)

#punto_9()

#10. ______________________

def punto_10():

    vocalistas = []

    bandas = {
    "Queen": [
        "Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"
    ],
    "The Doors": [
        "Jim Morrison", "Robby Krieger", "Ray Manzarek", "John Densmore"
    ],
    "Green Day": [
        "Billie Joe Armstrong", "Mike Dirnt", "Tré Cool"
    ],
    "Rolling Stones": [
        "Mick Jagger", "Keith Richards", "Charlie Watts", "Ron Wood"
    ],
    "Led Zeppelin": [
        "Robert Plant", "Jimmy Page", "John Paul Jones", "John Bonham"
    ],
    "Black Sabbath": [
        "Ozzy Osbourne", "Tony Iommi", "Bill Ward", "Geezer Butler"
    ],
    "Soundgarden": [
        "Chris Cornell", "Kim Thayil", "Matt Cameron", "Ben Shepherd"
    ],
    "Alice in Chains": [
        "Layne Staley", "Jerry Cantrell", "Sean Kinney", "Mike Starr"
    ]
    }

    bandas_ordenadas_alfabeticamente = sorted(bandas.items())

    for banda, miembros in bandas_ordenadas_alfabeticamente:
        vocalistas.append((miembros[0], banda))  # (vocalista, banda)

    for vocalista, banda in vocalistas:
        print(f"Vocalista: {vocalista}, Banda: {banda}")


#punto_10()
    
