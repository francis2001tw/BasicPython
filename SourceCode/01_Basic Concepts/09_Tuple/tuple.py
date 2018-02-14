# tuple

# [POINT 1]
myTuple = (1, 2, 3, 'A')
print(myTuple)

# [POINT 2]
myTuple = (1, 2, 3, 'A')
(a, b, c, d) = myTuple
print(a, b, c, d)

# Error: 'tuple' object does not support item assignment
# myTuple[0] = 5

# [POINT 3]
tuple1 = ('A', 'B', 'C')
print(len(tuple1))
