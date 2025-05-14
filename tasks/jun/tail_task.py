

# tail([1, 2, 3, 4, 5], 3)
# [3, 4, 5]

def tail(target, number):
    if number <= 0:
        return []

    result = [i for i in target]

    return list(result[-number:])


print(tail([1, 2, 3, 4, 5], 3))
print(tail((1, 2, 3, 4, 5), 3))

squares = (n**2 for n in range(10))
print(tail(squares, 3)) # [49, 64, 81]
