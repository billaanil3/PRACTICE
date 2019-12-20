import datetime


def next_day(given_date, weekday):
    day_shift = (weekday - given_date.weekday()) % 7
    return given_date + datetime.timedelta(days=day_shift)

now = datetime.date(2018, 4, 15) # sunday
names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
         'saturday', 'sunday']
for weekday in range(7):
    # print(names[weekday]
    print next_day(now, weekday)