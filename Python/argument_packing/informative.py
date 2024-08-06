"""
    Argument packing refers to the ability to pass a variable number of arguments to a function.

    Python provides two ways to achieve this:
        -> *args for positional arguments
        -> **kwargs for keyword arguments.
"""


# ------------ example : *args ------------
def greet(*args):               # *args allows you to pass a variable number of positional arguments to a function.
    for name in args:           # The arguments are packed into a tuple.
        print(f'Hello, {name}!')


greet('Alice', 'Bob', 'Charlie')
print("----------------------------- EXAMPLE: KWARGS ----------------------------")


# ------------ example : **kwargs ------------
def print_info(**kwargs):       # **kwargs allows you to pass a variable number of keyword arguments to a function.
    for key, value in kwargs.items():  # The arguments are packed into a dictionary.
        print(f'{key}: {value}')


print_info(name='Alice', age=30, city='New York')
print("------------------------ EXAMPLE : KWONLY ARGUMENTS --------------------------")


# ------------ example : Key Word Only Arguments ------------
def process_data(a, b, *, c, d):    # You can specify that certain arguments can only be passed by keyword.
    print(a, b, c, d)               # by placing them after a * in the function definition.


process_data(1, 2, c=3, d=4)  # Valid
# process_data(1, 2, 3, 4)    # Invalid: c and d must be passed as keyword arguments
print("----------------------- EXAMPLE : USE CASE----------------------------------")

def setup_user(name, age, location):
    print(f'{name} is {age} years old and lives in {location}.')


user_info = {'name': 'Alice', 'age': 30, 'location': 'New York'}
setup_user(**user_info)
