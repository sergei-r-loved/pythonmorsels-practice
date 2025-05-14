
def lstrip(sequence, object_to_except):
    sequence = [i for i in sequence]
    if len(sequence) == 0:
        return sequence
    if callable(object_to_except):
        for i in sequence:
            if not object_to_except(i):
                yield i
    else:
        for index, element in enumerate(sequence):
            if element != object_to_except:
                yield from sequence[index:]
                break
        return []







print(lstrip([0, 0, 1, 0, 2, 3], 0)) # [1, 0, 2, 3]
print(lstrip([1, 1, 1, 1], 1))
generator_1 = lstrip([1, 1, 2, 3, 1], 1) # [2, 3, 1]
print(list(generator_1))


def is_even(n): return n % 2 == 0
numbers = [1, 3, 5, 6]
print(list(lstrip(numbers, is_even)))
