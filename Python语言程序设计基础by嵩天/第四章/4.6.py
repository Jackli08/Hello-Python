import random

car1 = 0
answer = [False,True,False]
car2 = 0
 
for i in range(10000):
    choose = random.randint(0,2)
    
    if choose == True:
        car1 += 1
    
    if choose == 0 or choose == 2:
        car2 += 1

p1 = car1 / 10000 * 100
p2 = car2 / 10000 * 100
print('不更改的概率：{0:.2f}%，更改的概率：{1:.2f}%'.format(p1,p2))