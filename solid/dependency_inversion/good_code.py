class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


class Engine:
    def start(self):
        pass


class GasolineEngine(Engine):
    def start(self):
        print("Gasoline engine started")


class ElectricEngine(Engine):
    def start(self):
        print("Electric engine started")


if __name__ == '__main__':
    my_car = Car(GasolineEngine())
    my_car.start()
