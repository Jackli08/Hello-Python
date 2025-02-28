str_a = input('输入一行字符：')
eng = 0
num = 0
kong = 0
qita = 0
english1 = 'abcdefghijklmnopqrstuvwxyz'
english2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '1234567890'
kong2 = ' '
for i in str_a:
    if i in english1 or i in english2:
        eng += 1
    elif i in number:
        num += 1
    elif i in kong2:
        kong += 1
    else:
        qita += 1
print('英文字符有{0}个，数字{1}有个，空格有{2}个，其他字符有{3}个'.format(eng,num,kong,qita))