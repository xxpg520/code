""" 档案的读取、写入 """

# 打开档案方式
# open("档案的路径",mode = "开启模式")
"""  路径 """
# 绝对路径 ex : C:/Users/xxpg/Desktop/xiaobai/123.txt
# 相对路径 以程序的位置做延伸 ex: 123.txt
""" 模式 读取、覆写、添加"""
# mode = "r" 读取
# mode = "w" 覆写
# mode = "a" 在原先资料的后面加内容
""" 打开档案的列子 """
# file = open("C:/Users/xxpg/Desktop/xiaobai/123.txt",mode = "r") # 用读取模式打开123.txt 将内容存入file变量
# file = open("123.txt",mode = "r") 

""" 打印方法 """
# 1.
# print(file.read()) #打印file中存放的内容
# 2.
# print(file.readline()) #打印file中存放的内容 一行
# print(file.readline()) #打印file中存放的内容 一行
# 3.
""" 如果读取多行可以用for控制 """
# for line in file:
#     print(line)

# print(file.readlines()) # 结果为 ['77\n', '78\n', '79\n', '80\n', '81\n', '82']

""" 覆写 """
# file = open("123.txt",mode = "w",encoding= "utf-8") # 此处模式为覆写
# # file.write("hello") #此时123.txt中内容被替换hello

# # 写入中文显示乱码，需要在打开时加入第三个参数 参考30行
# file.write("你好") # 档案被修改成  ���



""" 关闭档案，减少资源占用 """
# 1 关闭
# file.close() #关闭打开档案，减少资源占用

# 2 不用关闭的语法 
with open("123.txt",mode = "w",encoding= "utf-8") as file:
    file.write("\n哈哈")
