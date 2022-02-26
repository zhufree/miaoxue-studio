import turtle
import random
interval = 5
start_radius = 80
for i in range(7):
	turtle.lt(90)
	cur_raduis = start_radius + i*interval
	turtle.color((random.random(), random.random(), random.random()))
	turtle.circle(cur_raduis, 180)
	turtle.lt(90)
	turtle.penup()
	turtle.fd(cur_raduis*2+interval)
	turtle.pendown()

input()