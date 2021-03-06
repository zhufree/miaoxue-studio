from PIL import Image, ImageDraw, ImageFont
import os
import xlrd
from xlutils.copy import copy
import xlwt
from xlwt import Workbook

class_list = {
    '万家': [], 
    '濮家': [],
    '笕新': []
}


def get_date(weekday):
    '''计算开学第一天日期'''
    if weekday == '周一':
        return '9月27日'
    elif weekday == '周二':
        return '9月28日'
    elif weekday == '周三':
        return '9月29日'
    elif weekday == '周四':
        return '9月30日'


def get_student_name(school_name, sheet):
    '''获取学生班级姓名'''
    name_list = sheet.col(2, start_rowx=1, end_rowx=None)
    result = []
    for i in range(len(name_list)):
        class_num = str(int(sheet.cell_value(i+1, 3)))
        class_list[school_name].append(class_num)
        result.append(class_num + name_list[i].value)
    return result

def get_text_position(bg_size, text, size):
    text_font = ImageFont.truetype("msyh.ttc", size)
    text_width = text_font.getsize(text)
    return int((bg_size[0]-text_width[0])/2)

def write_to_poster(school_name, sheets):
    '''写入图片'''
    normal_size = 24 if school_name == '笕新' else 18
    start_h = 460 if school_name == '笕新' else 420
    internal_h = 40 if school_name == '笕新' else 30
    poster = Image.open('poster.jpg')
    bg_size = poster.size
    draw = ImageDraw.Draw(poster)
    
    class_title_text = '濮小未来工程师社团{}校区'.format(school_name)
    class_title_font = ImageFont.truetype("msyh.ttc", 40)
    class_title_width = class_title_font.getsize(class_title_text)
    class_title_postion = int((bg_size[0]-class_title_width[0])/2), 80
    draw.text(class_title_postion, class_title_text,(255,255,255), font=class_title_font)

    content_text = '''亲爱的同学们：\n        祝贺以下同学被濮小未来工程师社团录取。在此谨向你们表示衷心的\n祝贺和热烈的欢迎。社团将从下周开始正式上课，上课时间是16:20-18:00，\n上课前老师会去教室接孩子，下课后统一送到校门口。
        录取名单如下：''' if school_name == '笕新' else '''亲爱的同学们：\n        祝贺以下同学被濮小未来工程师社团录取。在此谨向你们表示衷心的祝贺和热烈的欢迎。\n社团将从下周开始正式上课，上课时间是16:20-18:00，上课前老师会去教室接孩子，下课后\n统一送到校门口。
        录取名单如下：'''
    content_font = ImageFont.truetype("msyh.ttc", normal_size)
    content_width = content_font.getsize(content_text)
    suitable_width = (bg_size[0]-100)/2
    start_position = 0
    end_point = -1

    content_postion = 80, 280
    draw.multiline_text(content_postion, content_text,(255,255,255), font=content_font, spacing=10)

    for sheet in sheets:
        # xxx课录取名单：
        position = sheet.cell_value(1, 7)
        time = sheet.cell_value(1, 8)[0:2]
        if position == '电脑教室':
            position = '信息教室'
        class_name = sheet.name if sheet.name.endswith('班') else sheet.name + '班'
        draw.text((get_text_position(bg_size, '{}（{}）'.format(class_name, position), normal_size), start_h), 
            '{}（{}，{}）'.format(class_name, time, position),(255,255,255), font=content_font)
        start_h += internal_h
        student_name = get_student_name(school_name, sheet)
        name_font = ImageFont.truetype("msyh.ttc", normal_size)
        name_group = []
        for s in student_name:
            if len(s) < 6:
                    s = s + '    '
            if len(name_group) < 7:
                name_group.append(s)
            else:
                name_line = '    '.join(name_group)
                name_title_width = content_font.getsize(name_line)
                name_title_postion = int((bg_size[0]-name_title_width[0])/2), start_h
                draw.text(name_title_postion, name_line,(255,255,255), font=name_font)
                start_h += internal_h
                name_group = []
                name_group.append(s)
        if len(name_group) > 0:
            name_line = '    '.join(name_group)
            name_title_width = content_font.getsize(name_line)
            name_title_postion = int((bg_size[0]-name_title_width[0])/2), start_h
            draw.text(name_title_postion, name_line,(255,255,255), font=name_font)
            start_h += internal_h

    start_h += int(internal_h*0.5)
    group_text = '请各位家长扫码进入社团QQ群。'
    group_text_width = content_font.getsize(group_text)
    group_text_position = int((bg_size[0]-group_text_width[0])/2), start_h
    draw.text(group_text_position, group_text,(255,255,255), font=content_font)
    start_h += int(internal_h*1.5)
    group_img = Image.open('qq_group.png').resize((250, 250))
    img_location = (int((bg_size[0]-group_img.size[0])/2), start_h)
    poster.paste(group_img, img_location)


    end_text = '濮小未来工程师社团\n2021.9.23'
    if school_name == '笕新':
        draw.text((700, start_h+280), end_text,(255,255,255), font=content_font)
    else:
        draw.text((700, start_h+140), end_text,(255,255,255), font=content_font)
    poster.save('{}-poster-output.jpg'.format(school_name))

def poster(school_name):
    read_book = xlrd.open_workbook("{}名单.xls".format(school_name))
    class_sheets = read_book.sheets()
    # for s in class_sheets:
    #     class_name = s.name if s.name.endswith('班') else s.name + '班'
    #     position = s.cell_value(1, 7)
    #     time = s.cell_value(1, 8)
    #     weekday = time[0:2]
    write_to_poster(school_name, class_sheets
        # , class_name, get_date(weekday)+time[2:7], position
        )


if __name__ == '__main__':
    # write_to_poster()
    # get_student_name()
    
    for i in [
    # '万家', 
    '濮家', 
    # '笕新'
    ]:
        poster(i)
        # print(i + ':')
        # final_list = list(set(class_list[i]))
        # final_list.sort()
        # print(final_list)
