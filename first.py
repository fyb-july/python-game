# Author Fyb
# 用七彩颜色画圆
# api具体用法请见 https://docs.python.org/zh-cn/3/library/turtle.html#turtle-methods
import turtle as t
import random
t.pensize(3)
t.speed(100)
t.penup()
t.goto(0, 0)
t.pendown()
# tracer直接跳过过程到结尾
# t.tracer(False)
t.bgcolor('black')
r, g, b = 0, 0, 0
for i in range(180):
    r = random.random()
    g = random.random()
    b = random.random()
# 随机色
    t.pencolor(r, g, b)
    t.forward(200)
    t.backward(200)
    t.right(2)
t.down()
