""" 2维列表、巢状循环 """
# row = 行
# column = 列
nums = [
    [[0,1,2]],
    [[3,4,5]],
    [[6,7,8]],
    [[9]]
]

# 第一个[0]行  第二个[0]列
# print(nums[3][0])

for row in nums:
    for col in row:
        print(col)