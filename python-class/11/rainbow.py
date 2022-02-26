import random
import turtle

turtle.colormode(255)
turtle.lt(90) # 光标朝上，这样画圆是向左画
for i in range(7):
	R = random.randint(0, 255)
	G = random.randint(0, 255)
	B = random.randint(0, 255)
	turtle.pencolor(R, G, B)
	turtle.pendown()
	turtle.circle(50 + i * 5, 180) # 画半圆，半径每次+5
	turtle.penup()
	turtle.goto(i * 5 + 5, 0) # 向右移动回到最外圈再往外5
	turtle.lt(180) # 光标朝上
