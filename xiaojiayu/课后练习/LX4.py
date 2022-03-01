# # 参考答案
# temp = input('请输入一个整数:')
# number = int(temp)
# i = 1
# while number:
#     print(i)
#     i = i + 1
#     number = number - 1

# # 我的答案
# number = int(input("请输入一个整数："))
# add = 0 
# while add != number:
#     add += 1
#     print(add)

# # 参考答案
# number = int(input('请输入一个整数:'))
# while number:
#     i = number - 1
#     while i:
#         print(' ', end = '')
#         i = i - 1
#     j = number
#     while j:
#         print('*', end = '')
#         j = j - 1
#     print()
#     number = number - 1

# # 我的答案 不完美，最后一行可以发现前面有空格
# number = int(input("请输入一个整数："))
# add = "*"
# while number:
#     number -= 1
#     print(" " * (number-1),add * number)

# 抄一遍例子，总结
number = int (input('请输入一个整数：'))
while number:  #主循环体
    i = number -1  #i变量用来控制" " 此处直接-1 就不会多一个空格
    while i:
        print(' ',end = "")  # end="" 为了控制循环不会换行
        i -= 1     #用来控制循环" "中空格数量
    j = number      #j 用来控制 * 号的数量
    while j:
        print("*",end = '')
        j -= 1
    number -= 1
    print()     # 用来换行