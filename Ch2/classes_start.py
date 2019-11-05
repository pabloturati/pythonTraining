#
# Example file for working with classes
#


class myClass():
    def method1(self):
        print("Hello from method1")

    def method2(self, saySomething):
        print("Hello from method2", saySomething)


class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("Another method 1")

    def method2(self, saySomething):
        print("Another method 2")


def main():
    c = myClass()
    c.method1()
    c.method2("something")

    print("\nNow working with class that inherits:\n")

    c2 = anotherClass()
    c2.method1()
    c2.method2("something")


if __name__ == "__main__":
    main()
