""" 编码为 UTF-8 可以使用中文变量 """
# 小甲鱼 = "我的天"
# print(小甲鱼)

""" 出现用户输入错误的类型的时候，提醒用户重新输入 """
# temp = input("请输入一个数字:")
# print(temp.isdigit())
    
""" 判断闰年 """
number = None
while number != 0:
    number = input("请输入一个年份：")
    if number.isdigit():
        number = int(number)
        if number % 4 == 0 and number %100 != 0 or number % 400 == 0:
            print("是润年")
        else:
            print("该年份不是润年")
    else:
        print("请输入正确的数字：")
# elif number % 400 == 0:
#     print("该年份是闰年")
# else:
#     print("该年份不是闰年")