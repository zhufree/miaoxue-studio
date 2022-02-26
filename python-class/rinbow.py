import random
import turtle

turtle.colormode(255)
turtle.lt(90)
for i in range(7):
	R = random.randint(0, 255)
	G = random.randint(0, 255)
	B = random.randint(0, 255)
	turtle.pencolor(R,G,B)
	turtle.pendown()
	turtle.circle(100-i*5, 180)
	turtle.penup()
	turtle.goto(-i*5-5, 0)
	turtle.left(180)
