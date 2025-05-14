# Создай класс Temperature, который:
# хранит температуру в градусах Цельсия (celsius)
# имеет свойства:
# .celsius (по умолчанию возвращает как есть)
# .fahrenheit (переводит в °F)
# имеет строковое представление:
# str(t) → "25°C"
# repr(t) → Temperature(celsius=25.0)

# Добавь два @classmethod, которые создают объект из:
# градусов по Фаренгейту
# Пример: Temperature.from_fahrenheit(77) → celsius=25.0
# строки
# Пример: Temperature.from_string("86°F") или Temperature.from_string("30°C")
# Если строка не в формате — выбрасывать ValueError.

class Temperature():
    def __init__(self, celsius) -> None:
        self._celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f: float) -> 'Temperature':
        c = (f - 32) * 5 / 9
        return cls(c)

    @classmethod
    def from_string(cls, s: str) -> 'Temperature':
        s = s.strip().upper()
        if s.endswith("°C"):
            c = float(s[:-2])
            return cls(c)
        elif s.endswith("°F"):
            f = float(s[:-2])
            return cls.from_fahrenheit(f)
        else:
            raise ValueError("Invalid temperature format. Use '30°C' or '86°F'")

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * (9/5)) + 32

    def __str__(self) -> str:
        return f"{self.celsius}°C"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(celsius={self.celsius})"
    

t1 = Temperature(25)
print(t1.fahrenheit)     # 77.0
print(str(t1))           # "25.0°C"
print(repr(t1))          # "Temperature(celsius=25.0)"

t2 = Temperature.from_fahrenheit(86)
print(t2.celsius)        # 30.0

t3 = Temperature.from_string("100°F")
print(t3.celsius)        # 37.78...

Temperature.from_string("hello")  # ValueError
