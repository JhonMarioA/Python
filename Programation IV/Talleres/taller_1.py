#Jhon Mario Aguire, Programación IV - Taller 1
import random


#1. _____________________

def ejercicio_1():

    lista = [2, 8, "hola", "programación", 10, "utp", 85, 82, 100, "mundo"]

    numeros = []
    for i in lista:
        if type(i) == int:
            numeros.append(i)

    suma = sum(numeros)
    print(f"La suma de los números es {suma}")


#2. _______________________

def ejercicio_2():
    
    palabras = ["Hola", "mundo", "esto", "es", "Python"]
    cadena = ""

    for i in palabras:
        cadena += i 
        cadena += " "

    print(cadena)


#3. _______________________

def mostrar_mensaje(lista_asignaturas, lista_notas, promedio_asignatura1, promedio_asignatura2):

    print(f"{lista_asignaturas[0]}")
    for j in range(4):
        print(f"nota {j+1}: {lista_notas[0][j]}")

    if promedio_asignatura1 < 3:
        print(f"Promedio de {lista_asignaturas[0]}: {promedio_asignatura1} - asignatura perdida")

    elif promedio_asignatura1 >= 3 and promedio_asignatura1 <= 4:
        print(f"Promedio de {lista_asignaturas[0]}: {promedio_asignatura1} - buen trabajo")

    elif promedio_asignatura1 > 4 and promedio_asignatura1 <= 5:
        print(f"Promedio de {lista_asignaturas[0]}: {promedio_asignatura1} - felicidades seras becado")


    print("\n")
    print(f"{lista_asignaturas[1]}")
    for j in range(4):
        print(f"nota {j+1}: {lista_notas[1][j]}")

    if promedio_asignatura2 < 3:
        print(f"Promedio de {lista_asignaturas[1]}: {promedio_asignatura2} - asignatura perdida")

    elif promedio_asignatura2 >= 3 and promedio_asignatura2 <= 4:
        print(f"Promedio de {lista_asignaturas[1]}: {promedio_asignatura2} - buen trabajo")

    elif promedio_asignatura2 > 4 and promedio_asignatura2 <= 5:
        print(f"Promedio de {lista_asignaturas[1]}: {promedio_asignatura2} - felicidades seras becado")



def ejercicio_3():

    lista_asignaturas = ["Ingles", "Programación"]
    lista_notas = []
  
    promedio_asignatura1 = 0
    promedio_asignatura2 = 0

    for i in range(len(lista_asignaturas)):
        notas = []
        for j in range(4):
            notas.append(int(input(f"Ingrese de {lista_asignaturas[i]} la nota número {j+1}: ")))

        lista_notas.append(notas)
        print("\n")

    promedio_asignatura1 = (sum(lista_notas[0])) / 4
    promedio_asignatura2 = (sum(lista_notas[1])) / 4
    mostrar_mensaje(lista_asignaturas, lista_notas, promedio_asignatura1, promedio_asignatura2)


# 4. _________________________

def ejercicio_4():

    lista_numeros = []
    index = int(input("Ingrese la cantidad de números a agregar a la lista: "))

    for i in range(index):
        numero = int(input(f"número {i+1}: "))
        lista_numeros.append(numero)
        

    for i in lista_numeros:
        print(f"{i}- {pow(i,2)} - {pow(i,3)}")


# 5. _________________________


def ejercicio_5():
    lista_cadenas = []
    index = int(input("Ingrese la cantidad de palabras a agregar a la lista: "))

    for i in range(index):
        cadena = (input(f"cadena {i+1}: "))
        lista_cadenas.append(cadena)

    print(f"cadena mayor = {max(lista_cadenas, key=len)}")
    print(f"cadena menor = {min(lista_cadenas, key=len)}")
    


# 6. __________________________


def ejercicio_6():

    lista_palabras = ["carro", "perro", "avion", "arbol"]
    longitud_palabra = int(input("Ingrese un valor entero: "))

    for i in lista_palabras:
        if longitud_palabra == len(i):
            print(i)


# 7. __________________________

def par_o_impar(palabra):

    if (len(palabra) % 2) == 0:
        return (" es par.")
    else: return (" es impar.")


def ejercicio_7():

    lista = ["oso", "casa", "murcielago", "ventana", "programación", "objetos", "listas", "listas", "métodos", "utp"]

    caracter = input("Por favor ingrese el caracter: ")

    for i in lista:
        if caracter in i:
            print(i + par_o_impar(i))


# 8. __________________________ 

def ejercicio_8():

    lista = ["oso", "casa", "murcielago", "ventana", "programación", "objetos", "listas", "listas", "métodos", "utp"]
    
    caracteres_diferente_a_vocal = 0
    vocales = "aeiouáéíóú"
    

    for palabra in lista:
        for letra in palabra:
            if letra in vocales:
                pass
            else: 
                caracteres_diferente_a_vocal += 1

    print(caracteres_diferente_a_vocal)


# 9. ___________________________

def ejercicio_9():

    lista = []
    print(lista)

    for i in range(15):
        numero = random.randint(1,100)
        lista.append(numero)

    for i in lista:
        print(f"{i} - {pow(i,2)} - {pow(i,3)}")

   
# 10. _________________________ 

def filtrar_con_vocales(lista):

    vocales = "aeiouáéíóú"
    nueva_lista = []

    for palabra in lista:
        tiene_vocal = False
        for letra in palabra:
            if letra in vocales:
                tiene_vocal = True
                break 
        if tiene_vocal:
            nueva_lista.append(palabra)

    return nueva_lista

def ordenar_por_primer_caracter(lista):

    for i in range((len(lista)) - 1):
        for j in range(((len(lista))) - i - 1):        
            if lista[j][0].lower() > lista[j + 1][0].lower():      
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def ejercicio_10():

    lista = ["casa", "programación", "utp", "universidad", "utp", "casa", "casa", "thj", "vbh", "456", "987"]
    print(lista)
    lista = list(set(lista)) #para borrar repetidos convertimos a set y luego de nuevo a lista
    lista = filtrar_con_vocales(lista)
    lista = ordenar_por_primer_caracter(lista)

    print(lista)
