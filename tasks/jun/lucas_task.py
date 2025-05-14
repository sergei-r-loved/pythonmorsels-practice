

# def lucas(n):
#     list = [2, 1]

#     for i in range(2, n + 1):
#         list.append(list[i-2] + list[i-1])

#     return list[n]

# print(lucas(100))

a, b = 2, 1
a, b = b, a+b

# def lucas(n):
#     lucas_num = {'a': 2, 'b': 1}

#     for i in range(n):
#         lucas_num['a'], lucas_num['b'], = lucas_num.get('b'), lucas_num.get('a') + lucas_num.get('b')
        # print(lucas_num['b'])
def fibo(a=2,b=1,upto=4000000):
    while a+b<upto:
        a,b = b,a+b
        yield b




