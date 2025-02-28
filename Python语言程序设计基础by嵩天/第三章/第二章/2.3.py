#PythonDraw.py
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)
col = ["purple","red","blue","violet"]
for j in col:
      turtle.pencolor(j)
      turtle.circle(40,80)
      turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()
