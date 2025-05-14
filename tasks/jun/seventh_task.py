def count_words(string_to_count: str):
    result = {}
    for word in string_to_count.lower().split(" "):
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result





print(count_words("oh what a day what a lovely Day"))
