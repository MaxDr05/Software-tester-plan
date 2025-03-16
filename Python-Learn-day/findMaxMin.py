#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    #考虑空值
    if not L:
        return (None, None)
    
    #最大
    numMax = L[0]
    for num in L:
        if numMax < num:
            numMax = num
    
    #最小
    numMin = L[0]
    for num in L:
        if numMin > num:
            numMin = num

    return (numMin, numMax)

# 测试
if findMinAndMax([]) != (None, None):
    print('1!')
elif findMinAndMax([7]) != (7, 7):
    print('1!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('1!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('1!')
else:
    print('2!')