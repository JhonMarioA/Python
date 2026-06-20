from libro import Libro
import os

class Biblioteca:
    def __init__(self):
        self.libros = []
        
    def listar_libros(self):
        if not self.libros:
            print("No hay libros registrados.")
        else:
            print("\n--- LIBROS EN LA BIBLIOTECA ---")
            for lib in self.libros:
                print(f"- {lib.get_nombre()} ({lib.get_autor()})")

    def crear_libro(self):
        nombre = input("Nombre: ")
        autor = input("Autor: ")
        generos = input("Géneros (separados por comas): ").split(",")
        generos = [g.strip() for g in generos]
        paginas = int(input("Número de páginas: "))
        editorial = input("Editorial: ")
        anio = int(input("Año de publicación: "))
        edicion = input("Edición: ")
        nuevo = Libro(nombre, autor, generos, paginas, editorial, anio, edicion)
        self.añadir_libro(nuevo)

    def añadir_libro(self, libro):
        if isinstance(libro, Libro):
            self.libros.append(libro)
            libro.guardar_json()
            print(f"Libro '{libro.get_nombre()}' añadido con éxito.")
        else:
            print("Error: el objeto no es una instancia de Libro.")

    def editar_libro(self, nombre):
        for i, lib in enumerate(self.libros):
            if nombre.lower() == lib.get_nombre().lower():
                print(f"Editando '{lib.get_nombre()}'...")
                self.libros[i] = self.crear_libro()
                self.libros[i].guardar_json()
                print("Libro actualizado con éxito.")
                break
        else:
            print("No se encontró un libro con ese nombre.")

    def eliminar_libro(self, nombre):
        for lib in self.libros:
            if nombre.lower() == lib.get_nombre().lower():
                conf = input(f"¿Desea eliminar '{lib.get_nombre()}'? (Y para confirmar): ")
                if conf.lower() == "y":
                    self.libros.remove(lib)
                    archivo = f"{lib.get_nombre()}.json"
                    if os.path.exists(archivo):
                        os.remove(archivo)
                    print(f"Libro '{lib.get_nombre()}' eliminado con éxito.")
                else:
                    print("Eliminación cancelada.")
                break
        else:
            print("No se encontró un libro con ese nombre.")

    def ver_libro(self, nombre):
        for lib in self.libros:
            if nombre.lower() == lib.get_nombre().lower():
                print("\n--- DETALLES DEL LIBRO ---")
                print(f"Nombre: {lib.get_nombre()}")
                print(f"Autor: {lib.get_autor()}")
                print(f"Géneros: {', '.join(lib.get_generos())}")
                print(f"Páginas: {lib.get_paginas()}")
                print(f"Editorial: {lib.get_editorial()}")
                print(f"Año: {lib.get_anio()}")
                print(f"Edición: {lib.get_edicion()}")
                break
        else:
            print("No se encontró un libro con ese nombre.")
