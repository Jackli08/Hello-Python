def isPrime(x):
    from math import sqrt
    try:
        int(x)
    except:
        print('错误!')
    else:
        if x == 1 or x == 0:
            return False
        for i in range(2,int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True