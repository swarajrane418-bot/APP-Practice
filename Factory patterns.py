class Car:
    def drive(self):
        print("Car is driving.")

class Bike:
    def drive(self):
        print("Bike is riding.")

vehicle_type = input("Enter vehicle type (car/bike): ")

if vehicle_type.lower() == "car":
    vehicle = Car()
elif vehicle_type.lower() == "bike":
    vehicle = Bike()

vehicle.drive()