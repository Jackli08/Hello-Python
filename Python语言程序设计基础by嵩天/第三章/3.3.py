dayup = 1
dayfact = 10
for i in range(365):
      if i in [0,1,2,3]:
            if i % dayfact > 0:
                  dayup *= 1.01
print("输出{:.2f}".format(dayup))
