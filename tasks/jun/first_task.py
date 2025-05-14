# "# Даны две переменные: 
a = 'python'
b = 'all the love in the world'
c = ''

# Поменять переменные a и b местами
a,b = b,a 

# Перевернуть строку b

# for char in reversed(b):
#     c += char
# print(c)

# optimal

# print(b[::-1])

# Конвертировать обе строки в списки и обратно

a = [char for char in a]
b = (list(b))
# a = "".join(str(char) for char in a)

# Вернуть общее для двух списков элементов
general = set(a) & set(b)

# Убрать дубликаты из списка b

b_without_duplicates = set(b)

# Сделать из 2х списков словарь. Сделать ""а"" список ключом, ""b"" - значением
result_dict = dict(zip(a, b))
print(result_dict)

