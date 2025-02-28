#Q1
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上：{:.2f} ，向下：{:.2f}".format(dayup,daydown))

#Q2
dayfactor = 0.005
dayup = pow(1 + dayfactor,365)
daydown = pow(1 - dayfactor,365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup,daydown))

#Q3
dayup = 1.0
dayfactor = 0.01
for i in range(365):
      if i % 7 in [6,0]:
            dayup *= 1 - dayfactor
      else:
            dayup *= 1 + dayfactor
print("工作日的力量：{:.2f}".format(dayup))

#Q4
def dayUP(df):
      dayupB = 1
      for i in range(365):
            if i % 7 in [6,0]:
                  dayupB *= 1 - 0.01
            else:
                  dayupB *= 1 + df
      return dayupB
dayfactor = 0.01
dayupA = round(pow(1 + 0.01,365),2)
while dayUP(dayfactor) < dayupA:
      dayfactor += 0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))