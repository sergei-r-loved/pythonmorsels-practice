

def group_by(sequence, *, key_func=None):
    result_dict = {}
    for number in sequence:
        key = key_func(number) if key_func else number
        if key in result_dict.keys():
            result_dict[key].append(number)
        else:
            result_dict[key] = [number]
    return result_dict


numbers = [1, 4, 5, 6, 8, 19, 34, 55]
def mod3(n): return n % 3
print({1: [1, 4, 19, 34, 55], 2: [5, 8], 0: [6]})
print(group_by(numbers, key_func=mod3))
print(group_by([1, 2, 1, 3, 2, 1]))