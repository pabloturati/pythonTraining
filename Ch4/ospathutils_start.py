#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    filename = "mytextfile.txt"
    print("Item exists " + str(path.exists(filename)))
    print("Is this a file " + str(path.isfile(filename)))
    print("Is this a directory " + str(path.isdir(filename)))

    # Work with file paths
    # get full path
    print("Item path is: " + str(path.realpath(filename)))
    print("Split " + str(path.split(path.realpath(filename))))

    myFilepath = path.split(path.realpath(filename))[0]
    myFileName = path.split(path.realpath(filename))[1]
    print("%s/%s" % (myFilepath, myFileName))

    # Get the modification time
    # ctime converts epoch time to readable format
    t = time.ctime(path.getmtime(filename))
    print(t)

    print(datetime.datetime.fromtimestamp(path.getmtime(filename)))

    # Calculate how long ago the item was modified
    now = datetime.datetime.now()
    print(now)
    modDate = datetime.datetime.fromtimestamp(path.getmtime(filename))
    print("It has been " + str(now-modDate) + " since the file was modified")
    print("or %d total seconds" % (now-modDate).total_seconds())


if __name__ == "__main__":
    main()
