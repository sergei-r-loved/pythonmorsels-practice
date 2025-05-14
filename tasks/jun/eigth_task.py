matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

# [[3, -3], [-3, 3]]

# def add(matrix1, martrix2):
#     result_matrix = []
#     for i in range(len(matrix1)):
#         for k in matrix1[i], martrix2[i]:
            
#     # return print(result_matrix)



# add(matrix1, matrix2)

fruits = ["loquat", "jujube", "pear", "watermelon", "apple"]
colors = ["brown", "orange", "green", "pink", "purple"]

# for fruit, color in zip(fruits, colors):
#     print(fruit, color)

def add(matrix1, matrix2):
    return [
        [n+m for n, m in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)

    ]

print(add(matrix1, matrix2))
