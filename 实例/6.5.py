import random
def getBirth():
    ls = []
    mon = random.randint(1,12)
    if mon in [1,3,5,7,8,10,12]:
        dat = random.randint(1,31)
    elif mon == 2:
        dat = random.randint(1,28)
    else:
        dat = random.randint(1,30)
    ls.append(mon)
    ls.append(dat)
    return ls

def BirthNum():
    ls = []
    for i in range(23):
        ls.append(getBirth())
    return ls

def chong():
    t = 0
    ls = BirthNum()
    temp = set()
    for s in ls:
        p = tuple(s)
        temp.add(p)
    lls = len(ls)
    llt = len(temp)
    if lls != llt:
        t += 1
    return t

def main():
    a = int(input('输入次数:'))
    s = 0
    for i in range(a):
        s += chong()
    print('概率是:{}%'.format(s / a * 100))

main()