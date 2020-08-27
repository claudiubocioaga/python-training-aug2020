def decorator(func):
    def inner(*args, **kwargs):
        print(f'Before calling {func}')
        return_value = func(*args, **kwargs)
        print(f'After calling {func}')
        return return_value
    return inner


@decorator
def say_hello():
    print('Hello world!')


@decorator
def greet(name, upper=False):
    if upper:
        name = name.upper()
    print(f'Hello, {name}!')


@decorator
def increment(num, step=1):
    return num + step


# say_hello = decorator(say_hello)
say_hello()

# greet = decorator(greet)
# decorator(greet)('Ana')
greet('Ana')
greet('Andrei', upper=True)


print('10 incremented by 2:', increment(10, 2))
