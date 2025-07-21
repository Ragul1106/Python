from abc import ABC, abstractmethod

# Base abstract class
class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, daily_rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.daily_rate = daily_rate
        self.is_rented = False

    @abstractmethod
    def calculate_rent(self, days):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} {self.brand} (ID: {self.vehicle_id}) - ₹{self.daily_rate}/day"

# Bike class
class Bike(Vehicle):
    def calculate_rent(self, days):
        return self.daily_rate * days * 0.9  

# Car class
class Car(Vehicle):
    def calculate_rent(self, days):
        return self.daily_rate * days  

# Customer class
class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_vehicles = []

    def __str__(self):
        return f"Customer: {self.name}"

# Rental class manages renting and returns
class Rental:
    total_rentals = 0

    @staticmethod
    def rent_vehicle(customer: Customer, vehicle: Vehicle, days: int):
        if vehicle.is_rented:
            print(f"{vehicle} is already rented.")
        else:
            cost = vehicle.calculate_rent(days)
            vehicle.is_rented = True
            customer.rented_vehicles.append(vehicle)
            Rental.total_rentals += 1
            print(f"{customer.name} rented {vehicle} for {days} days. Total cost: ₹{cost}")

    @staticmethod
    def return_vehicle(customer: Customer, vehicle: Vehicle):
        if vehicle in customer.rented_vehicles:
            vehicle.is_rented = False
            customer.rented_vehicles.remove(vehicle)
            print(f"{customer.name} returned {vehicle}. Thank you!")
        else:
            print("This vehicle was not rented by the customer.")

    @classmethod
    def show_total_rentals(cls):
        print(f"Total rentals made: {cls.total_rentals}")



"""
# Create vehicles
bike1 = Bike("B101", "Yamaha", 300)
car1 = Car("C202", "Honda", 1200)

# Create customer
ragul = Customer("Ragul")

# Rent operations
Rental.rent_vehicle(ragul, bike1, 3)   
Rental.rent_vehicle(ragul, car1, 2)    

# Return bike
Rental.return_vehicle(ragul, bike1)

# Show total rentals
Rental.show_total_rentals()
"""