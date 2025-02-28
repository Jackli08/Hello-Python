from datetime import datetime
birthday = datetime(2008,4,3)
print(birthday.strftime('%d/%m/%Y'))
print(birthday.strftime('%Y-%m-%d'))
print(birthday.strftime('%m/%d/%Y'))
print(birthday.strftime('%d/%m/%Y'))
print(birthday.strftime('the{0:%d}of{0:%B},{0:%Y}'.format(birthday)))