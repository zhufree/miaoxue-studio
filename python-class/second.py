import random 
w = random.randint(0,100)
t = int(input('请输入一个数字：'))
while t != w:
  if t < w:
    t = int(input('低了继续输入：'))
  else:
    t = int(input('高了继续输入：'))
print('对了，不用再输了')