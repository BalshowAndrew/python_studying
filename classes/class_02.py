# наследование от родительского класса
class Car():
    def explain(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

# Проверим, наследован ли один класс от другого:
if issubclass(Yugo, Car):
    print("Класс Yugon унаследован от класса Car")
else:
    print("Класс Yugo не наследован от класса Car")
    
give_me_a_car = Car()
give_me_a_yugo = Yugo()
print(give_me_a_car.explain())
print(give_me_a_yugo.explain())

