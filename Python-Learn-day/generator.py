#目的：学习generator
#日期：2025-3-17 23：28
#文件内容：写一个斐波那契数列的生成器

def fobnia(n):
    cnt = 0
    a,b = 0,1
    while cnt < n:
        yield(b)
        a , b = b , a+b
        cnt += 1
    return "Done"

f = fobnia(6)

for num in f:
    print(num)
