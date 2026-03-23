print("*" * 30)
#---------------------------------------
# Positional and Keyword Arguments
#---------------------------------------

# Building full clean name
def clean_name(first_name, last_name, country):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)

# positional arguments
clean_name (" MariA", "SmITH", "DE") 

# There are 2 ways we send value to the python
# 1. keyword arguments
# 2. positional arguments

# keyword arguments ->> easier to read and understand extra effort 
clean_name(country = "DE", first_name = " MariA ", last_name = "SmiTh")


# mix arguments
clean_name(" MariA", last_name = "SmiTh", country = "DE")
clean_name(" MariA", "SmiTh", country = "DE")
# mix arguments has some rule like
# can't start with positional args then keyword
# follow --> positional argument follows keyword argument
# Why use positional and keyword together = for styling (NOT recommended)
# primary = positional 
# secondary = keyword