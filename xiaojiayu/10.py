""" while 循环 """
# while 条件:
#     循环体


""" for 循环 """
# favourite = "fishC"
# for i in favourite:
#     print(i,end= " ")

""" len 计算内容长度 """
# member = ["小甲鱼","小布丁","黑夜","迷途","怡静"]
# for i in member:
#     print(i,len(i))  #len() 计算内容长度
# 输出结果为：
# 小甲鱼 3
# 小布丁 3
# 黑夜 2
# 迷途 2

""" range() 的使用"""
# print(list(range(0,5)))

""" range() 和 for 使用 """
# for i in range(5):
#     print(i)

# 下面讲输出2-8
# for i in range(2,9):
#     print(i)

# 使用步进参数 会打印 1 3 5 7 9
# for i in range(1,10,2):
#     print(i)

""" break 和 continue """
# 例
bingo = "小甲鱼是帅哥"
answer = input("请输入小甲鱼最想听的一句话:")
while True:
    if answer == bingo:
        break
    answer = input("抱歉，错了，请重新输入（答案正确才能退出游戏！ :)")
print("哎呦，帅哦~")
print("您真是小甲鱼肚子里的蛔虫啊^_^")