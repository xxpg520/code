""" 类别class、物件object """
# 定义一个物件 object
class Phone:
    def __init__(self,os,number,is_waterproof):  # 定义类 确定有哪些参数 self 为物件本身。 os、number 等为参数
        self.os = os                            # self.os = os 用来调用传入参数的时候确定参数位置
        self.number = number
        self.is_waterproof = is_waterproof

# 创建第一台手机 传入参数
phone1 = Phone("ios",123,True)
print(phone1.os)
print(phone1.number)
print(phone1.is_waterproof)
print()
phone2 = Phone("android",456,False)
print(phone2.os)
print(phone2.number)
print(phone2.is_waterproof)
