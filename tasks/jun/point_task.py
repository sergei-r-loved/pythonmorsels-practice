# The Point class must accept 3 values on initialization (x, y, and z) and have x, y, and z attributes. 
# It must also have a helpful string representation. 
# Additionally, point objects should be comparable to each other 
# (two points are equal if their coordinates are the same and not equal otherwise).


class Point():

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Point(self.x * other, self.y * other, self.z * other)
    
    # def __rmul__(self, other):
    #     return self.__mul__(other)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

p1 = Point(1, 1, 3)
p2 = Point(1, 2, 4)
print(p1 == p2)
p2.x = 4
print(p1 == p2)
print(p2)
p3 = p2 + p1
print(p3)  
p2 = p2 * 3
print(p2)
x, y, z = p2
print((x, y, z))
