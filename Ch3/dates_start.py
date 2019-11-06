#
# Example file for working with date information
#

from datetime import date
from datetime import time
from datetime import datetime


def main():
    # DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today is", today)

    # print out the date's individual components
    print("Today is", today.day, today.month, today.year)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    weekdayStr = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    weekday = today.weekday()
    print('Today\'s weekday is', weekdayStr[weekday])

    # DATETIME OBJECTS
    # Get today's date from the datetime class

    now = datetime.now()
    print('Date and time is', now)

    # Get the current time
    time = datetime.time(datetime.now())
    print('The time now is:', time)


if __name__ == "__main__":
    main()
