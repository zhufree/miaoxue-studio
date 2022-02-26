import turtle

side_length = input('请输入边长')
side_length = int(side_length)

turtle.fd(side_length)
turtle.rt(90)
turtle.fd(side_length)
turtle.rt(90)
turtle.fd(side_length)
turtle.rt(90)
turtle.fd(side_length)
turtle.rt(90)

radius = input('请输入半径：')
radius = int(radius)

turtle.circle(radius)