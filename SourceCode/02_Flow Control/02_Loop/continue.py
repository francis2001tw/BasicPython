# continue

myString = 'My name is Frank'
index = -1

while index < 16:

    index = index + 1

    if index % 2 == 0:
        # [POINT 1]
        continue
    else:
        print(myString[index] + '-', end='')
