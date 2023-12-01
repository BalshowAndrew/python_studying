# Доступ к атрибутам
# Прямой доступ
class Duck:
    def __init__(self, input_name):
        self.name = input_name


fowl = Duck('Daffy')
print(fowl.name)
print()


# Геттеры и сеттеры
class Duck2:
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('Inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('Inside the setter')
        self.hidden_name = input_name


don = Duck2('Donald')
print(don.get_name())
print()
print(don.set_name('Dona'))
print()
print(don.get_name())


