#
# Example file for working with loops
#


def main():
    x = 0

    # define a while loop
    while (x < 5):
        print(x)
        x = x+1

    # define a for loop
    for x in range(5, 10):
        print(x)

    # use a for loop over a collection
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Satuday", "Sunday"]
    # for day in days:
    print(day)

    # use the break statement
    for day in days:
        if(day == "Wednesday"):
            break
        print(day)

    # use the continue statement
    for day in days:
        if(day == "Friday"):
            continue
        print(day)

    # using the enumerate() function to get index
    for index, day in enumerate(days):
        print(index, day)


if __name__ == "__main__":
    main()
