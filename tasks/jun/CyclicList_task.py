from typing import List
class CyclicList():

    def __init__(self, sequence) -> None:
        self.sequence = sequence

    def __iter__(self):
        while True:
            yield from self.sequence
    
    def __len__(self):
        self.lenth = 0
        for _ in self.sequence:
            self.lenth += 1
        return self.lenth

    def __str__(self) -> str:
        return f"{self.sequence}"

    def append(self, new_element):
        self.sequence += [new_element]

    def pop(self, element_to_pop=None):
        self.copy_of_sequence = self.sequence
        if element_to_pop is not None:
            if element_to_pop >= 0:
                for index, _ in enumerate(self.sequence):
                    if index == element_to_pop:
                        self.sequence = self.sequence[:index] + self.sequence[index+1:]
                        return self.copy_of_sequence[element_to_pop]

            self.copy_of_sequence = self.copy_of_sequence[::-1]
            for index, _ in enumerate(self.sequence[::-1]):
                if index == abs(element_to_pop):
                    self.sequence = self.sequence[:index] + self.sequence[index+1:]
                    return self.copy_of_sequence[abs(element_to_pop)]                

        else:
            self.sequence = self.sequence[:-1]
            return self.copy_of_sequence[-1]

my_list = CyclicList([1, 2, 3, 4])
# for i, n in enumerate(my_list):
#     if i > 8:
#         break
#     print(n)

my_list.append(5)
# print(len(my_list))
print(my_list.pop())
print(my_list)
print(my_list.pop(0))
print(my_list)
print(my_list.pop(-2))

# test_list = [1, 2, 3, 5]