# -*- coding: utf-8 -*-
def trim(s):
    if not s:
        return s
    
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    
    if start == len(s):
        return ''
    
    end = len(s) - 1
    while end >= 0 and s[end] == ' ':
        end -= 1
    
    return s[start:end + 1]

# 测试:
if trim('hello  ') != 'hello':
    print('1!')
elif trim('  hello') != 'hello':
    print('111!')
elif trim('  hello  ') != 'hello':
    print('1111!')
elif trim('  hello  world  ') != 'hello  world':
    print('11111!')
elif trim('') != '':
    print('111111!')
elif trim('    ') != '':
    print('1!')
else:
    print('PASS!')