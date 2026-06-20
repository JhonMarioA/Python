import csv
# HERENCIA MÚLTIPLE

# 1) ________________________________________________________________

class PersonalUniversitario:
    def __init__(self, nombre, carrera_estudiada, año_de_inicio, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.carrera_estudiada = carrera_estudiada
        self.año_de_inicio = año_de_inicio

    def antiguedad(self):
        print(f"La antiguedad de la entidad es {2025 - self.año_de_inicio} años")


class Profesor(PersonalUniversitario):
    def __init__(self, tipo_de_profesor, horas_mensuales, categoria, **kwargs):
        super().__init__(**kwargs)
        self.tipo_de_profesor = tipo_de_profesor
        self.horas_mensuales = horas_mensuales
        self.categoria = categoria

    def calcular_sueldo(self):
        if self.tipo_de_profesor == "Planta":
            sueldo = 6000000
        elif self.tipo_de_profesor == "Catedra":
            sueldo = 60000 * self.horas_mensuales
        else:
            sueldo = 12000 * self.horas_mensuales

        print(f"El sueldo de la entidad es {sueldo}")
        return sueldo

    def materias_asignadas(self):
        materias_por_categoria = {
            "Auxiliar": ["Matemáticas Básicas", "Álgebra", "Cálculo I"],
            "Asistente": ["Programación I", "Estructuras de Datos", "Bases de Datos"],
            "Asociado": ["Inteligencia Artificial", "Optimización", "Redes"],
            "Titular": ["Investigación Avanzada", "Seminario de Doctorado", "Metodología"]
        }
        return materias_por_categoria.get(self.categoria, [])

    def mostrar_materias(self):
        print(f"Materias de {self.nombre} ({self.categoria}): {self.materias_asignadas()}")


class Alumno(PersonalUniversitario):
    def __init__(self, materia_favorita, medio_de_transporte, **kwargs):
        super().__init__(**kwargs)
        self.materia_favorita = materia_favorita
        self.medio_de_transporte = medio_de_transporte


class ProfesorAyudante(Profesor, Alumno):
    def __init__(self,
                 nombre, carrera_estudiada, año_de_inicio,
                 tipo_de_profesor, horas_mensuales, categoria,
                 materia_favorita, medio_de_transporte,
                 tipo_de_monitoria):
   
        super().__init__(
            nombre=nombre,
            carrera_estudiada=carrera_estudiada,
            año_de_inicio=año_de_inicio,
            tipo_de_profesor=tipo_de_profesor,
            horas_mensuales=horas_mensuales,
            categoria=categoria,
            materia_favorita=materia_favorita,
            medio_de_transporte=medio_de_transporte
        )
        self.tipo_de_monitoria = tipo_de_monitoria


profesorayudante1 = ProfesorAyudante(
    "Carlos", "Física", 2020,
    "Monitor", 140, "Titular",
    "Física", "Carro", "Laboratorio"
)
"""
profesorayudante1.antiguedad()   
profesorayudante1.calcular_sueldo()    
profesorayudante1.mostrar_materias()  
print("Materia favorita:", profesorayudante1.materia_favorita)
print("Medio de transporte:", profesorayudante1.medio_de_transporte)
print("Tipo de monitoría:", profesorayudante1.tipo_de_monitoria)
"""

# 2) ________________________________________________________________

# Modelando dispositivos / tecnología

class Hardware:
    def __init__(self, material, peso, **kwargs):
        super().__init__(**kwargs)
        self.material = material
        self.peso = peso

    def to_dict(self):
        return {
            "material": self.material,
            "peso": self.peso
        }


class Software:
    def __init__(self, sistema_operativo, ram, **kwargs):
        super().__init__(**kwargs)
        self.sistema_operativo = sistema_operativo
        self.ram = ram

    def to_dict(self):
        return {
            "sistema_operativo": self.sistema_operativo,
            "ram": self.ram
        }


class Celular(Hardware, Software):
    def __init__(self, camara, numero, **kwargs):
        super().__init__(**kwargs)
        self.camara = camara
        self.numero = numero

    def tomar_foto(self):
        print("Tomando foto...")

    def enviar_mensaje(self):
        print(f"Enviando mensaje desde {self.numero}.")

    def cargar(self):
        print("Cargando celular...")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "camara": self.camara,
            "numero": self.numero
        })
        return data


class Portatil(Hardware, Software):
    def __init__(self, camara, targeta_grafica, **kwargs):
        super().__init__(**kwargs)
        self.camara = camara
        self.targeta_grafica = targeta_grafica

    def programar(self):
        print("Programando: print('Hello world')")

    def editar_video(self):
        print("Editando un video MP4.")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "camara": self.camara,
            "targeta_grafica": self.targeta_grafica
        })
        return data


class Xiaomi(Celular):
    def __init__(self, modelo, precio, **kwargs):
        super().__init__(**kwargs)
        self.modelo = modelo
        self.precio = precio

    def carga_rapida(self):
        print("Activando carga rápida.")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "modelo": self.modelo,
            "precio": self.precio,
            "tipo": "Xiaomi"
        })
        return data


class Asus(Portatil):
    def __init__(self, modelo, precio, **kwargs):
        super().__init__(**kwargs)
        self.modelo = modelo
        self.precio = precio

    def bloquear_pantalla(self):
        print("Bloqueando pantalla del portátil Asus.")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "modelo": self.modelo,
            "precio": self.precio,
            "tipo": "Asus"
        })
        return data


xiaomi1 = Xiaomi(
    material="Plástico",
    peso="120gr",
    sistema_operativo="Android",
    ram=8,
    camara="48px",
    numero="320131345",
    modelo="Redmi Note 13",
    precio="1.000.000"
)

asus1 = Asus(
    material="Aluminio",
    peso="1.5kg",
    sistema_operativo="Windows 11",
    ram=16,
    camara="720p",
    targeta_grafica="RTX 3050",
    modelo="ZenBook",
    precio="5.000.000"
)


xiaomi1.carga_rapida()
xiaomi1.tomar_foto()
xiaomi1.enviar_mensaje()

asus1.programar()
asus1.editar_video()
asus1.bloquear_pantalla()

# Guardar en CSV
dispositivos = [xiaomi1, asus1]

fieldnames = set()
for d in dispositivos:
    fieldnames.update(d.to_dict().keys())
fieldnames = list(fieldnames)  # convertir a lista

with open("dispositivos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for d in dispositivos:
        writer.writerow(d.to_dict())
