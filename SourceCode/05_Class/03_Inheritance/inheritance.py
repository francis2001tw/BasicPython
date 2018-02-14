# inheritance

# [POINT 1]
class Animal:

    def __init__(self, canFly=False):
        self.canFly = canFly

    def fly(self):
        if self.canFly:
            print("I can fly!")
        else:
            print("I can not fly!")

class Dog(Animal):

    def bark(self):
        print("Woof!")

d = Dog()
d.fly()
d.bark()
