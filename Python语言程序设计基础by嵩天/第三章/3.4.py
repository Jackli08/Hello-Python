n = input("一串数字：")
if len(n) == 5:
      N = eval(''.join(reversed(n)))
      if N == eval(n):
            print('是')
      else:
            print('不是')
else:
      print('错误')
