# Создаем класс Person:
class Person:
    name = 'Andrew'

print(Person.name)

print(Person.__name__)

print(Person.__class__)

# Создаем экземпляр класса Person:
p = Person()

print(p.__class__)
print(type(p))

# Создадим объект того же типа, что и объект p 
new_person = p.__class__()
print(new_person.__class__)

print(id(p))
print(id(new_person))
