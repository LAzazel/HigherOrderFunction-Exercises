def iterate(obj, callback):
    for key, value in obj.items():
        callback(key, value, obj)

def store(value):
    def inner():
        return value
    return inner

def contract(func, *types):
    def wrapper(*args):
        for arg, type in zip(args, types[:-1]):
            if not isinstance(arg, type):
                raise TypeError
        res = func(*args)
        if not isinstance(res, types[:-1]):
            raise TypeError
        return res
    return wrapper


obj = {
    'a': 1,
    'b': 2,
    'c': 3,
}
read = store(5)
value = read()
add = lambda x, y: x + y
add_numbers = contract(add, int, int, int)


iterate(obj, lambda key, value, obj: print({'key': key, 'value': value}))
print(value)
print(add_numbers(1, 2))