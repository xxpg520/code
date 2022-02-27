""" 猜数字游戏改进 
改进要求：
1.猜错的时候提示用户当前输入比答案大了还是笑了
2.程序应该提供多次机会给用户猜测，专业点来讲就是程序需要重复运行某些代码。

"""
nice = 8
jishu = 0
guess = None
while guess != 8:
    guess = int(input("猜猜小甲鱼心里想的是什么数字："))
    
    if guess == nice:
        print("哇草，你是小甲鱼心里的蛔虫吗？")
        print("哼，猜中了也没有奖励")
    else:
        if guess > nice:
            print("哥，大了大了~~")
        else :
            print("嘿，小了！小了")
print("游戏结束，不玩了~~")