import time

def get_time():
    time_msg = '各位家长{time}好{emoji}，'
    tick = time.localtime(time.time())
    if tick.tm_hour < 12:
        time_msg = '各位家长上午好[太阳][太阳]，'
    elif tick.tm_hour < 18:
        time_msg = '各位家长下午好[太阳][太阳]，'
    elif tick.tm_hour < 24:
        time_msg = '各位家长晚上好[晚安][晚安]，'
    return time_msg

concentrate_words = ['认真听讲', '认真完成任务', '态度认真']
active_words = ['表现活跃', '表现积极', '踊跃回答问题']
creative_words = ['很有创意', '']
class_intro = '今天是我们{classname}的第{no.}节课。'
class_content = '本节课{class_content}。'
special_student = '{name}同学{}，表现出色，提出表扬{emoji}。'


print(time_msg)