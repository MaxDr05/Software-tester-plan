from functools import reduce


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(str1):
    def a(x,y):
        return x * 10 + y
    
    def tonum(x):
        return DIGITS[x]

    return reduce(a,map(tonum,str1))

print(type(str2int("19999999")))
