# создаем самый простой класс и присваиваем атрибуты
class Cat():
    def __init__(self, name):
        self.name = name


# создаем экземпляр класса, передав строку для параметра name
furball = Cat("Grumpy")

print(furball)
print(furball.name)
