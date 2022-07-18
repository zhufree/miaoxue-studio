import random
import string

print('''
    猜字符串游戏
    规则：输入你要猜的字符串长度，计算机会随机生成一个字符串。你可以输入符合这个长度字符串来猜
    1. 如果你输入的字符串中的字母在目标字符串中并且位置也正确，计算机会在这一位显示√
    2. 如果字母正确，位置不对，计算机会在该字母位置显示-
    3. 如果目标字符串没有这个字母，计算机会显示x
    ''')
word_length = int(input('请输入你要猜的字符串长度：'))
answer = ''
current_notice = []
for i in range(word_length):
    answer += random.choice(string.ascii_lowercase)
    current_notice.append('x')
print(answer)
print(current_notice)
while 'x' in current_notice or '-' in current_notice:
    guess_word = input('请输入你猜的字符串: ')
    if len(guess_word) != word_length:
        print('输入的字符串长度不正确')
    else:
        for i, guess_letter in enumerate(guess_word):
            if guess_letter == answer[i]:
                current_notice[i] = '√'
            elif guess_letter in answer:
                current_notice[i] = '-'
            else:
                current_notice[i] = 'x'
        print(guess_word)
        print(''.join(current_notice))
