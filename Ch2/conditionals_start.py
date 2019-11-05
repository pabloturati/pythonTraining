#
# Example file for working with conditional statements
#


def main():
    x, y = 1000, 100

    # conditional flow uses if, elif, else
    if(x < y):
        st = "x is less then y"
    elif(x == y):
        st = "x is the same as y"
    else:
        st = "x is more then y"

    print(st)
    # conditional statements let you use "a if C else b"
    print("Now, using a single line")
    st = "x is less then y" if (x < y) else "y is less then x"
    print(st)


if __name__ == "__main__":
    main()
