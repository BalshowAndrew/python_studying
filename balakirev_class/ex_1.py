# Создание класса и его атрибутов
class Point:
    color = 'red'
    circle = 2


print(f"color = {Point.color}")
Point.color = 'black'
print(f"color = {Point.color}")
print(f"circle = {Point.circle}")
print()
print(Point.__dict__)
print()

# Создаем экземпляры класса
a = Point()

print(a)
print(f"color = {a.color}, circle = {a.circle}")
print()

b = Point()

print(b)
print(f"color = {b.color}, circle = {b.circle}")
print()

print(type(a))
print(type(a) == Point)
print(isinstance(a, Point))
print('Сами объекты a и b не содержат своих атрибутов')
print(a.__dict__)
print(b.__dict__)

print('Если выполнить a.color = "green"')
a.color = 'green'
print(f"color = {a.color}")
print('В объекте a будет создано свое пространство имен:')
print(a.__dict__)


# Создаем новые атрубуты с помощью функции setattr:
setattr(Point, 'prop', 1)

print()
print(Point.__dict__)
print(Point.prop)

# Функуция getattr()
print(getattr(Point, 'a', False))
print(getattr(Point, 'color', False))

# Удаление атрибутов из класса:
del Point.prop

delattr(Point, 'circle')

# Проверка на существование атрибута:
print(hasattr(Point, 'prop'))
print(hasattr(Point, 'circle'))

