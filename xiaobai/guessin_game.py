""" 猜数字游戏 """
num = int (55)      # 定义谜底变量 num 类型int
guess = None        # 定义存放猜谜的变量guess,暂时为None
guess_count = 0     # 定义guess_count 计数器起始值为0
guess_limit = 3     # 定义guess_limit 计数器结束值为3
out_of_limit = False        # 定义跳出循环的条件变量
while guess != num and not(out_of_limit):  #设定循环条件 guess是否等于谜底 且 跳出循环变量out_of_limit是否为真
    guess_count += 1   # 计数器值+1 
    if guess_count <= guess_limit:      #判断计数器值guess_count是否小于等于计数器结束值
        guess = int(input("请输入你猜的数字："))
        if guess > num:     #判断输入的数字是否大于谜底值
            print("你猜的数字大了")
        elif guess < num:   #判断驶入的数字是否小于谜底值
            print("你猜的数字小了")   
    else:       #在9行不符合条件情况下
        out_of_limit = True   #赋值out_of_limit 为真,导致循环结束

if out_of_limit:        #判断循环结束条件out_of_limit是否成立,成立则输出下行
    print("抱歉，你输了")
else :                  #不成立则因为跳出循环是因为猜对结果guess == num,输出下行
    print("恭喜你赢了")
