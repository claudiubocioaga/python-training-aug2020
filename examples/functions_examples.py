def function(*args, **kwargs):
    print(args)
    print(kwargs, end='\n\n')


function(1, 2, 3, 4, 5, 6)
function()
function(10, 40, name='ana', age=40)
function(x=14, y=15)


def print_clone(*args, sep=' ', end='\n', flush=False):
    print(*args, sep=sep, end=end, flush=flush)


print_clone(1, 2, 3)
print_clone(10, 'ana', 'blabla', sep='*', end='\n#####\n')


def func_all_params_types(name, age, *args, step=1, **kwargs):
    print(args, name, age, step, kwargs)


func_all_params_types('test', 1, 2, 3, x='Ana', y=20)


# Argument unpacking
words = ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']
options = {'sep': ' ', 'end': '?\n'}
print(*words, **options)
# print('hello', 'hello', 'is', 'there', 'anybody', 'in', 'there', sep=' ', end='?')

print(words, options)
# print(['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there'], {'sep': ' ', 'end': '?'})
