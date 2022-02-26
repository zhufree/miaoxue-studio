student_dict = {}
student_list = []
print('please input student info:')
while True:
	cmd = input('cmd:')
	if cmd == 'q':
		break
	elif cmd == 'i':
		name = input('Input name:')
		class_ = input('Input class:')
		age = input('Input age:')
		student_list.append({
			'name': name,
			'age': age,
			'class': class_
		})
		student_dict[name] = {
			'age': age,
			'class': class_
		}
	elif cmd == 'o':
		print('name|age|class')
		print('==============')
		for i in student_list:
			print(i['name'], i['age'], i['class'])
			print('-------------')
		# for i in student_dict.keys():
		# 	print(i, student_dict[i]['age'], student_dict[i]['class'])
		# 	print('-------------')
