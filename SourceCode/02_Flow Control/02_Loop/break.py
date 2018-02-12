# break

myString = 'My name is Frank'
index = -1

while index < 16:

    index = index + 1

    if index == 10:
        # [POINT 1]
        break
    else:
        print(myString[index] + '-', end='')
