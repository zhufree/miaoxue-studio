import turtle

t = input('draw type?')
distant = int(input('distant?'))
if t == 'line':
	turtle.fd(distant)
elif t == 'circle':
	turtle.circle(distant)
elif t == 'dot':
	turtle.fd(distant)
	turtle.dot(distant)
	turtle.fd(distant)
elif t == 'stamp':
	turtle.fd(distant)
	turtle.stamp()
	turtle.fd(distant)
input()
