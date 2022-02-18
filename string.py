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
