from inventario import Inventario
from productos import Electronico, Ropa, Alimento
import json

def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE PEDIDOS =====")
    print("1. Mostrar productos disponibles")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Realizar pedido")
    print("5. Guardar productos en JSON")
    print("6. Salir")
    return input("Seleccione una opción: ")

def agregar_producto(inventario):
    tipo = input("Tipo de producto (E=Electrónico, R=Ropa, A=Alimento): ").upper()
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad disponible: "))

    if tipo == "E": 
        garantia = int(input("Garantía (meses): "))
        p = Electronico(nombre, precio, cantidad, garantia)
    elif tipo == "R":
        tamano = input("Tamaño: ")
        p = Ropa(nombre, precio, cantidad, tamano)
    elif tipo == "A":
        fecha = input("Fecha de caducidad (dd/mm/aaaa): ")
        p = Alimento(nombre, precio, cantidad, fecha)
    else:
        print("Tipo inválido.")
        return
    
    inventario.agregar_producto(p)
    print("Producto agregado con éxito.")

def realizar_pedido(inventario):
    nombre = input("Ingrese el nombre del producto a comprar: ")
    producto = inventario.buscar_producto(nombre)
    if producto == 0:
        print("Producto no encontrado.")
        return

    cantidad = int(input("Ingrese cantidad a comprar: "))
    if cantidad > producto.get_cantidad():
        print("No hay suficiente stock disponible.")
        return

    total = producto.calcular_precio(cantidad)
    producto.vender_productos(cantidad)
    print(f"Pedido realizado con éxito.")
    print(f"Total a pagar: ${total:.2f}")
    print(f"Stock restante: {producto.get_cantidad()}")

def guardar_json(inventario):
    datos = []
    for p in inventario.productos:
        d = {
            "nombre": p.get_nombre(),
            "precio": p.get_precio(),
            "cantidad": p.get_cantidad()
        }
        if isinstance(p, Electronico):
            d["garantia"] = p.get_garantia()
        elif isinstance(p, Ropa):
            d["tamano"] = p.get_tamano()
        elif isinstance(p, Alimento):
            d["fecha_caducidad"] = p.get_fecha()
        datos.append(d)

    with open("inventario.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print("Inventario guardado en 'inventario.json'.")

#Func principal
def main():
    inventario = Inventario()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            lista = inventario.listar_productos()
            if lista == 0:
                print("No hay productos registrados.")
            else:
                print(lista)
        elif opcion == "2":
            agregar_producto(inventario)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            producto = inventario.buscar_producto(nombre)
            if producto == 0:
                print("Producto no encontrado.")
            else:
                inventario.eliminar_producto(producto)
                print("Producto eliminado correctamente.")
        elif opcion == "4":
            realizar_pedido(inventario)
        elif opcion == "5":
            guardar_json(inventario)
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente nuevamente.")

main()