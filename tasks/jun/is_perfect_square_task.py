from math import sqrt
from decimal import Decimal

def is_perfect_square(number: int) -> bool:
    if number <= 0:
        return False
    x = sqrt(number)
    if Decimal(x) % 1 == 0:
        return True
    return False

print(is_perfect_square(4))
print(is_perfect_square(5776))
print(is_perfect_square(35))
print(is_perfect_square(4624000000000000))