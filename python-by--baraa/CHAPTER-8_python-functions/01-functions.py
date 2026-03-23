# example without function
import math
print("Wake up")
print("Start Machine")
print("Make Coffee")
print("Add Milk")
print("Enjoy it")
print("Working for a while")
print("Start Machine")
print("Make Coffee")
print("Add Milk")
print("Enjoy it")

# example with function
print("*" * 30)


def make_coffee():
    print("Start Machine")
    print("Make Coffee")
    print("Add Milk")
    print("Enjoy it")


print("Wake up")
make_coffee()


print("*" * 30)
# Different source of python functions

# Built-in Function (Just Calling)
print(len("Python"))

# Function From Libraries (Import Then Call)
number = 4.2
print(math.ceil(number))

# User Defined Function (Define Then Call)
def greet():
    print("Hello")
greet()