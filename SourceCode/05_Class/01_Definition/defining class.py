# defining class

# [POINT 1]
class Animal:

    def __init__(self, animalType):
        print('Initial Animal Object')
        self.animalType = animalType

    def getType(self):

        return self.animalType

a = Animal('Mammals')
animalType = a.getType()
print(animalType)
