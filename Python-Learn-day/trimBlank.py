def trim(s):
    cnt = 0
    #考虑空值传入
    if s == "":
        return s
    
    for letter in s:
        #去除前置空格
        if letter == ' ':
            cnt += 1
            if cnt == len(s):
                return ""
        else:
            s = s[cnt:]
            cnt = len(s)
            break

    for letter in s[::-1]:
        #去除后置空格
        if letter == ' ':
            cnt -= 1
        else:
            s = s[:cnt]
            break
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('11!')
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
    print('2!')