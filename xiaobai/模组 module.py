""" 模组 module """
""" # 调取模组 """
# 调取自建模组
# 例1
import tool  #引入 tool模组
# 使用模组中变量
print(tool.name) #打印tool.py 中变量name对应值
print(tool.age)  #打印tool.py 中变量age对应值
# 使用模组中的函数
print(tool.max_num(33,22,98)) 
# ——————————————————————————————————————————————————
""" # 调取python模组 """
# 查询python内建模组
# python module list
# 例 引入内建模组 token 
# ===================================================
import token
# 使用模组  
print(token.AT) # token是模组名称  AT 是模组中对应的变量
# ==================================================
# 例2 印出系统存放路径 Lib为python自带模组路径
import sys
print(sys.path)
# ——————————————————————————————————————————————————
""" 调取第三方模组    需要pip套件管理工具 """
# 例 numpy 模组 先查询要下载的模组如 numpy
# 查询下载模组的命令
# ==================================================
# 在命令行 输入
# pip install numpy
# ==================================================
# 调用 numpy
import numpy
# 后面则可以调用numpy模组中的函数和变量。
#===================================================
# 给调用模组换名字
# 调用时 import numpy as np
# 则可以用 np 来代替numpy模组
