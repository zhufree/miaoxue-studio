import turtle

# old
turtle.fd(100)
turtle.rt(144)
turtle.fd(100)
turtle.rt(144)
turtle.fd(100)
turtle.rt(144)
turtle.fd(100)
turtle.rt(144)
turtle.fd(100)
turtle.rt(144)

# new
for _ in range(0, 5):
    turtle.fd(100)
    turtle.rt(144)