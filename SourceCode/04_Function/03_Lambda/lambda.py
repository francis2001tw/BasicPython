# lambda

# # [POINT 1]
# myList = [(1, 'D'), (2, 'C'), (3, 'B'), (4, 'A')]
# printFirstElement = lambda data: data[0]
# print(printFirstElement(myList))
# print(printFirstElement(myList[0]))

# [POINT 2]
myList = [(1, 'D'), (2, 'C'), (3, 'B'), (4, 'A')]
myList.sort(key=lambda data: data[1])
print(myList)
