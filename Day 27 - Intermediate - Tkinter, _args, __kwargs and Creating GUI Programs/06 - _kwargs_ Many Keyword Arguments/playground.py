def add(*args):
    a = 0
    for n in args:
        a += n
    return a

print(add(3, 4, 5, 6, 7, 8, 9))

def calculate(n, **kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add= 3, multiply= 5)