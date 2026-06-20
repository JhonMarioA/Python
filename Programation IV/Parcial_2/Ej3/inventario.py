from productos import Producto, Electronico, Alimento, Ropa
import os


class Inventario:
    def __init__(self, productos=None):
        self.productos = productos if productos else []

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
            return 1  # Éxito
        return -1  # Error

    def listar_productos(self):
        if len(self.productos) == 0:
            return 0  # No hay productos
        else:
            lista = ""
            for p in self.productos:
                lista += f"{p}\n"
            return lista

    def buscar_producto(self, nombre):
        if len(self.productos) == 0:
            return 0  # No hay productos
        else:
            for p in self.productos:
                if p.get_nombre().lower() == nombre.lower():
                    return p  
            return 0  # No se encontró
        
    def eliminar_producto(self, producto):
        self.productos.remove(producto)
        archivo = f"{producto.get_nombre()}.json"
        if os.path.exists(archivo):
            os.remove(archivo)
        return 1  # Éxito
    
    
