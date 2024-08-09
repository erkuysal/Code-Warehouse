import time


def timed(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        process = func(*args, **kwargs)
        stop = time.time()
        fname = func.__name__
        print(f"{fname} took {stop - begin} seconds to execute.")
        return process

    return wrapper

@timed
def random_func(x):
    result = 1
    for i in range(x):
        result += i

    return result


print(random_func(5))