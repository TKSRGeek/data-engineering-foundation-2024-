# 2. __init__ is a constructor which allow us to create variables in class.

'''In Python, a constructor is a special method that is called when an instance (object) of a class
is created. The constructor method is
defined using the __init__ method. It allows you to initialize the object's attributes with specific values when the object is created.
'''

'''The primary use of a constructor is to initialize the attributes of a class when an object is created. 
This ensures that the object is in a valid state right from the start.'''
class Person:
    def __init__(self):
        # 👇 Instance Variables
        self.name = "Jordan"
        self.age = 20
        self.location = "USA"

    def user_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Location: {self.location}")


jordan = Person()
jordan.user_info()
