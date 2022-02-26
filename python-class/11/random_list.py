import random

size = int(input("请输入列表长度: "))
l = []
for i in range(size):
	l.append(random.randint(0, 100))

print(l)
print(random.choice(l))