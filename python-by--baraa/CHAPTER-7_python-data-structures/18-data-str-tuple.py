# Ordered collection that can't be changed after creating it

# Locked for safety reason
# Usage: when the data need to be protected
# create (, , , )


print("*" * 30)
# ------------------------------
# Data structures has these 4 character
# ------------------------------

# ----TUPLE----
# Ordered
# Duplicates
# Indexed
# Mutable

print("*" * 30)
my_tuple = (10, 30, 20)
print(my_tuple) # my given ordered


print("*" * 30)
my_tuple = [10, 30, 20, 10]
print(my_tuple) # allow duplicate

print("*" * 30)
my_tuple = (10, 30, 20, 10)
print(my_tuple[1]) # tuple are indexed

print("*" * 30)
my_tuple = (10, 30, 20, 10)
# my_tuple[3] = 40
print(my_tuple) # NOT Mutable  = Immutable

print(sorted(my_tuple)) # can change-- output of this funtion list