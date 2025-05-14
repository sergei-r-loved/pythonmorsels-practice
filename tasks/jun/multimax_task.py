
# def max(sequence, *, key=None):
#     iterator = iter(sequence)
#     try:
#        max = key(next(iterator)) if key is not None else next(iterator)
#     except StopIteration:
#         max = 0 
#     for number in iterator:
#         if key(number) > max if key is not None else number > max:
#             max = key(number) if key is not None else number
#     return max

# def multimax(sequence, *, key=None) -> list:
#     sequence = list(sequence)
#     maximum = max(sequence, key=key)
#     return [item for item in sequence if (key(item) if key else item) == maximum]


def multimax(sequence, *, key=None) -> list:
    iterator = iter(sequence)
    try:
        first = next(iterator)
    except StopIteration:
        return []
    
    max = key(first) if key else first
    list_of_maximums = [first]

    for item in iterator:
        current_item = key(item) if key else item
        if current_item > max:
            max = current_item
            list_of_maximums =[item]
        elif current_item == max:
            list_of_maximums.append(item)
    return list_of_maximums

words = ["alligator", "animal", "apple", "artichoke", "avalanche"]
print(multimax(words, key=len))
# print(multimax([1, 4, 2, 4, 3])) # [4, 4]
# # print(max(["asd", "sdddd"], key=len))
# print(multimax(["asd", "asd", "a"], key=len))
# print(multimax(n**2 for n in range(1, 10)))