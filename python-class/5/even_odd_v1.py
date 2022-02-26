number = input('请输入一个数字：')
# v1
if number.isdigit():
	if int(number) % 2 == 0:
		print(number + '是偶数')
	else:
		print(number + '是奇数')
else:
	print('不是数字')

# v2
if number.isdigit() and int(number) % 2 == 0:
	print(number + '是偶数')
elif number.isdigit() and int(number) % 2 != 0:
	print(number + '是奇数')
else:
	print('不是数字')

# v3 二元表达式
print(number + '是偶数' if number.isdigit() and int(number) % 2 == 0 else "") 