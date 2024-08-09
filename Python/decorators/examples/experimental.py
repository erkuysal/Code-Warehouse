def my_decorator(function):

    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = function(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator
def say_hello(name):
    print(f"this is print line : Hello {name}")
    return f"this is return line : Hello {name}"


print(say_hello("John"))

