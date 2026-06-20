# Jhon Mario Aguirre - Taller 3, Programación IV
import os

# 1. ___________________________________________

class Libro():
    
    def __init__(self, titulo, autor, año, editorial, genero):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.editorial = editorial
        self.genero = genero
        self.guardar()

    def guardar(self):
        with open("libros.txt", "a") as file:
            file.write(f"{self.titulo}, {self.autor}, {self.año}, {self.editorial}, {self.genero} \n")

    @staticmethod
    def mostrar():
        autor_buscar = input("Ingrese el autor a buscar: ")

        with open("libros.txt", "r") as file:
            for linea in file:
                str(linea)
                datos = linea.strip().split(",")

                if autor_buscar in datos:
                    print(f"Libros del autor {autor_buscar}:\n {linea}")

"""
libro1 = Libro("MMM", "Joung", 2022, "hkj", "comedia")
libro2 = Libro("UUU", "Lebron Gabriel", 2016, "nls", "romance")
Libro.mostrar()
"""
    
# 2. _____________________________________________

class Estudiante():

    def __init__(self, nombre, codigo, carrera, edad, promedio):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
        self.edad = edad
        self.promedio = promedio
        self.guardar()

    def guardar(self):
        with open("estudiantes.txt", "a") as file:
            file.write(f"{self.nombre}, {self.codigo}, {self.carrera}, {self.edad}, {self.promedio} \n")

    @staticmethod    
    def promedio():

        with open("estudiantes.txt", "r") as file:
            for linea in file:

                datos = linea.strip().split(",")

                if float(datos[4]) >= 3.0:
                    print("Haz aprobado!!!")

                else:
                    print("Haz desaprobado!!!")

""""
Estudiante("Juan", 10212, "Ingeniería en sistemas", "18", 3.5)
Estudiante.promedio()
"""

# 3. ________________________________________________


class InventarioProducto():

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.guardar()

    def guardar(self):
        with open("inventario.txt", "a") as file:
            file.write(f"{self.nombre}, {self.precio}, {self.cantidad}\n")

    @staticmethod
    def valor_inventario():

        valor_inventario = 0

        with open("inventario.txt", "r") as file:
            for linea in file:

                datos = linea.strip().split(",")
                print(datos)
                valor_inventario += (int(datos[1]) * int(datos[2]))
                print(valor_inventario)
""""
producto1 = InventarioProducto("arroz", 5000, 10)
producto2 = InventarioProducto("azucar", 3000, 12)
InventarioProducto.valor_inventario()
"""

# 4. ______________________________________________


class Vehiculo():

    def __init__(self, marca, modelo, año, tipo, placa):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.tipo = tipo
        self.placa = placa
        self.guardar()

    def guardar(self):
        if self.año == 2025:
            with open("vehiculos.txt", "a") as file:
                file.write(f"{self.marca}, {self.modelo}, {self.año}, {self.tipo}, {self.placa}\n")
    @staticmethod
    def mostrar():
        if os.path.exists("vehiculos.txt"):
            with open("vehiculos.txt", "r") as file:
                print(f"vehiculos registrados del año actual: ")
                for linea in file:
                    print(linea)
        else:
            print("Aún no hay registros.\n")
            return
"""
vehiculo1 = Vehiculo("kjdf", 2025, 2025, "kdfd", "ljan")
vehiculo2 = Vehiculo("nmap", 2016, 2016, "qsc", "bnd")
Vehiculo.mostrar()
"""

# 5. _________________________________________________


class Encuesta():

    lista_ciudades = []

    def __init__(self, edad, genero, ciudad, opinion):

        self.edad = edad
        self.genero = genero
        self.ciudad = ciudad
        self.opinion = opinion
        self.guardar()

    
    def guardar(self):

        if (self.ciudad + ".txt") in self.lista_ciudades:
            with open(f"{self.ciudad}.txt", "a") as file:
                file.write(f"{self.edad}, {self.genero}, {self.ciudad}, {self.opinion}\n")

        else:
            with open(f"{self.ciudad}.txt", "a") as file:
                 file.write(f"{self.edad}, {self.genero}, {self.ciudad}, {self.opinion}\n")

            self.lista_ciudades.append(f"{self.ciudad}.txt")

    @classmethod
    def estadistica_por_genero(cls):

        edad_total_M = 0
        edad_total_F = 0
        total_M = 0
        total_F = 0

        for ciudades in cls.lista_ciudades:
            with open(ciudades, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    
                    genero = datos[1].strip()
                    edad = int(datos[0].strip())

                    if genero == "M":
                        edad_total_M += edad
                        total_M += 1
                    elif genero == "F":
                        edad_total_F += edad
                        total_F += 1

                        total_F += 1
        
        print(f"El promedio de edad para el genero masculino es {edad_total_M / total_M}\n El promedio de edad para el genero femenino es {edad_total_F / total_F}\n")
        
    @classmethod
    def mostrar(cls):

        for ciudades in cls.lista_ciudades:
            with open(ciudades, "r") as file:
                for linea in file:
                    print(linea)

"""
encuesta1 = Encuesta(10, "M", "Pereira", "Solo lobo sur")
encuesta1 = Encuesta(20, "M", "Pereira", "...")
encuesta2 = Encuesta(21, "F", "Medellin", "...")
Encuesta.mostrar()
Encuesta.estadistica_por_genero()
"""

# 6. _________________________________________________

class NotaMusical():

    def __init__(self, nombre, frecuencia, duracion):

        self.nombre = nombre
        self.frecuencia = frecuencia
        self.duracion = duracion
        self.guardar()
        self.ejecucion()

    def guardar(self):

        if self.frecuencia > 350:
            with open("notasmusicales.txt", "a") as file:
                file.write(f"{self.nombre}, {self.frecuencia}, {self.duracion}\n")

    def ejecucion(self):
        print(f"nota: {self.nombre}, sonido: {self.nombre}")

# nota1 = NotaMusical("Do", 389, 5)


# 7. _________________________________________________

class AgendaContactos():

    def __init__(self, nombre, telefono, correo, direccion):

        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    @staticmethod
    def guarda_contacto():

        print("Por favor ingres la siguiente información: ")
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")
        direccion = input("Direccion: ")

        nuevo_contacto = AgendaContactos(nombre, telefono, correo, direccion)
         
        with open("contactos.txt", "a") as file:
            file.write(f"{nuevo_contacto.nombre}, {nuevo_contacto.telefono}, {nuevo_contacto.correo}, {nuevo_contacto.direccion}\n")

    @staticmethod
    def buscar_contacto():

        buscar = input("Ingrese el contacto a buscar: ")

        with open("contactos.txt", "r") as file:

            for contacto in file:
                datos = contacto.strip().split(",") 
                if buscar == datos[1].strip():
                    print(f"Información del contacto: {contacto}")

"""
AgendaContactos.guarda_contacto()
AgendaContactos.buscar_contacto()
"""

# 8. _________________________________________________

class Triangulo():

    lista_triangulos = []

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c 
       
    @staticmethod
    def guardar():

        print("Ingrese la longitud de los lados del triangulo: ")
        a = int(input("Lado a: "))    
        b = int(input("Lado b: "))
        c = int(input("Lado c: "))
        nuevo_triangulo = Triangulo(a, b, c)

        Triangulo.lista_triangulos.append(nuevo_triangulo)
        Triangulo.calculos()
    
    @staticmethod
    def calculos():

        for triangulo in Triangulo.lista_triangulos:

            a, b, c = triangulo.a, triangulo.b, triangulo.c
            perimetro = a + b + c
            s = perimetro / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 

            if a == b == c:
                tipo = "equilátero"
            elif a == b or b == c or a == c:
                tipo = "isósceles"
            else:
                tipo = "escaleno"

        print(f"El triangulo es de tipo {tipo}, área: {area: .2f}, perimetro: {perimetro}")

"""
Triangulo.guardar()
"""

# 9. _________________________________________________ 

class Empleado:
    def __init__(self, nombre, id_empleado, departamento, salario_base, bonificacion=0, descuento=0):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.departamento = departamento
        self.salario_base = salario_base
        self.bonificacion = bonificacion
        self.descuento = descuento

    def calcular_salario_neto(self):
        return self.salario_base + self.bonificacion - self.descuento


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def generar_reporte_departamento(self, departamento):
        archivo = f"reporte_{departamento}.txt"
        with open(archivo, "w") as file:
            file.write(f"Reporte del departamento: {departamento}\n")
            
            for emp in self.empleados:
                if emp.departamento == departamento:
                    file.write(f"{emp.nombre} - Salario neto: {emp.calcular_salario_neto()}\n")

    def generar_reportes_todos(self):
        departamentos = set(emp.departamento for emp in self.empleados)
        for dep in departamentos:
            self.generar_reporte_departamento(dep)

"""
e1 = Empleado("Ana", 1, "Ventas", 2000, bonificacion=300, descuento=100)
e2 = Empleado("Luis", 2, "Ventas", 2200, bonificacion=200, descuento=50)
e3 = Empleado("Marta", 3, "TI", 2500, bonificacion=500, descuento=200)

empresa = Empresa("MiEmpresa")
empresa.agregar_empleado(e1)
empresa.agregar_empleado(e2)
empresa.agregar_empleado(e3)

empresa.generar_reportes_todos()
"""

# 9. _________________________________________________ 


class SistemaNotas:
    def __init__(self):
        self.estudiantes = []  # cada estudiante será un diccionario

    def agregar_estudiante(self, nombre, notas):    
        self.estudiantes.append({"nombre": nombre, "notas": notas})

    def promedio_por_materia(self, materia):     
        total = 0
        contador = 0
        for est in self.estudiantes:
            if materia in est["notas"]:
                total += est["notas"][materia]
                contador += 1
        return total / contador if contador > 0 else 0

    def guardar_mejores(self, archivo="mejores.txt"):
        if not self.estudiantes:
            return
        
        promedios = []
        for est in self.estudiantes:
            notas = list(est["notas"].values())
            promedio = sum(notas) / len(notas)
            promedios.append((est["nombre"], promedio))

        with open(archivo, "w") as f:
            f.write("Mejores estudiantes:\n")
            for nombre, prom in promedios[:3]:
                f.write(f"{nombre} - Promedio: {prom:.2f}\n")
        print(f"Archivo '{archivo}' con los mejores estudiantes.")



