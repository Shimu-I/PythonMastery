# Unordered collection of unique values
# { , , ,}
# this is very fast

print("*" * 30)
# ------------------------------
# Data structures has these 4 character
# ------------------------------

# ----SET----
# Ordered
# Duplicates
# Indexed
# Mutable

print("*" * 30)
my_set = {10, 30, 20}
print(my_set) # NOT ordered


print("*" * 30)
my_set = {10, 30, 20, 10}
print(my_set) # NOT duplicate

print("*" * 30)
my_set = {10, 30, 20, 10}
# print(my_set[1]) # NOT indexed

print("*" * 30)
my_set = {10, 30, 20, 10}
my_set.remove(20)
print(my_set) # Mutable 

