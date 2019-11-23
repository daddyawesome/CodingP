#Write a Python program to calculate number of days between two dates
from datetime import timedelta
from datetime import date

f_date = date(2019, 11, 23)
l_date = date(2020, 4, 11)
delta = l_date - f_date
print(delta.days)
print(f_date + timedelta(days=100))
