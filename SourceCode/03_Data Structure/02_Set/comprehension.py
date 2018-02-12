# comprehension

# # [POINT 1]
# myList = [0, 1, 2, 2, 3, 3, 3]
#
# mySet = {x for x in myList if x % 2 != 0}
# print(mySet)

# [POINT 2]
myList = [0, 1, 2, 2, 3, 3, 3]

mySet = set([x for x in myList if x % 2 == 0])
print(mySet)
