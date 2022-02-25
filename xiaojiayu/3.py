from tempfile import tempdir
from wsgiref.util import guess_scheme


print("----------------猜数字---------")
guess = int(input("不妨猜猜小甲鱼现在心里想的数字:"))

if guess == 8:
    print("我草，你是小甲鱼心里的蛆虫吗？！")
    print("哼，猜中了也没有奖励！")
else:
    print("猜错了，小甲鱼现在心里想的是8！")
print("游戏结束，不玩了")