"""

Generators in Python are a type of iterable, like lists or tuples, but instead of storing all their values in memory, they generate values on the fly. This makes generators very memory efficient and suitable for large data sets or infinite sequences. Generators are written using functions and the yield keyword.

Key Features of Generators

    1.	Lazy Evaluation:
    •	Generators compute their values on the fly and yield them one at a time only when requested, rather than computing and storing all values at once.
    2.	State Retention:
    •	Each time a generator function yields a value, it retains its state so it can resume from where it left off when the next value is requested.
    3.	Single Use:
    •	Generators can be iterated over only once. After all values are generated, they are exhausted.

"""


def my_generator(n):
    for x in range(n):
        yield x ** 2


generated_values = my_generator(9999)

for i in range(10):
    print(next(generated_values))