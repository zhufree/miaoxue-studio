prompt = "输入一些内容，系统将原样返回给你(键入 'q' 结束此程序运行。)\n"
message = ''
while message != 'q':
    message = input(prompt)
    print(message)
