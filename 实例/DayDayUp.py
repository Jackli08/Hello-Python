def dayUP(n) :
    dayup = 1.0
    for i in range(365):
        if i % 7 in [0,2,3,1]:
            dayup *= (1 + n)
    return dayup
N = float(input('n='))
print('结果是：{}'.format(dayUP(N)))