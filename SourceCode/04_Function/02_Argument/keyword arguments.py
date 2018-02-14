# keyword arguments

# [POINT 1]
def myFunction1(input='Tom'):

    myString = input

    return myString

myString1 = myFunction1()
print(myString1)

# [POINT 2]
def myFunction2(input='Tom'):

    myString = input

    return myString

myString2 = myFunction2('Frank')
print(myString2)
