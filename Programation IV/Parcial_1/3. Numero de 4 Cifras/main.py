import os

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def ejercicio():
    while True:
        print("===================================")
        print("    Trabajo con números de 4 cifras")
        print("===================================")

        numero = int(input("Ingrese un número entero de 4 cifras: "))

        if numero < 1000 or numero > 9999:
            print("ERROR - El número no es de 4 cifras")
        else:
            d1 = numero // 1000         
            d2 = (numero // 100) % 10  
            d3 = (numero // 10) % 10
            d4 = numero % 10

            if d4 == 0:
                print(f"No se puede comprobar si {d1} es múltiplo de {d4} (división por cero).")
            else:
                if d1 % d4 == 0:
                    print(f"El primer número {d1} SÍ es múltiplo de {d4}")
                else:
                    print(f"El primer número {d1} NO es múltiplo de {d4}")
                    
            print(f"La suma del segundo número {d2} y el tercero {d3} es: {d2 + d3}")

        opcion = input("\n¿Quieres hacerlo de nuevo? (s/n): ").strip().lower()
        if opcion != "s":
            print("\nSaliendo del programa...")
            limpiar_consola()
            break
        else:
            limpiar_consola()

limpiar_consola()
ejercicio()
