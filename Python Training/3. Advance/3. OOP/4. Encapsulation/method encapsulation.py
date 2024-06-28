class Example:
    def public_method(self):
        print("This is a public method.")

    def _protected_method(self):
        print("This is a protected method.")

    def __private_method(self):
        print("This is a private method.")

# Usage
example = Example()
example.public_method()        # Accessible
example._protected_method()    # Accessible (but should be used with caution)
try:
    example.__private_method() # Not directly accessible
except AttributeError as e:
    print(e)

# Accessing private method using name mangling
example._Example__private_method()
