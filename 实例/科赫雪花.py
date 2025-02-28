import turtle as t
def koch(size,n):
    if n == 0 :
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)

def main():
    t.setup(600,600)
    t.speed(0)
    t.pu()
    t.goto(-200,100)
    t.pd()
    t.pensize(2)
    t.hideturtle()
    level = 5
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.right(120)
    koch(400,level)

main()
t.done()
