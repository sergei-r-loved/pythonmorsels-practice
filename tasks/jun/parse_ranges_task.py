

import re


def parse_ranges(ranges_string):

    for value in ranges_string.split(","):
        range_start, sep, range_end = value.partition("-")
        if re.findall(r'\b[\w.]+->[\w.]+\b', value):
            yield int(range_start)
        else:
            if range_end:
                yield from range(int(range_start), int(range_end)+1)
            else:
                yield int(range_start)





# # print(parse_ranges('0-0, 4-8, 20-20, 43-45')) # [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
# # numbers = parse_ranges('0, 100-10000')
# # print(next(numbers))
# # print(next(numbers))
# # print(next(numbers))
numbers = list(parse_ranges('0,4-8,20->exit,43-45'))

print(numbers)