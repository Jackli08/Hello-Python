#实例1的修改。
tempstr = eval(input("请输入摄氏温度值："))
F = 1.8*tempstr + 32
print("转换后的温度是{}F".format(int(F)))
#-------------------------------------------
TempStr = eval(input("请输入华氏温度值："))
C = (TempStr - 32)/1.8
print("转换后的温度是{}C".format(int(C)))
