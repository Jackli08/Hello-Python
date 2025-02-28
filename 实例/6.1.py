import random
words = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',\
'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',\
'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', \
'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',\
'1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(10):
    password = random.sample(words,8)
    for w in password:
        print(w,end='')
    print()