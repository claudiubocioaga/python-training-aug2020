# Names defined on built-in level: print, float, dir
# Names defined on global level: X, func, MyClass
# Names defined on local level (function func()): a, b, inner_func
# Names defined on local level (function inner_func()): m, n
# Names defined on enclosing level (function inner_func()): a, b

X = 10


def func(a):
    # global X
    # X = 10000
    b = "bbb"

    def inner_func(m):
        # nonlocal a
        # a = 'BLA'
        n = 'nn'
        print('Call from inner_func:', m, n, a, b, X)

    inner_func('mm')
    print('Call from func:', a, b, inner_func, X)


class MyClass:
    pass


func("aaa")

print('Call from global:', dir, int, range)
print('Call from global:', X, func, MyClass)


i = None
for i in [1, 2, 3]:
    print(i)

print('i outside of for:', i)

my_var = None
if X > 50:
    my_var = 2

print('my_var outside of if:', my_var)
