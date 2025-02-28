def chong(ls):
    temp = set(ls)
    lenls = len(ls)
    lent = len(temp)
    if lenls != lent:
        return True
    
str = input('输入数字逗号隔开:')
l = str.split(',')
if chong(l) == True:
    print('有重复!')
else:
    print('无重复!')