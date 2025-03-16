def power(x,n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

print(power(5,3))
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

#list1 = {"city":"Beijing","job":"Engineer"}
#person('dingrui',24,**list1)

list1 = [1,2,3,4,5,6,7,8]

print(list1[::])


