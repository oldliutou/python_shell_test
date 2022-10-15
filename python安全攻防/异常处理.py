#coding:utf-8


try:
    while (1):
        mathScore = input('数学成绩：')
        mathScore = int(mathScore)
        if(0<=mathScore<=100):
            print("输入的数学成绩为：",mathScore)
        else:
            print("输入不在本科成绩范围内。")
except Exception as e:
    print('输入的数值有误！')