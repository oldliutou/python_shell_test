import requests

'''student = ["number","name","age"]
print(student)'''
# 选择结构
'''while(1):

    studentScore = int(input('Score of Students:'))
    if (studentScore == 999):
        print("结束")
        break
    elif( studentScore < 60 and studentScore>=0):
        print("不及格")
    elif(studentScore>=60 and studentScore<80):
        print("良好")

    elif(studentScore>=80 and studentScore<=100):
        print("优秀")
    else:
        print("输入不合规")'''
# 循环结构
Sum = 0
for i in range(1,101):
    Sum += i
print(Sum)
