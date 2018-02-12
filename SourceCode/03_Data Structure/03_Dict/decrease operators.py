# decrease operators

# # [POINT 1]
# myDict = {'Name': 'Frank', 'ID': 123, 'Schedule': {'Monday': '9:00-18:00', 'Tuesday': '14:00-22:00'}}
# print(myDict)
#
# del myDict['ID']
# print(myDict)

# [POINT 2]
myDict = {'Name': 'Frank', 'ID': 123, 'Schedule': {'Monday': '9:00-18:00', 'Tuesday': '14:00-22:00'}}
print(myDict)

schedule = myDict.pop('Schedule')
print(schedule)
print(myDict)
