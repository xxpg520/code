""" 猜数字游戏改进 
改进要求：
1.猜错的时候提示用户当前输入比答案大了还是笑了
2.程序应该提供多次机会给用户猜测，专业点来讲就是程序需要重复运行某些代码。
3.每次程序产生的答案是随机的
"""
import random # 调用模块
nice = random.randint(1,99) #randint(1,9) 产生一个随机整数范围在1~9
guess = 0
add =3
while guess != nice and add :
    guess = input("猜猜小甲鱼心里想的是什么数字：")
    add -= 1
    if guess.isdigit():
        guess = int(guess)
        if guess == nice:
            print("哇草，你是小甲鱼心里的蛔虫吗？")
            print("哼，猜中了也没有奖励")
        else:
            if guess > nice:
                print("哥，大了大了~~")
            else :
                print("嘿，小了！小了")
    else:
        print("抱歉：您输入的数字有误")
if add == 0 :
    print("三次机会用完啦。")
print("游戏结束，不玩了~~")