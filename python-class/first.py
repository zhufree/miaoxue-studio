import random
num = random.randint(1,100)
time = 0
while True:
  guess = int(input("输入1到100中的一个数"))
  if guess<num:
    print("猜的太小了！")
    time+=1
  elif guess>num:
    print("猜的太大了！")
    time+=1
  else:
    print("猜对了！")
    time+=1
    print(f"你猜了{time}次才猜到！")
    break