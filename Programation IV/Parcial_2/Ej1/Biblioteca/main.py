import os
from biblioteca import Biblioteca
from libro import Libro

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresiona Enter para continuar...")

def main():
    mi_biblioteca = Biblioteca()

    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", ["Realismo mágico", "Ficción"], 471, "Sudamericana", 1967, "Primera")
    libro2 = Libro("1984", "George Orwell", ["Distopía", "Ciencia ficción"], 328, "Secker & Warburg", 1949, "Primera")

    mi_biblioteca.añadir_libro(libro1)
    mi_biblioteca.añadir_libro(libro2)

    for libro in mi_biblioteca.libros:
        if not os.path.exists(f"{libro.get_nombre()}.json"):
            libro.guardar_json()

    while True:
        limpiar_consola()
        print("=== MENÚ DE BIBLIOTECA ===")
        print("1. Listar libros")
        print("2. Añadir libro")
        print("3. Editar libro")
        print("4. Eliminar libro")
        print("5. Ver detalles de un libro")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            limpiar_consola()
            mi_biblioteca.listar_libros()
            pausar()

        elif opcion == "2":
            limpiar_consola()
            mi_biblioteca.crear_libro()
            pausar()

        elif opcion == "3":
            limpiar_consola()
            nombre = input("Nombre del libro a editar: ").strip()
            mi_biblioteca.editar_libro(nombre)
            pausar()

        elif opcion == "4":
            limpiar_consola()
            nombre = input("Nombre del libro a eliminar: ").strip()
            mi_biblioteca.eliminar_libro(nombre)
            pausar()

        elif opcion == "5":
            limpiar_consola()
            nombre = input("Nombre del libro que desea ver: ").strip()
            mi_biblioteca.ver_libro(nombre)
            pausar()

        elif opcion == "6":
            limpiar_consola()
            print("Gracias por usar la Biblioteca.")
            print("Hasta luego")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
            pausar()

if __name__ == "__main__":
    main()
