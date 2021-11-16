class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.__weight = 2

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

    def walk(self):
        print('walk')


class Fish(Animal):
    def swim(self):
        print('swim')


m = Mammal()
# m.eat()
# m.walk()
# print(m.__dict__)
f = Fish()
# print(f.__dict__)
# print(isinstance(m, Mammal))
# print(isinstance(m, Animal))
# print(isinstance(m, object))
# print(issubclass(Mammal, Animal))
# print(issubclass(Mammal, object))
print(m.age)
print(m.weight)

# Multiple Inheritance


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
