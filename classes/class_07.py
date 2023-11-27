#  Миксины
class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


t = Thing()

t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
print(t.dump())
