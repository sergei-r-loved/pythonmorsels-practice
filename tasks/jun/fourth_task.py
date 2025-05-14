# Задача 1: Класс с @property и __repr__
# Создай класс Rectangle, у которого:

# есть два обязательных атрибута: width и height

# есть свойство area, которое возвращает площадь

# есть свойство perimeter, которое возвращает периметр

# __repr__ возвращает строку в виде Rectangle(width=3, height=4)

# нельзя создать прямоугольник с отрицательной шириной или высотой


class Rectangle():
    def __init__(self, width: int, height: int):
        if width < 1 or height < 1:
            raise ValueError
        else:
            self.width = width
            self.height = height

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return self.height * 2 + self.width * 2
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


r = Rectangle(3, 4)
print(r.area)       # 12
print(r.perimeter)  # 14
print(r)            # Rectangle(width=3, height=4)
