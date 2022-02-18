# 如何使用数字、数字的用法
# 整数、负数
print(-77.2)

# 加
print(8+5)
# 减
print(8-5)
# 乘
print(8*5)
# 除
print(8/5)
# 整除 小数点后不保留
print(8//5)  


# 连续运算符 先乘除后加减
print(8+8*5)

#连续运算 用()来控制先后
print((8+8)*5) 

# 变量带入运算
number = 8
print(number * 5)

# 取余数  8÷5=1……3 
print(number % 5)

# 函数  转换为字串  srt()
number = 8
print(str(number))
print("会印出数字" + str(number))

# 类型不同无法相加 会有如下贴士
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
""" print(8 + str(number)) """

# 函数 绝对值   abs()
number = -8
print(abs(number))

# 函数 次方  pow() 
print(pow(2,4))  # 2 的 4 次方

# 函数 返回最大值  max()
number = [2,3,88,100,52,11,78,111]
print(max(number))

# 函数 返回最小值  min()
print(min(number))

# 函数 四舍五入 round()
print(round(4.4))
print(round(4.6))


"""  引入更多函数 """
from math import *

# 无条件舍去小数点之后数字  floor()
print(floor(4.6))  # 4

# 无条件进位   ceil()
print(ceil(5.1))   # 6

# 开方 sqrt（）
print(sqrt(64)) # 8
