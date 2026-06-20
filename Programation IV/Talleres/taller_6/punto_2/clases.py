import csv
# 2) ________________________________________________________________

# Modelando dispositivos / tecnología

class Hardware:
    def __init__(self, material, peso, **kwargs):
        super().__init__(**kwargs)
        self.__material = material
        self.__peso = peso

    def get_material(self):
        return self.__material
    
    def get_peso(self):
        return self.__peso

    def to_dict(self):
        return {
            "material": self.get_material(),
            "peso": self.get_peso()
        }


class Software:
    def __init__(self, sistema_operativo, ram, **kwargs):
        super().__init__(**kwargs)
        self.__sistema_operativo = sistema_operativo
        self.__ram = ram
    
    def get_sistema_operativo(self):
        return self.__sistema_operativo
    
    def get_ram(self):
        return self.__ram

    def to_dict(self):
        return {
            "sistema_operativo": self.get_sistema_operativo(),
            "ram": self.get_ram()
        }


class Celular(Hardware, Software):
    def __init__(self, camara, numero, **kwargs):
        super().__init__(**kwargs)
        self.__camara = camara
        self.__numero = numero

    def tomar_foto(self):
        print("Tomando foto...")

    def enviar_mensaje(self):
        print(f"Enviando mensaje desde {self.get_numero()}.")

    def get_camara(self):
        return self.__camara
    
    def get_numero(self):
        return self.__numero

    def cargar(self):
        print("Cargando celular...")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "camara": self.get_camara(),
            "numero": self.get_numero()
        })
        return data


class Portatil(Hardware, Software):
    def __init__(self, camara, targeta_grafica, **kwargs):
        super().__init__(**kwargs)
        self.__camara = camara
        self.__targeta_grafica = targeta_grafica

    def programar(self):
        print("Programando: print('Hello world')")

    def editar_video(self):
        print("Editando un video MP4.")

    def get_camara(self):
        return self.__camara
    
    def get_targeta_grafica(self):
        return self.__targeta_grafica

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "camara": self.get_camara(),
            "targeta_grafica": self.get_targeta_grafica()
        })
        return data


class Xiaomi(Celular):
    def __init__(self, modelo, precio, **kwargs):
        super().__init__(**kwargs)
        self.__modelo = modelo
        self.__precio = precio

    def get_modelo(self):
        return self.__modelo
    
    def get_precio(self):
        return self.__precio

    def carga_rapida(self):
        print("Activando carga rápida.")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "modelo": self.get_modelo(),
            "precio": self.get_precio(),
            "tipo": "Xiaomi"
        })
        return data


class Asus(Portatil):
    def __init__(self, modelo, precio, **kwargs):
        super().__init__(**kwargs)
        self.__modelo = modelo
        self.__precio = precio

    def bloquear_pantalla(self):
        print("Bloqueando pantalla del portátil Asus.")

    def get_modelo(self):
        return self.__modelo
    
    def get_precio(self):
        return self.__precio

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "modelo": self.get_modelo(),
            "precio": self.get_precio(),
            "tipo": "Asus"
        })
        return data




