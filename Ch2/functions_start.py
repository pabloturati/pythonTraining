#
# Example file for working with functions
#

# define a basic function


def func1():
    print("This is a function")

# function that takes arguments


def func2(val1, val2):
    print(val1, " ", val2)

# function that returns a value


def cube(x):
    return x*x*x

# function with default value for an argument


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result*num
    return result


# function with variable number of arguments

def multi_add(firstArg, *args):
    result = 0
    for i in args:
        result = result + i
    print("First is " + str(firstArg))
    return result

# Comment each line to run it


func1()
print(func1())
print(func1)

func2(10, 20)
print(func2(10, 20))
print(cube(10))

print(power(2))
print(power(2, 3))
print(power(x=2, num=3))


print(multi_add(3))
print(multi_add(3, 5))
print(multi_add(3, 5, 7))
