#绘制靶盘。
from turtle import *
for i in range(9):
      circle(50 + 20 * i)
      pu()
      seth(270)
      fd(20)
      seth(0)
      pd()
done()
