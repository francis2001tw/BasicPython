# polymorphism

class Animal:

    def __init__(self, canFly=False):
        self.canFly = canFly

    def fly(self):
        if self.canFly:
            print("I can fly!")
        else:
            print("I can not fly!")

# [POINT 1]
class Chicken(Animal):

    def fly(self):
        print("Chicken can't fly")

class Hawk(Animal):

    def fly(self):
        print("Hawk can fly")

c = Chicken()
c.fly()

h = Hawk()
h.fly()
