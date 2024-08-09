def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Using the Fibonacci generator
fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))
