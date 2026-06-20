import json

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, new):
        if isinstance(new, str):
            self.__nombre = new
        else:
            raise ValueError("El nombre debe ser una cadena de texto")

    def get_precio(self):
        return self.__precio

    def set_precio(self, new):
        if isinstance(new, (int, float)) and new >= 0:
            self.__precio = new
        else:
            raise ValueError("El precio debe ser un número positivo")

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, new):
        if isinstance(new, int) and new >= 0:
            self.__cantidad = new
        else:
            raise ValueError("La cantidad debe ser un número entero positivo")

    def calcular_precio(self, cantidad):
        if isinstance(cantidad, int) and cantidad >= 0:
            return cantidad * self.get_precio()
        else:
            return -1  # Código de error

    def vender_productos(self, cantidad):
        if cantidad <= self.get_cantidad():
            self.set_cantidad(self.get_cantidad() - cantidad)
            return 1  # Código de éxito
        else:
            return -1  # Código de error
        
    def __str__(self):
        return f"{self.get_nombre()} - ${self.get_precio()} - Cantidad: {self.get_cantidad()}"
    
    def guardar_json(self):
        diccionario ={
            "nombre":self.get_nombre(),
            "precio":self.get_precio(),
            "cantidad":self.get_cantidad()
        }
        try:
            with open(f"{self.get_nombre()}.json", "w", encoding="utf-8") as f:
                json.dump(diccionario, f, indent=4)
                return 1
        except Exception as e:
            return f"Error - {e}"


class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, garantia):
        Producto.__init__(self, nombre, precio, cantidad)
        self.__garantia = garantia

    def get_garantia(self):
        return self.__garantia

    def set_garantia(self, new):
        if isinstance(new, int) and new >= 0:
            self.__garantia = new
        else:
            raise ValueError("La garantía debe ser un número entero positivo")

    def calcular_precio(self, cantidad):
        if isinstance(cantidad, int) and cantidad > 0:
            total = cantidad * self.get_precio()
            if cantidad >= 5:
                total *= 0.9  # 10% de descuento
            return total
        else:
            return -1
        
    def __str__(self):
        return f"{super().__str__()} - Garantía: {self.get_garantia()} meses"
    
    def guardar_json(self):
        diccionario ={
            "nombre":self.get_nombre(),
            "precio":self.get_precio(),
            "cantidad":self.get_cantidad(),
            "garantia":self.get_garantia()
        }
        try:
            with open(f"{self.get_nombre()}.json", "w", encoding="utf-8") as f:
                json.dump(diccionario, f, indent=4)
                return 1
        except Exception as e:
            return f"Error - {e}"


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, tamano):
        Producto.__init__(self, nombre, precio, cantidad)
        self.__tamano = tamano

    def get_tamano(self):
        return self.__tamano

    def set_tamano(self, new):
        if isinstance(new, str):
            self.__tamano = new
        else:
            raise ValueError("El tamaño debe ser una cadena")

    def calcular_precio(self, cantidad):
        if isinstance(cantidad, int) and cantidad > 0:
            total = cantidad * self.get_precio()
            if cantidad >= 5:
                total *= 0.85  # 15% de descuento
            return total
        else:
            return -1
        
    def __str__(self):
        return f"{super().__str__()} - Tamano: {self.get_tamano()}"
    
    def guardar_json(self):
        diccionario ={
            "nombre":self.get_nombre(),
            "precio":self.get_precio(),
            "cantidad":self.get_cantidad(),
            "tamano":self.get_tamano()
        }
        try:
            with open(f"{self.get_nombre()}.json", "w", encoding="utf-8") as f:
                json.dump(diccionario, f, indent=4)
                return 1
        except Exception as e:
            return f"Error - {e}"

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha):
        Producto.__init__(self, nombre, precio, cantidad)
        self.__fecha = fecha

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, new):
        if isinstance(new, str):
            self.__fecha = new
        else:
            raise ValueError("La fecha debe ser una cadena")

    def calcular_precio(self, cantidad):
        if isinstance(cantidad, int) and cantidad > 0:
            total = cantidad * self.get_precio()
            if cantidad >= 5:
                total *= 0.95  # 5% de descuento
            return total
        else:
            return -1
        
    def __str__(self):
        return f"{super().__str__()} - Fecha de caducidad: {self.get_fecha()}"
    
    def guardar_json(self):
        diccionario ={
            "nombre":self.get_nombre(),
            "precio":self.get_precio(),
            "cantidad":self.get_cantidad(),
            "fecha_caducidad":self.get_fecha()
        }
        try:
            with open(f"{self.get_nombre()}.json", "w", encoding="utf-8") as f:
                json.dump(diccionario, f, indent=4)
                return 1
        except Exception as e:
            return f"Error - {e}"
