# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5

bmi = weight/height**2
if bmi < 18.5:
    print("偏轻")
elif bmi <= 25.0 :
    print("正常")
elif bmi <= 28.0 :
    print("偏胖")
elif bmi <= 32.0 :
    print("肥胖")
else:
    print("过度肥胖")