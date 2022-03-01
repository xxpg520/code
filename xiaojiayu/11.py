""" 列表：一个打了激素的数组 """
# """ 
# 可以存入
# 整数
# 浮点数
# 字符串
# 对象
#  """
""" ------------------------------------------------- """
# 创建一个列表
# member = ['小甲鱼',"小不丁","黑夜","迷途","怡静"]
# print(member)

# number = [1,2,3,4,5]
# print(number)

# mix = [1,'小甲鱼',3.14,[1,2,3]]
# print(mix[0])

# empty = []
# print(empty)
""" -------------------向列表添加元素------------------------------- """
# 向列表尾部添加
#  append() 添加
member = ['小甲鱼',"小不丁","黑夜","迷途","怡静"]
print(member)
member.append("福禄娃娃")
print(len(member))  # len 给列表计数

# 尝试添加多个-----产生错误
# member.append("竹林小溪","Crazy迷恋")
# print(len(member)) 

# extend([]) 添加。原则是用列表扩充列表
member.extend(["竹林小溪","Crazy迷恋"])
print(member)

# insert(位置,内容) 指定位置进行添加
member.insert(0,"牡丹")
print(member)