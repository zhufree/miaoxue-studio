import random

select = input('1.今天吃什么\n2.计算BMI\3.Collatz序列')
if select.isdigit():
    if int(slelect) == 1:
        lottery()
    elif int(slelect) == 2:
        func2()
    elif int(slelect) == 3:
        func3()

def lottery():
    option = random.choice(['上上签',''])
    pass

def BMI():
    # (bmi = weight / height2)
    # if bmi <= 18.5 return "Underweight"
    # if bmi <= 25.0 return "Normal"
    # if bmi <= 30.0 return "Overweight"
    # if bmi > 30 return "Obese"
    pass

def collatz():
    pass