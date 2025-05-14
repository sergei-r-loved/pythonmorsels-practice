

def numeric_range(sequence):
    iterator = iter(sequence)
    if len(sequence) == 0:
        return 0
    try:
        min= max = next(iterator)
    except StopIteration:
        min = max = 0 
    for number in sequence:
        if number < min:
            min = number
        if number > max:
            max = number
    return max - min

print(numeric_range([10, 8, 7, 5, 3, 6, 2]))
print(numeric_range([n ** 2 for n in range(10)]))
print(numeric_range(n**2 for n in range(1, 4)))
