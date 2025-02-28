num1 = int(input('第一个整数：'))
num2 = int(input('第二个整数：'))
if num1 > num2:
    num3 = num2 % (num1 % num2)
else:
    num3 = num1 % (num2 % num1)
num4 = num1 * num2 / num3
print('最大公约数为：{0}，最小公倍数为：{1}'.format(num3,num4))