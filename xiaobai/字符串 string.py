""" 字符串 """
# 如何使用字串、字串的用法

# 换行符 \n
print("Hello \nMr.White")

# 字串中有双引号  \"
print("Hello\" Mr.White")

# 两个字串相加
print("Hello " + "Mr.White")

phrase = "Hello "
print(phrase + "Mr.White")

# 全部变为小写字母函数  lower()
phrase = "Hello Mr.White"
print(phrase.lower())

# 全部变为大写字母函数 upper()
print(phrase.upper())

# 判断是否全是大写，是则返回 True，否则返回 false
print(phrase.isupper())

# 判断是否全是小写，是则返回 True，否则返回 false
print(phrase.islower())

# 列子： 先将字符全部转换为小写，然后检查是否全是小写
print(phrase.lower().islower())  # 正确 返回True 

# 中括号用法
phrase = "Hello Mr.White"
#         0123456
print(phrase[0])  

# 查找函数 index()  返回最前面的位数
print(phrase.index("l"))

# 替换函数 replace("X","Y")    X 被 y 替换
print(phrase.replace("H","h"))
