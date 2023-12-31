# магические матоды:
# __init__(self) - вызывается сразу после создания экземпляра класса
# __del__(self) - вызывается непосредственно перед удалением экземпляра класса

# Инициализатор __init__(self):
class Point:
    color = 'red'
    circle = 2

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

# Используем значения параметров по умолчанию:
pt_1 = Point()
print(pt_1.__dict__)

# Задаем значения параметров при создении экземпляра класса:
pt = Point(2, 5)
print(pt.__dict__)

# Задаем значения параметров при помощи метода set_coords:
pt.set_coords(3, 8)
print(pt.__dict__)

# Финализатор __del__():
class Point2:
    color = 'red'
    circle = 2

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __del__(self):
        print("Удаление экземпляра: " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt_02 = Point2()
print(pt_02.__dict__)

