#
# Example file for formatting time and date output
#

from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes

    now = datetime.now()

    #### Date Formatting ####

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime(
        "The date is: \nYear: long- %Y short- %y\nMonth: long- %B short- %b\nDay: %d\nThe full date is %D\n"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime(
        "The locale is:\n Date and time %c\nJust date: %x\nJust time: %X\n"))

    #### Time Formatting ####

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime(
        "Formatted current time:\nNormal time is: %I:%M:%S %p\nMilitary time is: %H:%M:%S\n"))


if __name__ == "__main__":
    main()
