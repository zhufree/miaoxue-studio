import random
input('请想好一个1-100内的数字，按回车键计算机开始猜：')
guess_num = random.randint(0,100)
max_num = 100
min_num = 0
while True:
    guess_react = input(f'计算机猜的数是{guess_num}，输入0表示小了，2表示大了，1表示猜对：')
    if guess_react == '1':
        print('计算机猜对了！')
        break
    elif guess_react == '2':
        if max_num > guess_num:
            max_num = guess_num
        guess_num = int((max_num + min_num)/2)
        print('猜大了')
    else:
        if min_num < guess_num:
            min_num = guess_num
        guess_num = int((max_num + min_num)/2)
        print('猜小了')
