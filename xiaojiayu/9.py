""" 练习 """

# score = float(input("请输入你的分数:"))

# if score >=90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 60:
#     print("C")
# elif score < 60:
#     print("D")
# else:
#     print("输入错误")

""" 三元操作符 """
# x,y = 4,5
# if x < y :
#     small = x
# else:
#     small = y
# print(small)

# # 可以改进为：
# small = x if x < y else y
# print(small)

""" 断言 assert """
assert 3 > 4

# 当这个关键字后面的条件为假的时候，程序自动崩溃并抛出AssertionError的异常
# 一般来说我们可以用Ta在程序中置入检查点，当需要确保程序中的某个条件一定为真才能让程序正常工作的话，assert关键字就非常有用了