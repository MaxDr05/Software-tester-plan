#在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else

list1 = [x * x for x in range(1,11) if x * x % 2 == 0]
print(list1)

d = {'x': 'A', 'y': 'B', 'z': 'C' }

#利用列表表达式快速写出一个列表
list2 = [k + "=" + v for k,v in d.items()]
print(list2)