# I want you to make a class that represents a circle.
# The circle should have a radius, a diameter, and an area. It should also have a nice string representation.
# Additionally the radius should default to 1 if no radius is specified when you create your circle:

from math import pi

class Circle:
    def __init__(self, radius=1) -> None:
        self.radius = radius
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.radius})"

    @property
    def area(self):
        return self._radius ** 2 * pi

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


a = Circle(5)
b = Circle()

print(a.radius)
print(a.diameter)
print(a.area)
a.diameter = 40
print(a.radius)
# print(b.radius)
# print(b.diameter)
# print(b.area)
# a.area = 100
# print(a.area)