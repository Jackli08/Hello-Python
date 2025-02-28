#正方形螺旋线的绘制。
from turtle import *
seth(90)
for i in range(11):
      fd(10 + i * 10)
      left(90)
      fd(10 + i * 10)
      left(90)
fd(120)
done()
