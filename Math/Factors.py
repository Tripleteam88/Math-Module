'''
Python Program to find the factors of a number

This function computes the factor of the argument passed

Note: Will not use proper documentation. Atleast not yet
'''
global xList
global zList
xList = []
zList = []

def find_factors(x, lis1):
    '''
    Will find all factors of a number
    '''    
    FactLis = lis1
    for i in range(1, x + 1):
        if x % i == 0:
            FactLis.append(i)
    print("The factors of", x, 'are:', FactLis)
    return FactLis
    

def gcfLis(lis1, lis2):
    '''
    Will find the gcf in 2 lists
    '''
    cfLis = []
    if len(lis1) > len(lis2):
        l = len(lis2)
    elif len(lis2) > len(lis1):
        l = len(lis1)
    if len(lis1) == len(lis2):
        l = len(lis1)
    
    for i in range(0, l):
        if lis1[i] == lis2[i]:
            cfLis.append(lis1[i])
    
    print('The common factors are', cfLis)
    print('The greatest common factor is', cfLis[-1])

def gcf(x, y):
    '''
    Takes 2 values and finds their greatest common factor.
    '''
    cfLis = []
    if x > y:
        z = x
    elif x < y:
        z = y
    elif x == y:
        z = x

    for i in range(1, z):
        if x % i == 0 and y % i == 0:
            cfLis.append(i)

    print(cfLis)
    print(f"The greatest common factor of {x} and {y} is {cfLis[-1]}")
    return int(cfLis[-1])


#This is a first attempt at catching errors and raising exceptions
'''
try:
    if gcf(30, 90) != 30:
        raise ValueError
except ValueError:
    print("Incorrect Answer")
'''

