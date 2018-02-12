# comprehension

data1 = list()
for num in range(0, 10):
    if num % 2 == 0:
        data1.append(num)
print(data1)

# [POINT 1]
data2 = [num for num in range(0, 10) if num % 2 == 0]
print(data2)

# [POINT 2]
pairs2D = [(x, y) for x in range(2) for y in range(2)]
print(pairs2D)

pairs3D = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
print(pairs3D)
