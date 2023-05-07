# SRP (Single Responsibility Principle)
The Single Responsibility Principle (SRP) is a software design principle that states that a class, module, funciton or other entity should have only one reason to change or one responsibility. In other words, a class, module, funciton or other entity should have only one job or responsibility and it should do it well.

<br>

## Bad Code
    class Car:
        def __init__(self, model, year, engine_capacity):
            self.model = model
            self.year = year
            self.engine_capacity = engine_capacity

        def start_engine(self):
            # code to start the engine
            pass

        def stop_engine(self):
            # code to stop the engine
            pass

        def drive(self, destination):
            # code to drive the car to the destination
            pass

        def park(self):
            # code to park the car
            pass
        
<br>

## Good Code
    class Car:
        def __init__(self, model, year, engine_capacity):
            self.model = model
            self.year = year
            self.engine_capacity = engine_capacity

        def start_engine(self):
            # code to start the engine
            pass

        def stop_engine(self):
            # code to stop the engine
            pass


    class Driver:
        def __init__(self, name, age, driving_license):
            self.name = name
            self.age = age
            self.driving_license = driving_license

        def drive_car(self, car, destination):
            # code to drive the car to the destination
            pass


    class ParkingLot:
        def __init__(self, location, capacity):
            self.location = location
            self.capacity = capacity

        def park_car(self, car):
            # code to park the car
            pass
