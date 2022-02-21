""" if 判断语句的使用  """

# if 判断语句
# 1.
# 如果 我肚子饿
#      我就去吃饭
from importlib.resources import read_binary


hungry = True
if hungry:
    print("我就去吃饭")

# 2.
# 如果 今天下雨
#       我就开车去上班
# 否则
#       我就走路去上班
rainy = False
if rainy:
    print("我就开车去上班")
else:
    print("我就走路去上班")

# 3.
# 如果 你考100分
#       我就给你1000元
# 或是如果 你考80分以上
#       我就给你500元
# 或是如果  你考60分以上
#       我就给你200元
# 否则
#       你就给我300元
score = 50
if score == 100:
    print("我给你100元")
elif score >= 80 :
    print("我给你500元")
elif 80> score >= 60 :
    print("我给你100元")
else:
    print("你给我300")

# 4.
# 如果 你考100分 且 今天下雨
#       我就给你1000元
# 否则
#       你给我100元
score = 100
rainy = True
if score == 100 and rainy :
    print("我给你1000元")
else:
    print("你给我100元")