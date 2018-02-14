# increase operators

# [POINT 1]
myList = ['python3', int(10), 'Frank', float(2.718)]

myList.append('A')
print(myList)

myList.insert(1, int(20))
print(myList)

# [POINT 2]
myList = ['python3', int(10), 'Frank', float(2.718)]

myList.extend(['B'])
print(myList)

myList.append(['B'])
print(myList)
