""" for 循环 """
"""
for 变量 in 字串or列表:
    要重复执行的程序代码 """

# for letter in "小白你好":
#     print(letter)

# for num in [0,1,2,3,4]:  
#     print(num)

# 下行用range()函数展示
# for num in range(2,7): # 从2到7之间不包含7
#     print(num)
# vars = "abvfh"
# for i in vars:
#     print(i)

# 练习
# print(pow(2,6))  #2的5方
#
# num = 0
# while num <= 10 :
#     num += 1
#     if num % 2 == 0:
#         continue #跳过本次循环,继续执行下一次
#     print(num)
#     if num == 7:
#         break    #跳出循环,后面不在执行

"""
    exit() 
    quit()
用于结束当前python解释器程序的,而break和continue 是跳过
"""

# 作业联系
"""
循环输出十行十列 ♥

"""
# hang = "※"
# lie = "※"
#
# for i in range(10):
#     for y in range(9):
#         print(hang,end=" ")
#     print(lie)

# print(pow(2,6))  # 2的6次方
# 2*2*2*2*2*2


# def power(base_num,pow_num): # 定义2个变量,base_num 用来代表基数,pow_num代表次数
#     result = base_num           # 用result 保存base_num中的值2
#     for index in range(pow_num -1):     # pow_num - 1 用来控制次数 本例中 5-1   2*2*2*2*2 *符号有4个
#         result = result * base_num      #
#     return result                   # 用return返回result保存的最终结果

# print(power(2,5))                   # 打印调用函数power(2,5)结果
