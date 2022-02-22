""" 建立一个计算器 """
# 可以计算加减乘除
num1 = float(input("请输入第一个数："))
op = input("请输入运算符号：")
num2 = float(input("请输入第二个数："))

if op == "+" :
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("不支持的运算") 
