'''Static variables, also known as class variables, are variables that are shared among
all instances of a class. They are not tied to any specific instance, but rather
to the class itself. Static variables serve several important purposes in object-oriented programming:

Uses of Static Variables
Shared Data Across Instances:

Static variables can hold data that should be shared among all instances of a class.
For example, a counter that tracks the number of instances created.'''
class Car:
    # 👇 Static variable
    num_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        # 👇 Accessing static variable
        Car.num_cars += 1


# Creating instances of Car
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

print()

print("Number of cars created:", Car.num_cars)  # 2
