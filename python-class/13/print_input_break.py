prompt = "输入一些内容，系统将原样返回给你(键入 'q' 结束此程序运行。)\n"
while True:
    message = input(prompt)
    if message == 'q':
        break
    else:
        print(message)
