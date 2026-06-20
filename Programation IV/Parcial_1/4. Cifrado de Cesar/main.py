import os

class Texto:
    def __init__(self, archivo):
        listaLin = []
        with open(archivo, "r") as f:
            for linea in f:
                listaLin.append(linea.strip().split(" "))

        self.lineas = listaLin

    def encriptar(self, clave):

        resultado = []

        for linea in self.lineas:
            newLinea = []
            for palabra in linea:
                newPalabra = ""
                for letra in palabra:
                    if 65 <= ord(letra) <= 90:
                        base = 65
                        newLetra = chr((ord(letra) - base + clave) % 26 + base)
                        newPalabra += newLetra
                    elif 97 <= ord(letra) <= 122:
                        base = 97
                        newLetra = chr((ord(letra) - base + clave) % 26 + base)
                        newPalabra += newLetra
                    else:
                        newPalabra += letra
                newLinea.append(newPalabra)
            resultado.append(newLinea)

        return resultado

    def desencriptar(self, clave):

        return self.encriptar(-clave)

    def guardar_encriptado(self, archivo, clave):
        encriptado = self.encriptar(clave)
        with open(f"{archivo}-encriptado.txt", "w") as f:
            for linea in encriptado:
                f.write(" ".join(linea) + "\n")

    def guardar_desencriptado(self, archivo, clave):
        encriptado = self.desencriptar(clave)
        with open(f"{archivo}-desencriptado.txt", "w") as f:
            for linea in encriptado:
                f.write(" ".join(linea) + "\n")

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def ejercicio():
    while True:
        print("===================================")
        print("        Cifrado de César       ")
        print("===================================")
        print("Asegúrate de que el archivo de entrada esté en el mismo directorio.")
        print("-----------------------------------")

        archivo = input("Nombre del archivo de entrada (sin .txt): ").strip()
        clave = int(input("Clave del cifrado César: "))
        opcion = input("¿Quieres (E)ncriptar o (D)esencriptar? ").strip().lower()

        try:
            texto = Texto(f"{archivo}.txt")

            if opcion == "e":
                texto.guardar_encriptado(archivo, clave)
                print(f"\nTexto encriptado guardado en {archivo}-encriptado.txt")
            elif opcion == "d":
                texto.guardar_desencriptado(archivo, clave)
                print(f"\nTexto desencriptado guardado en {archivo}-desencriptado.txt")
            else:
                print("\nOpción no válida.")
        except FileNotFoundError:
            print(f"\nEl archivo {archivo}.txt no fue encontrado.")

        opcion = input("\n¿Quieres hacerlo de nuevo? (s/n): ").strip().lower()
        if opcion != "s":
            print("\nSaliendo del programa...")
            limpiar_consola()
            break
        else:
            limpiar_consola()

limpiar_consola()
ejercicio()