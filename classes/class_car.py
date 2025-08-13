class Car:

    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

    def start_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is starting...")

    def stop_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is stopping...")

car1 = Car("Toyota", "Camry", 2020)
car1.display_info()
car1.start_engine()
car1.stop_engine()

car2 = Car("Honda", "Civic", 2019)
car2.display_info()
car2.start_engine()
car2.stop_engine()


# Accessing class variable
print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

Car.wheels = 5  # Changing class variable

print(car1.wheels)  # Output: 5
print(car2.wheels)  # Output: 5

