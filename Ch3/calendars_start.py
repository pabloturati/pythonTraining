#
# Example file for working with Calendars
#


# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2019, 1, 9, 1)
print(st)


# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2019, 1)
print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2019, 8):
    print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for i in calendar.month_name:
    print(i)

print("\n")

for i in calendar.day_name:
    print(i)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

print("Thursday monthly meetings will be on the following dates")

for m in range(1, 13):
    cal = calendar.monthcalendar(2019, m)
    firstWeek = cal[0]
    secondWeek = cal[1]

    if(firstWeek[calendar.THURSDAY] != 0):
        meetday = firstWeek[calendar.THURSDAY]
    else:
        meetday = secondWeek[calendar.THURSDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))
