

def compact(sequence):
    _sentinel = object()
    for elem in sequence:
        if elem != _sentinel:
            _sentinel = elem
            yield elem



# print(compact([1, 1, 2, 2, 3, 2])) # [1, 2, 3, 2]
# print(compact([None, 0, "", []]), [None, 0, "", []])
# print(compact([None, 0, "", []]))