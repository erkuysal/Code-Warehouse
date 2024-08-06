# They are typically used to extend the functionality of existing functions without modifying their structure.

"""

    @staticmethod: Defines a static method that does not operate on an instance of the class.
    @classmethod: Defines a class method that receives the class as the first argument.
    @property: Defines a method as a property, allowing it to be accessed like an attribute.

"""


def example(func):
    def wrapper():
        print(f'--------------------- EXAMPLE: -----------------------------')
        func()
    return wrapper


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")
say_hello()


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")




