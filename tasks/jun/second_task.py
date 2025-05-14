# Дан список:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Написать цикл который выводит числа из списка a
# for i in a:
#     print(i)


# Как можно выводить эти же числа без списка (без хранения значений в памяти)
# for i in range (1, 11):
#     print(i)
# Как можно написать простую генераторную функцию, которая принимает целое число n и генерирует числа от 1 до n включительно.
def generator_for_n(n):
    for i in range(1, n+1):
        yield i

# Создать собственный итератор, определить класс, реализующий методы __iter__() и __next__().

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

it = MyIterator(1, 4)
for num in it:
    print(num)
# Напишите генераторную функцию fibonacci, которая будет генерировать числа Фибоначчи. Дополнительно создайте функцию take, которая принимает генератор и количество элементов, и возвращает список из первых N элементов генератора.