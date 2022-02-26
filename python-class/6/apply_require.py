age = int(input("请输入年龄："))
height = int(input("请输入身高："))

if age >= 18 and age <= 30 and height >= 170 and height <= 185 :
    print("恭喜，你符合报考飞行员的条件")
else:
    print("抱歉，你不符合报考飞行员的条件")