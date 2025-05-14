# data = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 4
data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}


def pluck(data, *keys, sep='.', default=""):
    if len(keys) == 1:
        keys = keys.split(f'{sep}')
        value = None
        try:
            if len(keys) == 1:
                return data[keys]
            else:
                for key in keys:

                    if type(value) is dict:
                        value = value[key]
                    else:
                        value = data[key]

                return value
        except KeyError:
            if default is None:
                return default
            elif len(str(default)) > 0:
                return default
            raise KeyError
#     keys = (key.split(f'{sep}') for key in keys)
#     value = None
#     result = []
#     for key in keys:
#         try:
#             if len(key) == 1:
#                 value = data[key[0]]
#                 result.append(value)
#             else:
#                 for son_key in key:
#                     if type(value) is dict:
#                         value = value[son_key]
#                     else:
#                         value = data[son_key]

#                 result.append(value)
#         except KeyError:
#             if default is None:
#                 return default
#             elif len(str(default)) > 0:
#                 return default
#             raise KeyError
        
#     return tuple(result)

# pluck(data, 'y.z', default=0)
print(pluck(data, 'category.name', 'amount'))
# ('Music', 10.64)

