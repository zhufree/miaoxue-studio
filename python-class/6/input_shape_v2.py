import turtle

shape = input('请输入要画的形状：1.圆/2.正方形/3.三角形：')
size = input('请输入多边形的边长或圆的半径：')

if size.isdigit():
    size = int(size)
    if shape == '1':
        turtle.circle(size)
    elif shape == '2':
        # 正方形
        turtle.fd(size)
        turtle.rt(90)
        turtle.fd(size)
        turtle.rt(90)
        turtle.fd(size)
        turtle.rt(90)
        turtle.fd(size)
        turtle.rt(90)
    elif shape == '3':
        # 三角形
        turtle.fd(size)
        turtle.rt(120)
        turtle.fd(size)
        turtle.rt(120)
        turtle.fd(size)
        turtle.rt(120)
    else:
        print('请输入正确的编号')
else:
    print('输入的不是数字')
