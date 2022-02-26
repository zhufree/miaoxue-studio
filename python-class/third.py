import random
num = random.randint(0,100)

while True:
  player=int(input("从1至100中输入一个数字"))
  if num!=player:
    if num<player:
      print("往小了猜")
    if num>player:
      print("往大了猜")
  else:
    print("猜对了大聪明")
    break