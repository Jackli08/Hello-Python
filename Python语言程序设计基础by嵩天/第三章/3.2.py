dayup = 1
for i in range(365):
      if i % 7 in [0,1,2,3]:
            dayup *= 1.01
print("输出{:.2f}".format(dayup))
