import os

class Empleado:
    def __init__(self, nombre, id, salBase, exp):
        self.nombre = nombre
        self.id = int(id)
        self.salBase = float(salBase)
        self.exp = int(exp)
        
    def calcular_salario(self):
        bono = 0
        if 0 <= self.exp <= 2:
            bono = (self.salBase * 5)/100
        elif 3 <= self.exp <= 5:
            bono = (self.salBase * 10)/100
        else:
            bono = (self.salBase * 15)/100
        return self.salBase + bono
    
    def emp_texto(self):
        return (f"{self.nombre} - {self.id} - {self.salBase} - {self.exp} - {self.calcular_salario()}")


class GestorEmpleados:
    def __init__(self, *empleados):
        self.empleados = list(empleados)
        
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def eliminar_empleado(self, id):
        for emp in self.empleados:
            if emp.id == id:
                self.empleados.remove(emp)
                return emp
    
    def buscar_empleado(self, id):
        for emp in self.empleados:
            if emp.id == id:
                return emp
            
    def editar_empleado(self, id, newNombre, newSalBase, newExp, archivo):
        emp = self.buscar_empleado(id)
        if emp:
            emp.nombre = newNombre
            emp.salBase = newSalBase
            emp.exp = newExp
            self.guardar_empleados(archivo)
            return emp
    
    def mostrar_empleados(self):
        for emp in self.empleados:
            print(emp.emp_texto())
            
    def guardar_empleados(self, archivo):
        with open(archivo, "w") as f:
            for emp in self.empleados:
                f.write(emp.emp_texto() + "\n")
            
    def cargar_empleados(self, archivo):
        self.empleados.clear()
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split(" - ")
                if len(partes) == 5:
                    self.agregar_empleado(
                        Empleado(partes[0], partes[1], partes[2], partes[3])
                    )


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresione Enter para continuar...")

def menu():
    gestor = GestorEmpleados()
    archivo = "gestion_empleados.txt"

    while True:
        limpiar_consola()
        print("===================================")
        print("       Menú de Gestión de Empleados")
        print("===================================")
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Buscar empleado")
        print("4. Editar empleado")
        print("5. Mostrar todos los empleados")
        print("6. Guardar empleados en archivo")
        print("7. Cargar empleados desde archivo")
        print("0. Salir")
        print("===================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            id = int(input("ID: "))
            salBase = float(input("Salario base: "))
            exp = int(input("Años de experiencia: "))
            gestor.agregar_empleado(Empleado(nombre, id, salBase, exp))
            print("\nEmpleado agregado correctamente.")
            pausar()

        elif opcion == "2":
            id = int(input("Ingrese el ID del empleado a eliminar: "))
            eliminado = gestor.eliminar_empleado(id)
            if eliminado:
                print(f'\nEmpleado "{eliminado.nombre}" con ID {eliminado.id} eliminado.')
            else:
                print("\nEl empleado no existía.")
            pausar()

        elif opcion == "3":
            id = int(input("Ingrese el ID del empleado a buscar: "))
            emp = gestor.buscar_empleado(id)
            if emp:
                print("\nEmpleado encontrado:")
                print(emp.emp_texto())
            else:
                print("\nEmpleado no encontrado.")
            pausar()

        elif opcion == "4":
            id = int(input("Ingrese el ID del empleado a editar: "))
            newNombre = input("Nuevo nombre: ")
            newSalBase = float(input("Nuevo salario base: "))
            newExp = int(input("Nuevos años de experiencia: "))
            editado = gestor.editar_empleado(id, newNombre, newSalBase, newExp, archivo)
            if editado:
                print(f"\nEmpleado con ID {id} editado y archivo actualizado.")
            else:
                print("\nEl empleado no existía.")
            pausar()

        elif opcion == "5":
            print("\n--- Lista de Empleados ---")
            print("[Nombre] - [ID] - [Salario Base] - [Años de Experiencia] - [Salario Total]")
            gestor.mostrar_empleados()
            pausar()

        elif opcion == "6":
            gestor.guardar_empleados(archivo)
            print(f"\nEmpleados guardados en '{archivo}'.")
            pausar()

        elif opcion == "7":
            try:
                gestor.cargar_empleados(archivo)
                print(f"\nEmpleados cargados desde '{archivo}'.")
            except FileNotFoundError:
                print(f"\nEl archivo '{archivo}' no existe.")
            pausar()

        elif opcion == "0":
            print("\nSaliendo del programa...")
            limpiar_consola()
            break

        else:
            print("\nOpción no válida. Intente de nuevo.")
            pausar()


menu()
