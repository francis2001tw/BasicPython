# arbitrary arguments

# [POINT 1]
def myFunction1(*args):

    print(type(args))

    myString = args

    return myString

myString1 = myFunction1('My', 'name', 'is')

print(myString1)

myString1 = myFunction1('My', 'name', 'is', 'Frank')
print(myString1)

# [POINT 2]
def myFunction2(**kargs):

    print(type(kargs))

    chA = kargs.get('A')
    chB = kargs.get('B')
    chC = kargs.get('C')
    chD = kargs.get('D')

    myString = (chD, chC, chA, chB)

    return myString

myString2 = myFunction2(A='My', B='name', C='is')
print(myString2)

myString2 = myFunction2(A='My', B='name', C='is', D='Frank')
print(myString2)
