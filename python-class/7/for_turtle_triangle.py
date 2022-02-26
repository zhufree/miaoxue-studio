import turtle

# old
turtle.fd(100)
turtle.rt(120)
turtle.fd(100)
turtle.rt(120)
turtle.fd(100)
turtle.rt(120)

# new
for _ in range(0, 3):
    turtle.fd(100)
    turtle.rt(120)