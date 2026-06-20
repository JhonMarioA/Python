# Product
class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"Car with {self.engine} engine, {self.wheels} wheels, color {self.color}"

# Builder
class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def build(self):
        return self.car

# Director (opcional)
class Director:
    @staticmethod
    def build_sports_car():
        return (CarBuilder()
                .set_engine("V8")
                .set_wheels(4)
                .set_color("red")
                .build())

    @staticmethod
    def build_electric_car():
        return (CarBuilder()
                .set_engine("electric")
                .set_wheels(4)
                .set_color("white")
                .build())

# Uso
sports_car = Director.build_sports_car()
electric_car = Director.build_electric_car()

print(sports_car)
print(electric_car)
