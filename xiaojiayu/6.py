# str() 字符串
a =str(5e19)
print(a) # 结果5e+19 会有正负符号

# int() 整数
# 浮点数转换整数直接截掉小数点后内容，不会四舍五入
b = int(5.99)
print(b)

# float() 浮点数
c =float(520)
print(c)

# tpye（）查看变量类型
print(type(a))
print(type(b))
print(type(c))


# ininstance(变量，类型) 进对比 相同返回True 不同返回false
print(isinstance(a,str))
print(isinstance(a,int))
print(isinstance(33,str))