# Dictionaries Special methods

user = {
    'id': 1,
    'age': 30,
    'city': "berlin"
}

# access
print(user['city'])
# print(user["name"]) # if key not find gives error

# if not sure about the key being existed
print(user.get("name"))  # return value or NONE

print(user.get("name", "Unknown"))  # shows different message

# checks if the keys are inside or not
print("age" in user)
print("name" in user)

# view objects
# it returns all the keys of dictionaries
print(user.keys())
# it returns all the values of dictionaries
print(user.values())
# it returns both key and value
print(user.items()) # we get a list of tuples [ (), (), ()] 
# it is easir to looping, transforming data, building new dicts, coparing and more


# looping
for u in user:
    print(u) # only getting the key

for u in user:
    print(u, " ",user[u]) # both key and value NOT recommended

for key, value in user.items():
    print(key, value) # recommended