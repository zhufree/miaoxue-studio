import turtle

l = input('边长:')
count = input('边数:')
if l.isdigit() and count.isdigit():
    l = int(l)
    count = int(count)
    degree = 360/count
    for _ in range(0, int(count)):
        turtle.fd(l)
        turtle.rt(degree)