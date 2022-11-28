def add(*args):
    a = 0
    for n in args:
        a += n
    return a

print(add(3, 4, 5, 6, 7, 8, 9))