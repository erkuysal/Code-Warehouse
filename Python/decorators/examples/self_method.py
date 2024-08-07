def log_instance(func):
    def wrapper(*args, **kwargs):
        instance = func.__self__
        print(f"Method called on instance: {instance}")
        return func(*args, **kwargs)
    return wrapper


class MyClass:
    def method(self):
        print(f"Method executed on {self}")


# Create an instance
obj = MyClass()

# Bind method and apply decorator manually (normally done via @log_instance)
bound_method = log_instance(obj.method)

# Call the decorated method
bound_method()
