# Множественное наследвание:
class Animal:
    def says(self):
        return "I speak!"


class Horse(Animal):
    def says(self):
        return "Neigh!"


class Donkey(Animal):
    def says(self):
        return "Hee-haw!"


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


print(Mule.mro())
print(Hinny.mro())

mule = Mule()
hinny = Hinny()

print(mule.says())
print(hinny.says())
