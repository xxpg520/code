""" 问答程序 """
from question import Question # 只引入question 中 Question

test = [
    "1 + 3 = ？\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1公尺等于几公分？\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "香蕉是什么颜色的？\n(a) 黑色\n(b) 黄色\n(c) 白色\n\n"
]
questions = [
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1
    print("你得到" + str(score) + "分  共" + str(len(questions)) + "题")

run_test(questions)