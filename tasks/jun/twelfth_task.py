


def uniques_only(iterable):
    for i in dict.fromkeys(iterable).keys():
        yield i
