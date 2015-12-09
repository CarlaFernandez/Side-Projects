#-------------------------------------------------------------------------------
# Name:        while_programs
# Purpose:     Python program to test several while programs which
#              perform arithmetic operations
#
# Author:      carla
#
# Created:     09/12/2015
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


#----------------------FUNCTIONS--------------------#

def sum(x1, x2):
    x3 = 0
    while x2 != x3:
        x1+=1
        x2-=1
    return x1

def substract(x1, x2):
    x3 = 0
    while x2 != x3:
        x1-=1
        x2-=1
    return x1

def multiply(x1, x2):
    x3 = x1
    while x2 != 0:
        x1= sum(x1,x3)
        x2-= 1
    x1 -= x3
    return x1

def divide(x1,x2):
    x1 += 1
    x3 = 0
    x4 = 0
    while x1 > x3:
        x4 += 1
        x1 = substract(x1,x2)
    x1 = x4 - 1
    return x1

def mod(x1,x2):
    x1 += 1
    x3 = 0
    x4 = 0
    while x1 > x3:
        x4 = x1
        x1 = substract(x1,x2)

    x1 = x4-1
    return x1

def pow2(x1):
    x2 = 1 # current number
    x3 = 0 # current power
    while x3 != x1:
        x3 += 1
        x2 = sum(x2, x2)
    x1 = x2
    return x1

def factorial(x1):
    x2 = 1
    x3 = 0
    while x1 != x3:
        x3 += 1
        x2 = multiply(x2, x3)
    x1 = x2
    return x1

def log(x1):
    x2 = 0
    x3 = 0
    while x1 != x3:
        x1 = x1 / 10
        x2 += 1
    x1 = x2 - 1
    return x1

def sum_factorial(x1):
    x1 += 1
    x2 = 0
    x4 = 0
    while x1 != x2:
        x3 = factorial(x2)
        x4 = x4 + x3
        x2 += 1
    x1 = x4
    return x1

def divMod(x1,x2):
    '''This function performs the operation:
        y / (x % y)'''
    x3 = 0
    x4 = 0
    x6 = x2
    while x6 > x3:
        x5 = mod(x1,x2)
        x6 = substract(x6,x5)
        x4 += 1
    x1 = x4
    return x1

#------------------END OF FUNCTIONS--------------------#
