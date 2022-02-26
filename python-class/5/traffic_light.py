current = input('请输入当前红绿灯颜色：green/yellow/red')
if current == 'green':
    return 'yellow'
elif current == 'yellow':
    return 'red'
else:
    return 'green'