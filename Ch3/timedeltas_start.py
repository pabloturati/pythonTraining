#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it

print(timedelta(days=365, weeks=3, minutes=1))

# print today's date
now = datetime.now()
print("Today is " + str(now))

# print today's date one year from now
print("A year from today will be " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("A time delta with multiple arguments would be " +
      str(timedelta(days=365, hours=12, minutes=11, seconds=55)))

# calculate the date 1 week ago, formatted as a string
print("A week ago the date was " + str(now - timedelta(weeks=1)))
print(now.strftime("In a better format it would be: %A %B %d, %Y"))

# How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if(afd < today):
    print("April fools day already passed %d days ago" % (today-afd).days)
    afd = afd.replace(year=afd.year+1)

# Now calculate the amount of time until April Fool's Day
print("Days for next april fools day %d" % (afd-today).days)
