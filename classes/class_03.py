# 01 Переопределение методов:
class Car():
    def explaim(self):
        print("I'm a Car")
        

class Yugo(Car):
    def explaim(self):
        print("I'm a Yugo!")


give_me_a_car = Car()
give_me_a_yugo = Yugo()


print(give_me_a_car.explaim())
print(give_me_a_yugo.explaim())

# 02 Переопределение методов:
class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name
        

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"
        

person = Person('Fodd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
print(doctor.name)
print(lawyer.name)
