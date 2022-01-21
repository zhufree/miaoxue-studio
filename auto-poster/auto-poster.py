from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

students = {'戚菡宇&戚菡辰': '戚菡宇和戚菡辰是两位很乖巧的同学，上课遵守纪律，也积极完成课堂任务，因为年纪比较小，可能在使用鼠标，打字等方面有一些困难，但态度很认真，上课很积极，也有自己的想法，期待两个小朋友一起把scratch这门课学得越来越好，能够做出自己的作品，体会到编程世界的魅力！',
'安启维': '安启维同学上课很活跃，在老师提问的时候能积极回答，但有时候也会说一些和课上无关的话，注意力不是很集中，这一块的能力和习惯还需要多加锻炼，才能适应编程课需要抽象思维的课程内容，加油，老师相信你的潜力！',
'张之逍': '你是个活泼可爱的孩子，上课时非常活跃，对课堂内容的掌握也很不错，总能想出一些和老师不同的点子，有自己的想法，很有潜力，期待你把scratch这门课学得越来越好，能够做出自己的作品，体会到编程世界的魅力，老师期待看到你的进步！',
'丁鋆杰': '你在课堂上非常活跃，看得出来你很喜欢这门课程，有认真对待每一节课，积极回应老师的讲课，也认真记笔记，跟着老师的进度完成任务，课后还能主动花时间在家练习，每一点进步老师都看得见，期待你把scratch这门课学得越来越好，能够做出自己的作品，体会到编程世界的魅力，加油！',
'梅瑾': '你在课堂上不太爱说话，但是看得出来完成任务很认真，沉稳内敛的性格可能更有助于专注在课程内容上，能够长时间集中注意力，锻炼自己的抽象思维，很多时候你都能提前完成老师的任务，有问题时也希望你积极提问，解决了问题才能学得更好，期待你之后的表现，加油！',
'邱奕琛': '邱奕琛同学上课很活跃，但是很容易被其他同学影响，注意力不是很集中，同时要养成主动测试自己作品的习惯，代码写完之后要自己运行尝试，独立发现问题。兴趣是孩子最好的老师，希望在保持对scratch编程的兴趣的情况下，你能够查漏补缺，打好基础，做出自己喜欢的作品，加油！',
'金赫阳': '你在前几节课上的注意力不是很集中，但后面的转变让老师很欣慰，看到你有努力跟着老师的进度去尝试完成，但是老师希望你可以自信一些，大胆尝试，错了也可以修改，所以不需要每一步都要先征询老师的意见，理清思路动手去做就好，遇到错误再来提问就好，老师相信你会有更大的进步，加油！',
'陈逸楠': '陈逸楠同学，你对scratch有一定的基础，能够独立完成一部分的任务，但老师认为如果上课能够更加专心在课堂上的话，你会有更大的进步，希望你不要荒废已经学到的东西，老师相信你是有潜力的，加油，期待你的进步！',
'陈德锦': '你的scratch学得很好，老师觉得你的水平其实可以上中级班，看到你在课上能够游刃有余完成任务，同时还能发挥自己的创造力，做出有自己风格的作品，老师知道你对基础积木块的掌握已经得心应手，后面需要提升的主要是设计和组织作品的能力，期待你给老师带来更多精细，加油！',
'王梓萱': '你是一个很让老师放心的孩子，上课时纪律很好，作品完成很快，也能够根据自己的审美对造型做出一定的发挥，入门班的课程对你来说不是太大的挑战，相信在这个过程中你也收获了很多，希望你能体会到编程的乐趣，创造的乐趣，期待你之后的作品，加油！',
'陶宋豪': '陶宋豪同学，你上课时很遵守纪律，能认真跟随老师的讲解，也能独立完成大部分任务，有问题时会积极提问，是个不需要老师太操心的学生，但老师希望你可以对自己要求更高一些，完成的作品之后可以主动找找bug，花心思做得更完美一些，有比较强的自驱力才能做出更好的作品，你是很有潜力的，老师期待你的进步！',
'黄迪睿': '黄迪睿同学，因为课业等原因你有一些课程没有跟上课堂进度，但老师也看见你在课堂上有认真对待，积极完成任务，不懂的问题也有提问老师，希望错过的知识不会影响你对编程的兴趣，老师相信你可以跟上进度，发挥自己的潜力，加油！',
'傅予': '傅予同学，你在前几节课上的注意力不是很集中，总是喜欢按照自己的想法随心所欲，但后面的转变让老师很欣慰，看到你有努力跟着老师的进度去尝试，有认真记笔记，努力完成任务，相信在这个过程中你也收获了很多，希望你能体会到编程的乐趣，创造的乐趣，老师相信未来你会有更大的进步，加油！',
'张妙涵': '你是一个很让老师放心的孩子，上课时纪律很好，作品完成很快，也能够根据自己的审美对造型做出一定的发挥，入门班的课程对你来说不是太大的挑战，相信在这个过程中你也收获了很多，希望你能体会到编程的乐趣，创造的乐趣，期待你之后的作品，加油！'}

def write_to_poster(name, comment, class_name):
    start_h = 720
    internal_h = 50
    poster = Image.open('report_bg_2.jpg')
    bg_size = poster.size
    draw = ImageDraw.Draw(poster)

    # draw title
    title_text = class_name
    title_font = ImageFont.truetype("tonghua.ttf", 90)
    title_width = title_font.getsize(title_text)
    title_postion = int((bg_size[0]-title_width[0])/2), start_h
    draw.text(title_postion, title_text,(255,255,255), font=title_font)
    start_h += 95
    title2_text = '期末总评'
    title2_font = ImageFont.truetype("tonghua.ttf", 85)
    title2_width = title2_font.getsize(title2_text)
    title2_postion = int((bg_size[0]-title2_width[0])/2), start_h
    draw.text(title2_postion, title2_text,(255,255,255), font=title2_font)
    
    # draw name
    start_h += 95
    name_font = ImageFont.truetype("tonghua.ttf", 60)
    name_width = name_font.getsize(name)
    name_postion = int((bg_size[0]-name_width[0])/2), start_h
    draw.text(name_postion, name,(255,255,255), font=name_font)
    
    # draw content
    start_h += 80
    content_font = ImageFont.truetype("tonghua.ttf", 50)
    suitable_x = (bg_size[0]-600)/2
    lines = textwrap.wrap(comment, width=12)
    for line in lines:
        width, height = content_font.getsize(line)
        draw.text((suitable_x, start_h), line, font=content_font, fill=(255,255,255))
        start_h += internal_h
        # draw.text(content_postion, comment,(255,255,255), font=content_font, spacing=10)
    start_h += 30
    # draw footer
    footer_text = '2022.1.20\n朱老师'
    footer_font = ImageFont.truetype("tonghua.ttf", 40)
    footer_width = footer_font.getsize(footer_text)
    footer_postion = 600, start_h
    draw.text(footer_postion, footer_text,(255,255,255), font=footer_font)
    poster.save('{}-poster-output.jpg'.format(name))

if __name__ == '__main__':
    # name = input('name:')
    # comment = input('comment:')
#     name = '戚菡宇&戚菡辰'
#     comment = '戚菡宇和戚菡辰是两位很乖巧的同学，上课遵守纪律，也积极完成课堂任务\
# ，因为年纪比较小，可能在使用鼠标，打字等方面有一些困难，但态度很认真，上课\
# 很积极，也有自己的想法，期待两个小朋友一起把scratch这门课学得越来越好，能够\
# 做出自己的作品，体会到编程世界的魅力！'
    for name in students.keys():
        write_to_poster(name, students[name], 'scratch入门班')