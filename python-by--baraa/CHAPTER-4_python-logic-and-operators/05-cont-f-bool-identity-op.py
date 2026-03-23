# Identity Operators

# here we are compairing the object id with (is)

# if two objects pointing to = same value = has same object ID

# if two object != different value != object ID

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print(x == y)
print(x is y)

x = 10
y = 10
print(x == y)
print(x is y)

y = x
print(x == y)
print(x is y)


#Usage
# Make sure the email exists, and it's not empty.

email = None
print(email is not None and email != "")