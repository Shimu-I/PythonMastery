# Function parameters and Arguements

# its types, shaps, and purposes


#---------------------------------------
# Parameters usage case
#---------------------------------------
def clean_name():
    name = " vioLet " 
    print(name.strip().lower())

clean_name()

print("*" * 30)

def clean_name(name):
    print(name.strip().lower())

clean_name(" vioLet  ")
clean_name(" liLy  ")





print("*" * 30)
#---------------------------------------
# Parameters Local Variables adn Global Variables
#---------------------------------------

# python has 3 kinds of variables
# parameters
# local variables
# global variabls

# only two things matter
# How long does it live?
# Where is it accessible?


def clean_name(name): # parameter
    cleaned = name.strip().lower() # local variable
    print("Raw:", name)
    print("Cleaned:", cleaned)

clean_name(" MariA  ")


print("*" * 30)
# global variable application 
case_rule = "n/a" # global
def clean_name(name): # parameter
    cleaned = name.strip() # local variable
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print("Cleaned:", cleaned)

clean_name(" MariA  ")
print("The Rule is:", case_rule)


