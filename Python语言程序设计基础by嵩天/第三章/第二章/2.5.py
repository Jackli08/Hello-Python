#叠加等边三角形的绘制。
from turtle import *
fd(200)
for i in range(3):
      seth(120 - i * 120)
      fd(200)
seth(0)
fd(200)
for i in range(2):
      seth(120 + i * 120)
      fd(400)
done()
