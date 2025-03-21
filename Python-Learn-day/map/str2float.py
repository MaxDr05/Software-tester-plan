#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce

def str2float(s):

    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def a(x,y):
        return x * 10 + y
    
    def b(x,y):
        return x + y * 0.1
    
    def chr2num(x):
        return DIGITS[x]
    
    delimeter = '.'
    part1,part2,part3 = s.partition('.')

    pnum1 = reduce(a,map(chr2num,part1))
    print(pnum1)
    pnum2 = reduce(b,map(chr2num,part3))
    return pnum1+pnum2




print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('1!')
else:
    print('2!')