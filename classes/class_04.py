# Добавление метода:
class Car():
    def exclaim(self):
        print("I'm a Car!")
        

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!")
    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()

try:
    give_me_a_car.need_a_push()
except:
    print("AttributeError: 'Car' object hap no attribute 'need_a_push'")
    
