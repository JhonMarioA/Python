import json

class Libro:
    def __init__(self, nombre, autor, generos, paginas, editorial, anio, edicion):
        self.__nombre = nombre
        self.__autor = autor
        self.__generos = generos
        self.__paginas = paginas
        self.__editorial = editorial
        self.__anio = anio
        self.__edicion = edicion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, new):
        if isinstance(new, str):
            self.__nombre = new
        else:
            raise ValueError("El nombre debe ser una cadena de texto")

    def get_autor(self):
        return self.__autor

    def set_autor(self, new):
        if isinstance(new, str):
            self.__autor = new
        else:
            raise ValueError("El autor debe ser una cadena de texto")

    def get_generos(self):
        return self.__generos

    def set_generos(self, new):
        if isinstance(new, list) and all(isinstance(x, str) for x in new):
            self.__generos = new
        else:
            raise ValueError("Los géneros deben ser una lista de cadenas de texto")

    def get_paginas(self):
        return self.__paginas

    def set_paginas(self, new):
        if isinstance(new, int) and new > 0:
            self.__paginas = new
        else:
            raise ValueError("El número de páginas debe ser un entero positivo")

    def get_editorial(self):
        return self.__editorial

    def set_editorial(self, new):
        if isinstance(new, str):
            self.__editorial = new
        else:
            raise ValueError("La editorial debe ser una cadena de texto")

    def get_anio(self):
        return self.__anio

    def set_anio(self, new):
        if isinstance(new, int) and new > 0 and new <= 2025:
            self.__anio = new
        else:
            raise ValueError("El anio debe ser un número positivo y no mayor a 2025")

    def get_edicion(self):
        return self.__edicion

    def set_edicion(self, new):
        if isinstance(new, str):
            self.__edicion = new
        else:
            raise ValueError("La edición debe ser una cadena de texto")

    def obtener_diccionario(self):
        diccionario = {
            "nombre": self.get_nombre(),
            "autor": self.get_autor(),
            "generos": self.get_generos(),
            "paginas": self.get_paginas(),
            "editorial": self.get_editorial(),
            "anio": self.get_anio(),
            "edicion": self.get_edicion(),
        }
        return diccionario

    def guardar_json(self):
        try:
            with open(f"{self.get_nombre()}.json", "w", encoding="utf-8") as f:
                json.dump(self.obtener_diccionario(), f, indent=4)
                print("Archivo generado exitosamente")
        except Exception as e:
            print(f"Error - {e}")
