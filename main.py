import  datetime
import pytz
from pip._vendor.toml import tz

today = datetime.date.today()
print(today)

birthday = datetime.date(1997, 3, 28)
print(birthday)

#find the days since birth
days_since_birthday = today - birthday
print(days_since_birthday)


# adding 10 days to cureent date
tdelta = datetime.timedelta(days=10)
print(today - tdelta)

print(today.month)

print(today.day )
print(today.weekday())

print (datetime.time(7, 2, 20, 15))
#datetime.date(Y, M, D)
#datetime.time(h, m, s, ms)
#datetime.datetime(Y, M, D, h, m, s, ms)


#add 10 hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

#print(datetime.datetime.now(tz=pytz.UTC))

datetime_today = (datetime.datetime.now(tz=pytz.UTC))
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)
for tx in pytz.all_timezones:
    print(tz)

#string formating with dates
#2020-11-07 -> November , 2020

print(datetime_pacific.strftime('%B %d, %Y'))


#November 07, 2020 -> datetime(2020,3,9)
# strptime (p = parsting)

datetime_thing = datetime.datetime.strptime('November 07, 2020', '%B %d, %Y')
print(datetime_thing)












