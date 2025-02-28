import turtle as t
def koch(size,n):
    if n == 0 :
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)

def main():
    t.setup(800,400)
    t.speed(10)
    t.pu()
    t.goto(300,50)
    t.pd()
    t.pensize(2)
    t.pencolor('red')
    t.hideturtle()
    t.seth(180)
    koch(600,3)

main()
t.done()