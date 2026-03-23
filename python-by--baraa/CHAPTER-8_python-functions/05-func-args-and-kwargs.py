# cal the total of values
def total(a, b):
    print(a + b)


total(1, 2)

print("*" * 30)


def total(a=0, b=0, c=0):
    print(a + b + c)


total(1, 2)
total(1, 2, 3)
# total(1, 2, 3, 4)  # not efficient

print("*" * 30)
# instade of changing the num of args and them change the params we have two options
# option 1: can pass a list --> heavier
# option 2: *args or ** kwargs
# python is collecting differnt vlaue in tuples

# *args example


def total(*args):
    print(sum(args)) # data type of args = tuple


total(1, 2, 3, 4, 5)


print("*" * 30)
# **kwargs example
# create the user profile


def create_user(**kwargs):
    print(type(kwargs)) # data type of kwargs = dictionary
    print(kwargs)


create_user(first_name="mo", last_name="sa", age=33, country="Egypt")
create_user(name="motg",country="Egypt")
#create_user("motg","Egypt") # doesn't word as this is not posiitional
