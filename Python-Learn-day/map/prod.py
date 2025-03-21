from functools import reduce

def prod(L):
    def mul(x,y):
        return x * y
    return reduce(mul,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('1!')
else:
    print('2!')