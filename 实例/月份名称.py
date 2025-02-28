monthstr = '一月二月三月四月五月六月七月八月九月十月十一月十二月'
monthid = eval(input('输入数字(1-12):'))
if monthid <= 10 :
    pos = (monthid - 1) * 2
    print(monthstr[pos:pos + 2])
elif 10 < monthid <= 12 :
    pos = (monthid - 1) * 2
    if monthid == 12:
        pos = (monthid - 2) * 2 + 3
    print(monthstr[pos:pos + 3])
else:
    print('错误！')
