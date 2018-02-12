# encapsulation

# [POINT 1]
class Animal:

    def __init__(self, animalType):
        print('Initial Animal Object')
        self.__animalType = animalType

    def getType(self):
        return self.__animalType

    def setType(self, animalType):
        self.__animalType = animalType

a = Animal('Mammals')

print(a.__animalType)
print(a.getType())

a.setType('Reptiles')
print(a.getType())
