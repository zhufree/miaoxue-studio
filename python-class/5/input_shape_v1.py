import turtle

shape = input('请输入要画的形状：1.圆/2.正方形/3.三角形：')

if shape == '1':
	turtle.circle(100)
elif shape == '2':
	# 正方形
	turtle.fd(100)
	turtle.rt(90)
	turtle.fd(100)
	turtle.rt(90)
	turtle.fd(100)
	turtle.rt(90)
	turtle.fd(100)
	turtle.rt(90)
elif shape == '3':
	# 三角形
	turtle.fd(100)
	turtle.rt(120)
	turtle.fd(100)
	turtle.rt(120)
	turtle.fd(100)
	turtle.rt(120)
