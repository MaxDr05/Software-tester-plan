L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [word.lower() for word in L1 if isinstance(word,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('1!')
else:
    print('2!')