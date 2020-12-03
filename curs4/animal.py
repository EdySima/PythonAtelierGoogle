class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f'animal - {self.name}: {self.age} ani'


class Cat(Animal):
    def speak(self):
        print('miua miau')

    def __str__(self):
        return f'cat - {self.name}: {self.age}'


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def speak(self):
        print('Hello!')

    def get_friends(self):
        return ', '.join(self.friends)

    def add_friends(self, friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)

    def get_age_diff(self, other):
        diff = self.age - other.age
        print(f'{abs(diff)} year difference')

    def __sub__(self, other):
        return abs(self.age - other.age)

    def __str__(self):
        return f'Persoana - {self.name}: {self.age}'


class Rabbit(Animal):
    # class variable
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rabbitID = Rabbit.tag
        Rabbit.tag += 1

    def get_rabbitID(self):
        return str(self.rabbitID)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __str__(self):
        return f'rabbit - {self.rabbitID}'

    def __eq__(self, other):
        same_parents = (self.parent1.get_rabbitID() == other.parent1.get_rabbitID()
                        and self.parent2.get_rabbitID() == other.parent2.get_rabbitID())
        opposite_parents = (self.parent1.get_rabbitID() == other.parent2.get_rabbitID()
                        and self.parent2.get_rabbitID() == other.parent1.get_rabbitID())
        return same_parents or opposite_parents


r1 = Rabbit(10)
r2 = Rabbit(20)

print(r1.get_rabbitID())
print(r2.get_rabbitID())

r3 = Rabbit(30)
r4 = Rabbit(40)

r5 = r1 + r2
r55 = r2 + r1

r6 = r3 + r4
r66 = r3 + r4

print(r5)
print(r6)

print(f'Parent 1 is {r5.get_parent1()}')
print(f'Parent 2 is {r5.get_parent2()}')

print(f'Parent 1 is {r6.get_parent1()}')
print(f'Parent 2 is {r6.get_parent2()}')

print(r5 == r55)
print(r6 == r66)

# dogo = Animal(4)
# print(dogo)
# dogo.set_name('Azorel')
# dogo.set_age(10)
# print(dogo.get_age())
# print(dogo.get_name())
# print(dogo)
#
# tom = Cat(4)
# print(tom)
#
# tom.set_name('Tom')
# print(tom)
# tom.speak()
#
#
# ion = Person('Ion', 24)
# ana = Person('Ana', 40)
# vasile = Person('Vasile', 100)
#
# print(ion)
# print(ana)
# ana.add_friends('Ion')
# ana.add_friends('Vasile')
# ana.add_friends('Maria')
# ana.add_friends('Maria')
# ana.add_friends('Maria')
# print(ana.get_friends())
# ion.speak()
#
# ion.get_age_diff(ana)
# print(ion - ana)
