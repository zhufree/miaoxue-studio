grade = [78, 65, 86, 91, 95, 77, 50, 79, 88, 66, 89, 93]
count_A = 0
count_B = 0
count_C = 0
count_D = 0
count_E = 0
for i in grade:
	if i < 60:
		print("E")
		count_E += 1
	elif i < 70:
		print("D")
		count_D += 1
	elif i < 80:
		print("C")
		count_C += 1
	elif i < 90:
		print("B")
		count_B += 1
	else:
		print("A")
		count_A += 1
print(f'成绩为A的学生有{count_A}人')
print(f'成绩为B的学生有{count_B}人')
print(f'成绩为C的学生有{count_C}人')
print(f'成绩为D的学生有{count_D}人')
print(f'成绩为E的学生有{count_E}人')