#
# Read and write files using the built-in Python file methods
#


def main():
    # Open a file for writing and create it if it doesn't exist
    # f = open("mytextfile.txt", "w+")

    # Open the file for appending text to the end
    # f = open("mytextfile.txt", "a")

    # write some lines of data to the file
    # for i in range(1, 11):
    #     f.write("This is line %d\r\n" % (i*10))

    # close the file when done
    # f.close()

    # Open the file back up and read the contents
    f = open("mytextfile.txt", "r")

    if(f.mode == "r"):
        # contents = f.read() #reads the entire file
        linesArray = f.readlines()
        for line in linesArray:
            print(line)

    f.close()


if __name__ == "__main__":
    main()
