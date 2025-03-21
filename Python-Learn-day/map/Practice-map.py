def normalize(name):
    cnt = 0
    tmp = ''
    for charName in name:
        if cnt == 0:
            tmp = tmp + charName.upper()
            cnt += 1
        else:
            tmp = tmp + charName.lower()
    name = tmp
    return name

    

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)