def draw(n):
    line = n * 5 + 1
    a = '+ - - - - '
    b = '+'
    c = '|         '
    for i in range(1,line + 1):
        if i % 5 == 1:
            print(a * n,end='')
            print(b)
        else:
            print(c * n,end='')
            print(c)
N = int(input('输入n值:'))
draw(N)