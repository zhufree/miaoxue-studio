if number.isdigit() and int(number) % 2 == 0:
    print(number + '是偶数')
elif number.isdigit() and int(number) % 2 != 0:
    print(number + '是奇数')
else:
    print('不是数字')