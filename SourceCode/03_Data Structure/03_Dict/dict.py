# dict

# [POINT 1]
myDict = {'Name': 'Frank', 'ID': 123, 'Schedule': {'Monday': '9:00-18:00', 'Tuesday': '14:00-22:00'}}

print(type(myDict))
print(myDict)
print(myDict['ID'])

# [POINT 2]
myDict = {'Name': 'Frank', 'ID': 123, 'Schedule': {'Monday': '9:00-18:00', 'Tuesday': '14:00-22:00'}}

print(myDict.get('k3', 'v0'))

# [POINT 3]
myDict = {'Name': 'Frank', 'ID': 123, 'Schedule': {'Monday': '9:00-18:00', 'Tuesday': '14:00-22:00'}}

print(len(myDict))
