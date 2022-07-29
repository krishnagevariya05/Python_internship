import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)


import datetime

date_object = datetime.date.today()
print(date_object)
import datetime

print(dir(datetime))


import datetime

d = datetime.date(2019, 4, 13)
print(d)


from datetime import date

a = date(2019, 4, 13)
print(a)

from datetime import date

today = date.today()

print("Current date =", today)

from datetime import date

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)


from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)
from datetime import datetime

#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)