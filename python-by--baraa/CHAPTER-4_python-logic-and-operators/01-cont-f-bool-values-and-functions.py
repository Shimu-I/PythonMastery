# Python Boolean (values and functions)
# Values true and false
print(True)
print(False)
print(type(True))
print(bool(123))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))

# functions
email = ""
phone = "0176-123456"
username = ""

# Allows registration
# if any field is filled
print(any([email, phone, username]))

# allows registration
# only of all fields is filled
print(all([email, phone, username]))

# value belong to a specific datatype
print(isinstance(123, int))
print(isinstance(True, str))
print("Hello".endswith("o"))
print("Hello".startswith("o"))



