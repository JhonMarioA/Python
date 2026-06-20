#PR
import xml.etree.ElementTree as ET

"""
1) Clase Producto
2) Clase Cliente
3) Clase Tienda
"""

#_____________________________________________________________________

class Producto():
    def __init__(self, nombre, id, precio, cantidad_en_inventario):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.cantidad_en_inventario = cantidad_en_inventario

    def disminuir_inventario(self, cantidad):
        self.cantidad_en_inventario -= cantidad

    @staticmethod
    def aumentar_inventario(producto_aumentar, cantidad):
        encontrado = False
        for producto in Tienda.lista_productos_disponibles:
            if producto.nombre == producto_aumentar:
                encontrado = True
                producto.cantidad_en_inventario += cantidad
                break
        if not encontrado:
            print("Producto no encontrado!!!.")

    @staticmethod
    def mostrar_informacion(id):
        encontrado = False
        for producto in Tienda.lista_productos_disponibles:
            if producto.id == id:
                encontrado = True
                break
        if encontrado:
            print("Información del producto: ")
            print(f"Nombre: {producto.nombre}, id: {producto.id}, precio: {producto.precio}, cantidad en inventario: {producto.cantidad_en_inventario}\n")
        else:
            print("Producto no encontrado.")

#_____________________________________________________________________

class Cliente():
    def __init__(self, nombre, id, saldo):
        self.nombre = nombre
        self.id = id
        self.saldo = saldo

    def realizar_compra(self, producto, cantidad):
        self.saldo -= (producto.precio * cantidad)

    @staticmethod
    def mostrar_informacion(id):
        encontrado = False
        for cliente in Tienda.lista_clientes_registrados:
            if cliente.id == id:
                encontrado = True
                break
        if encontrado:
            print("Información del cliente: ")
            print(f"Nombre: {cliente.nombre}, id: {cliente.id}, saldo: {cliente.saldo}.\n")
        else:
            print("Cliente no encontrado.")

#_____________________________________________________________________


class Tienda():
    lista_productos_disponibles = []
    lista_clientes_registrados = []

    def agregar_producto(self, producto):
        self.lista_productos_disponibles.append(producto)

    def agregar_cliente(self, cliente):
        self.lista_clientes_registrados.append(cliente)

    def realizar_venta(self, id_cliente, id_producto, cantidad):
        cliente = None
        producto = None

        for c in self.lista_clientes_registrados:
            if c.id == id_cliente:
                cliente = c
                break
        for p in self.lista_productos_disponibles:
            if p.id == id_producto:
                producto = p
                break

        if not cliente or not producto:
            print("Cliente o producto no encontrado!!!.")
            return

        if cliente.saldo < (producto.precio * cantidad) or producto.cantidad_en_inventario < cantidad:
            print("El saldo o el inventario del producto es insuficiente!!!.")
            return

        cliente.realizar_compra(producto, cantidad)
        producto.disminuir_inventario(cantidad)

    def mostrar_productos(self):
        for producto in Tienda.lista_productos_disponibles:
            print(f"Nombre: {producto.nombre}, id: {producto.id}, precio: {producto.precio}, cantidad en inventario: {producto.cantidad_en_inventario}")

    def mostrar_clientes(self):
        for cliente in Tienda.lista_clientes_registrados:
            print(f"Nombre: {cliente.nombre}, id: {cliente.id}, saldo: {cliente.saldo}")

    # Guardar datos en XML
    @staticmethod
    def guardar_datos(nombre_archivo="tienda.xml"):
        root = ET.Element("tienda")

        # Guardar productos
        productos_elem = ET.SubElement(root, "productos")
        for p in Tienda.lista_productos_disponibles:
            producto_elem = ET.SubElement(productos_elem, "producto", {"id": p.id})
            ET.SubElement(producto_elem, "nombre").text = p.nombre
            ET.SubElement(producto_elem, "precio").text = str(p.precio)
            ET.SubElement(producto_elem, "cantidad").text = str(p.cantidad_en_inventario)

        # Guardar clientes
        clientes_elem = ET.SubElement(root, "clientes")
        for c in Tienda.lista_clientes_registrados:
            cliente_elem = ET.SubElement(clientes_elem, "cliente", {"id": c.id})
            ET.SubElement(cliente_elem, "nombre").text = c.nombre
            ET.SubElement(cliente_elem, "saldo").text = str(c.saldo)

        tree = ET.ElementTree(root)
        tree.write(nombre_archivo, encoding="utf-8", xml_declaration=True)
        print(f"Datos guardados en {nombre_archivo}")

    # Cargar datos desde XML
    @staticmethod
    def cargar_datos(nombre_archivo="tienda.xml"):
        try:
            tree = ET.parse(nombre_archivo)
            root = tree.getroot()

            # Limpiar listas actuales
            Tienda.lista_productos_disponibles.clear()
            Tienda.lista_clientes_registrados.clear()

            # Cargar productos
            for producto_elem in root.find("productos"):
                nombre = producto_elem.find("nombre").text
                id = producto_elem.get("id")
                precio = int(producto_elem.find("precio").text)
                cantidad = int(producto_elem.find("cantidad").text)
                Tienda.lista_productos_disponibles.append(Producto(nombre, id, precio, cantidad))

            # Cargar clientes
            for cliente_elem in root.find("clientes"):
                nombre = cliente_elem.find("nombre").text
                id = cliente_elem.get("id")
                saldo = int(cliente_elem.find("saldo").text)
                Tienda.lista_clientes_registrados.append(Cliente(nombre, id, saldo))

            print(f"Datos cargados desde {nombre_archivo}")
        except FileNotFoundError:
            print("No existe un archivo de datos para cargar.")


#___________________________________________________________________

def menu():
    
    tienda = Tienda()

    print("Bienvendio al sistema de ventas de productos!!!")
    while True:
        print("Elija una opción:\n")
        print("1. Agregar cliente.")
        print("2. Agregar producto.")
        print("3. Realizar venta.")
        print("4. Mostrar productos.")
        print("5. Mostrar clientes.")
        print("6. Mostrar informacioń de un cliente.")
        print("7. Mostrar información de un producto")
        print("8. Sumar stock.")
        print("9. Guardar datos.")
        print("10. Cargar datos.\n")

        opcion = int(input("Opción: "))
        
        match opcion:

            case 1:
                print("Agregar un cliente:\n")
                nombre = input("Nombre: ")
                id = input("Id: ")
                saldo = int(input("Saldo: "))
                cliente = Cliente(nombre, id, saldo)
                tienda.agregar_cliente(cliente)

            case 2:
                print("Agregar un producto:\n")
                nombre = input("Nombre: ")
                id = input("Id: ")
                precio = int(input("Precio: "))
                cantidad_en_inventario = int(input("Cantidad en inventario: "))
                producto = Producto(nombre, id, precio, cantidad_en_inventario)
                tienda.agregar_producto(producto)

            case 3:
                print("Realizar venta:\n")
                id_cliente = input("Id del cliente: ")
                id_producto = input("Id del producto: ")
                cantidad = int(input("Cantidad: "))
                tienda.realizar_venta(id_cliente, id_producto, cantidad)

            case 4:
                tienda.mostrar_productos()
            case 5:
                tienda.mostrar_clientes()
            case 6:
                id = input("Ingrese el id del cliente a buscar: ")
                Cliente.mostrar_informacion(id)
            case 7:
                id = input("Ingrese el id del producto a buscar: ")
                Producto.mostrar_informacion(id)
            case 8: 
                print("Aumentar stock:\n")
                producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                Producto.aumentar_inventario(producto, cantidad)
            case 9:
                Tienda.guardar_datos()
            case 10:
                Tienda.cargar_datos()
    
menu()
