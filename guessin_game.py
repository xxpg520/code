""" 猜数字游戏 """

num = int (55)
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False
while guess != num and not(out_of_limit):
    guess_count += 1
    if guess_count < guess_limit:
        guess = int(input("请输入你猜的数字："))
        guess_count += 1
        if guess > num:
            print("你猜的数字大了")
        elif guess < num:
            print("你猜的数字小了")
    else:
        out_of_limit = True
if out_of_limit:
    print("抱歉，你输了")
print("游戏结束") 