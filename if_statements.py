""" if 判断语句的使用  """

# # if 判断语句
# # 1.
# # 如果 我肚子饿
# #      我就去吃饭
# from importlib.resources import read_binary
# from sys import flags
# from tkinter import N
# from tkinter.tix import NoteBook
# from turtle import Turtle


# hungry = True
# if hungry:
#     print("我就去吃饭")

# # 2.
# # 如果 今天下雨
# #       我就开车去上班
# # 否则
# #       我就走路去上班
# rainy = False
# if rainy:
#     print("我就开车去上班")
# else:
#     print("我就走路去上班")

# # 3.
# # 如果 你考100分
# #       我就给你1000元
# # 或是如果 你考80分以上
# #       我就给你500元
# # 或是如果  你考60分以上
# #       我就给你200元
# # 否则
# #       你就给我300元
# score = 50
# if score == 100:
#     print("我给你100元")
# elif score >= 80 :
#     print("我给你500元")
# elif 80> score >= 60 :
#     print("我给你100元")
# else:
#     print("你给我300")

# # 4.
# # 如果 你考100分 且 今天下雨
# #       我就给你1000元
# # 否则
# #       你给我100元
# score = 100
# rainy = False
# if score == 100 and rainy :
#     print("我给你1000元")
# else:
#     print("你给我100元")

# # 5.
# # 如果 你考100分 或 今天下雨
# #       我就给你1000元
# # 否则
# #       你给我100元
# score = 90
# rainy = False
# if score == 100 or rainy :
#     print("我给你1000元")
# else:
#     print("你给我100元")

# # 6.
# # 如果 你考100分 或 没有下雨
# #     我给你1000元
# # 否则
# # 你给我100元
# score = 100
# rainy = True
# if score != 100 or not(rainy):
#     print("我给你1000元")
# else:
#     print("你给我100元")

# # 练习
# # max_num
# # 输入3个数字，返回最大的数字

# max_num = None
# a = int(input("请输入第一个数字"))
# b = int(input("请输入第一个数字"))
# c = int(input("请输入第一个数字"))
# if a>b and a>c :
#     max_num = a
# elif b>a and b>c :
#     max_num = b
# else :
#     max_num = c
# print("最大的数字是：",max_num)

# 把上面练习做成函数
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(33,3,5))
>>>>>>> ac2dd20bbafdbe8cae42f5cb36e2d7d7b3dff08e
