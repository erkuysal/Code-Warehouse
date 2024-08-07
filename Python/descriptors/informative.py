"""

    Descriptors are a powerful, low-level mechanism that allows you to customize attribute access in your objects.
    They are used to define and manage the behavior of attributes in classes and provide a way
    to reuse the same access logic across different classes.

    A descriptor is a class that implements any of the following methods:
        •	__get__(self, instance, owner): Used to retrieve an attribute.
        •	__set__(self, instance, value): Used to set an attribute.
        •	__delete__(self, instance): Used to delete an attribute.

"""


# Example 1: Creating a simple descriptor
# ///////////////////////////////////////| DATA DESCRIPTOR |////////////////////////////////////////////////////
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person:
    name = Typed("name", str)
    age = Typed("age", int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Example usage
p = Person("Alice", 30)
print(p.name)  # Output: Alice
print(p.age)   # Output: 30
# p.age = "thirty"  # Raises TypeError: Expected <class 'int'>


# //////////////////////////////////////////| NON-DATA DESCRIPTOR |/////////////////////////////////////////////////
class Celsius:
    def __init__(self):
        self._temperature = 0

    def __get__(self, instance, owner):
        return self

    def __set__(self, instance, value):
        self._temperature = value

    def to_fahrenheit(self):
        return (self._temperature * 9/5) + 32


class Temperature:
    celsius = Celsius()


# Example usage
t = Temperature()
t.celsius = 25  # Setting the temperature in Celsius
print(t.celsius._temperature)  # Output: 25
print(t.celsius.to_fahrenheit())  # Output: 77.0




