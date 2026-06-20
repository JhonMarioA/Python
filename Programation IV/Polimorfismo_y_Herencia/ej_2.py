

class Vehiculo():
    def __init__(self, marca, descripcion):
        self.marca = marca
        self.descripcion = descripcion


class Carro(Vehiculo):
    def __init__(self, marca, descripcion):
        super().__init__(marca, descripcion)


class Moto(Vehiculo):
    def __init__(self, marca, descripcion):
        super().__init__(marca, descripcion)

    
vehiculos = [Carro("Mazda", "CCCC"), Moto("Suzuki", "MMMM")]

for vehiculo in vehiculos:
    print(f"Marca: {vehiculo.marca}, Descripción: {vehiculo.descripcion}")


