import json
import xlrd
from xlutils.copy import copy
import sqlite3


def json_2_excel():
    read_book = xlrd.open_workbook("applications.xls")
    write_book = copy(read_book)
    sheet = write_book.get_sheet(0)
    with open('application.json', 'r', encoding='utf-8') as json_file:
        data = json.loads(json_file.read())
        sheet.write(0, 0, '学生姓名')
        sheet.write(0, 1, '课程名')
        sheet.write(0, 2, '学生班级')
        sheet.write(0, 3, '学生校区')
        sheet.write(0, 4, '电话号码')
        sheet.write(0, 5, '班主任')
        row = 1
        for i in data:
            sheet.write(row, 0, i['studentName'])
            sheet.write(row, 1, i['class']['name'])
            sheet.write(row, 2, i['studentClass'])
            sheet.write(row, 3, i['studentSchool'])
            sheet.write(row, 4, i['phoneNumber'])
            sheet.write(row, 5, i['headTeacher'])
            row += 1
    write_book.save('applications_100.xls')

def sqlite_2_excel():
    read_book = xlrd.open_workbook("applications.xls")
    write_book = copy(read_book)
    sheet = write_book.get_sheet(0)
    sheet.write(0, 0, 'id')
    sheet.write(0, 1, '学生姓名')
    sheet.write(0, 2, '课程名')
    sheet.write(0, 3, '学生班级')
    sheet.write(0, 4, '学生校区')
    sheet.write(0, 5, '电话号码')
    sheet.write(0, 6, '班主任')
    # 传入数据库路径，db.s3db或者test.sqlite
    conn=sqlite3.connect('E:/chuangxi-class/.tmp/data.db')
    c=conn.cursor()
    mysel=c.execute("select studentName, class, studentClass, studentSchool, phoneNumber, headTeacher from applications")
    _id = 1
    for i, row in enumerate(mysel):
        sheet.write(i+1, 0, _id)
        _id = _id + 1
        for j, value in enumerate(row):
            if j == 1:
                #replace class name
                sheet.write(i+1, j+1, get_class_name(value))
            else:
                sheet.write(i+1, j+1, value)
    write_book.save('applications.xls')


def get_class_name(_id):
    if _id == 'undefined':
        return '无'
    else:
        conn=sqlite3.connect('E:/chuangxi-class/.tmp/data.db')
        c=conn.cursor()
        mysel=c.execute("select name from classes where id = {}".format(_id))
        for i in mysel:
            return i


def set_style(name='宋体', height=220, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 定义具体的字体
    font.color_index = 4  # 定义字体颜色
    font.height = height  # 定义字体大小  220就是11号字体，基数20*号数，11号字体就是20*11=220
    style.font = font  # 最终把自定义的字体，定义到风格里面
    
    alignment = xlwt.Alignment()  # 设置字体在单元格的位置
    alignment.horz = xlwt.Alignment.HORZ_CENTER  
    # 水平方向 居中：HORZ_CENTER  左对齐：HORZ_LEFT  右对齐：HORZ_RIGHT
    alignment.vert = xlwt.Alignment.VERT_CENTER  
    # 垂直方向 居中：VERT_CENTER  顶部对齐：VERT_TOP  底部对齐：VERT_BOTTOM
    style.alignment = alignment
    
    border = xlwt.Borders()  # 给单元格加框线
    border.left = xlwt.Borders.THIN  # 左
    border.top = xlwt.Borders.THIN  # 上
    border.right = xlwt.Borders.THIN  # 右
    border.bottom = xlwt.Borders.THIN  # 下
    border.left_colour = 0x40  # 设置框线颜色，0x40是黑色
    border.right_colour = 0x40
    border.top_colour = 0x40
    border.bottom_colour = 0x40
    style.borders = border
    
    return style

def class_name_excel(school_name):
    '''生成班级名单表'''
    read_book = xlrd.open_workbook("{}名单.xls".format(school_name))
    class_sheets = read_book.sheets()
    for s in class_sheets:
        filename = "{}班级名单.xls".format(s.name)
        if os.path.exists(filename):
            os.remove(filename)
        book = Workbook(encoding='utf-8')
        worksheet = book.add_sheet('Sheet 1')
        worksheet.write_merge(0, 0, 0, 3, '{}班级名单'.format(s.name),set_style(height=260))
        worksheet.col(0).width = 220*5
        worksheet.col(2).width = 220*7
        worksheet.col(3).width = 220*15
        worksheet.write(1, 0, '序号', set_style())
        worksheet.write(1, 1, '姓名', set_style())
        worksheet.write(1, 2, '班级', set_style())
        worksheet.write(1, 3, '电话号码', set_style())

        # 保存Excel book.save('path/文件名称.xls')
        book.save(filename)
        write_book = copy(xlrd.open_workbook(filename, formatting_info=True))
        sheet = write_book.get_sheet(0)
        
        row_count = s.nrows
        for i in range(1, row_count):
            sheet.write(i+1, 0, i, set_style('Arial'))
            sheet.write(i+1, 1, s.cell_value(i, 2), set_style())
            sheet.write(i+1, 2, s.cell_value(i, 3), set_style())
            sheet.write(i+1, 3, s.cell_value(i, 5), set_style())
        write_book.save("{}班级名单.xls".format(s.name))


if __name__ == '__main__':
    # sqlite_2_excel()
    # json_2_excel()
    for i in [
    '万家', 
    '濮家', 
    '笕新'
    ]:
        # poster(i)
        class_name_excel(i)