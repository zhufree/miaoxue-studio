grade = input('请输入学生成绩(0-100)：')
if grade.isdigit():
    grade = int(grade)
    if grade < 60:
        print("E")
    elif grade < 70:
        print("D")
    elif grade < 80:
        print("C")
    elif grade < 90:
        print("B")
    else:
        print("A")
else:
    print('输入的不是数字')