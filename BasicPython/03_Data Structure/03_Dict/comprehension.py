# comprehension

# [POINT 1]
myDict = {'Name': 'Frank', 'ID': 123, 'Schedule': {'Monday': '9:00-18:00', 'Tuesday': '14:00-22:00'}}

dictItems = myDict.items()
print(dictItems)

myList1 = [(key, value) for key, value in myDict.items()]
print(myList1)

# [POINT 2]
myDict = {'Name': 'Frank', 'ID': 123, 'Schedule': {'Monday': '9:00-18:00', 'Tuesday': '14:00-22:00'}}

dictKeys = myDict.keys()
print(dictKeys)

myList2 = [key for key in myDict.keys()]
print(myList2)

# [POINT 3]
myDict = {'Name': 'Frank', 'ID': 123, 'Schedule': {'Monday': '9:00-18:00', 'Tuesday': '14:00-22:00'}}

dictValues = myDict.values()
print(dictValues)

myList3 = [value for value in myDict.values()]
print(myList3)
