fo = open('E:\\linshi\\testfour.txt','r')
print(fo.read())
fo.close()



fo = open('E:\\linshi\\test4.txt','w')
fo.write('testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest')
fo.close()


fo = open('E:\\linshi\\test4.txt','r')
print(fo.read(30))
fo.close()