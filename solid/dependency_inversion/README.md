# Dependency Inversion Principle

The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules, both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

<br>

## Bad Code
    class Car:
        def __init__(self, engine):
            self.engine = engine

        def start(self):
            self.engine.start()


    class Engine:
        def start(self):
            print("Engine started")


    if __name__ == '__main__':
        my_car = Car(Engine())
        my_car.start()
        
<br>

## Good Code
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
