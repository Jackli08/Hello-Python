from datetime import datetime 
year = eval(input('请输入年份:'))
month = eval(input('请输入月份:'))
day = eval(input('请输入日期:'))
someday = datetime(year,month,day)
n = int(someday.isoweekday())
weekday_id = '星期一星期二星期三星期四星期五星期六星期天'
weekday_name = (n - 1) * 3
print(weekday_id[weekday_name:weekday_name + 3])