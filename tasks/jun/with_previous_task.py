



def with_previous(secuence, *, fillvalue=None):
    previous = fillvalue
    for i in secuence:
        yield (i, previous)
        previous = i

# list(with_previous("hello"))
# print(with_previous([1, 2, 3]))
print(next(with_previous([1, 2, 3])))
# list(with_previous(n**2 for n in [1, 2, 3]))
# [('h', None), ('e', 'h'), ('l', 'e'), ('l', 'l'), ('o', 'l')]
# [('h', None), ('e', 'h'), ('l', 'e'), ('l', 'l'), ('o', 'l')]
