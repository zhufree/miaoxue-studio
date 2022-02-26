import random

num = random.randint(0, 100)
while True:
    guess_num = int(input('请输入一个数字：'))
    if guess_num == num:
        print('你猜对了！')
        break
    elif guess_num > num:
        print('猜大了')
    else:
        print('猜小了')