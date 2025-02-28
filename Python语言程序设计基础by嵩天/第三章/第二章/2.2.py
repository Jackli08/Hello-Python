#汇率兑换程序。
money = input("请输入带货币符号的数值：")
if money[0:3] in ["CNY"]:
      U = eval(money[3:])/6
      print("转换后的数值是：USD{:.2f}".format(U))
elif money[0:3] in ["USD"]:
      R = eval(money[3:])*6
      print("转换后的数值是：RMB{:.2f}".format(R))
else:
      print("输入格式错误！")
