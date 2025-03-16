import math
def quadratic(a, b, c):
    result1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
    result2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)
    return result1,result2

print('quadratic(2,3,1) =',quadratic(2,3,1))
print('quadratic(1,3,-4) =',quadratic(1,3,-4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('FALSE')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('FALSE')
else:
    print('TURE')