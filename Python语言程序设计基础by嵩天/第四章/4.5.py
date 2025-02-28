import random
num = random.randint(0,100)
t = 0
while True:
    try:
        Num = int(input('请输入：'))
    except ValueError:
        print('输入内容必须为整数！')
        break
    else:
        t += 1
        if Num == num:
            print('预测{}次，你猜中了！'.format(t))
            break
        else:
            if Num > num:
                print('遗憾，太大了')
            else:
                print('遗憾，太小了')
