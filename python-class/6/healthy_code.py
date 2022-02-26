address1 = 'wuhan'
address2 = 'beijin'
address3 = 'shanghai'

a = input('请输入健康码: red/yellow/green')
b = input('请输入行程码: out/in')
c = input('请输入是否戴口罩: yes/no')

address = input('请选择你要去的地址: shanghai/beijin/wuhan')

if address == address1: 
    if a != 'green' or c == 'no' or b == 'out_of_province':
        print('抱歉, 您不满足要求无法通行. ')
    else:
        print('请通过')

if address == address2: 
    if a != 'green' or c == 'no':
        print('抱歉, 您不满足要求无法通行.')
    else :
      print('请通过')

if address == address3: 
    if a != 'green' or c == 'no':
        print('抱歉, 您不满足要求无法通行.')
    else :
        print('请通过')