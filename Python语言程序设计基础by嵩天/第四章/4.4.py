import random
num = random.randint(0,100)
t = 0
while True:
    t += 1
    Num = eval(input('请输入：'))
    if Num == num:
        break
    else:
        if Num > num:
            print('遗憾，太大了')
        else:
            print('遗憾，太小了')
print('预测{}次，你猜中了！'.format(t))