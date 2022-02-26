sum_ = 0
while True:
    num = input('请输入一个数字（输入0退出）：')
    if int(num) == 0:
        break
    else:
        sum_ += int(num)
        print(sum_)
