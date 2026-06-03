from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    def drive(self):
        print("Driving........")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

    def fuel_type(self):
        print(" petrol.")

class ElectricCar(Vehicle):
    def start_engine(self):
        print("Electric car powered on.")

    def fuel_type(self):
        print(" electric.")

c = Car()
c.start_engine()
c.drive()
c.fuel_type()   
e = ElectricCar()
e.start_engine()
e.drive()
e.fuel_type()



