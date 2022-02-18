""" 列表 list """

score1 = 90
score2 = 70
score3 = 60
score4 = 50
score5 = 80

# 创建列表
scores = [90,70,60,50,80]
#
#  不同类型的列表
friends = ["小黑","小黄","小绿"]
things = [90,"小黑",True]

# []中第几位就打印对应的内容
print(scores[3])    # 50 

# []中负数 从后开始
print(scores[-2])   # 50

# [0:2] 从0到2位之间 不含第2位
print(scores[0:2])   # [90, 70]

# [1:4] 从1到4位之间 不含第4位
print(scores[1:4])  # [70, 60, 50]

# [1:] 从1位到结束
print(scores[1:])   # [70, 60, 50, 80]

# [:4] 等同 [0:4]
print(scores[:4])   # [90, 70, 60, 50]

""" 修改列表内容 """
# 修改第0位内容位30

scores[0] = 30
print(scores)  # [30, 70, 60, 50, 80]

# 函数 extend()   在列表后面衔接列表
scores.extend(friends) #在scores 列表 后接上 friends 列表
print(scores)

scores = [90,70,60,50,80]
# 函数 append()  在列表后面加一个值
scores.append(30)  # 在列表后面加上30这个值
print(scores)
scores.append("胖子")  # 在列表后面加上 胖子
print(scores)

scores = [90,70,60,50,80]

# 函数 insert(位置,值)   在指定位置插入一个值
scores.insert(2,30)  #[90, 70, 30, 60, 50, 80]
print(scores)

# 函数 remove(值)  删除列表中的 值
scores.remove(90)
print(scores)   # [70, 30, 60, 50, 80]

# 函数 clear() 清空列表
scores.clear()
print(scores)   # []

scores = [90,70,60,50,80]
# 函数 pop() 移除列表的最后一位
scores.pop()
print(scores)   # [90, 70, 60, 50]

# 函数 sort() 由小到大做排列
scores = [90,70,60,50,80] 
scores.sort()
print(scores) #[50, 60, 70, 80, 90]

# 函数 reverse() 将列表反转
scores = [90,70,60,50,80] 
scores.reverse()
print(scores) #[80, 50, 60, 70, 90]

# 函数 index(值) 查找值并返回所在的位数
scores = [90,70,60,50,80,60,90,60] 
print(scores.index(60)) # 2

# 函数 count(值) 找出列表中有多少个值
print(scores.count(60)) # 3

# 函数len(列表) 找出有几个值
print(len(scores))