# Add, Remove, Update
print("-" * 30)
# Add
user = {
    "id": 1,
    "age": 30,
    "city": "berlin"
}

user["name"] = "John"  # new key and value
print(user)


print("-" * 30)
# update --  existing value
user['age'] = 35
print(user)



print("-" * 30)
# update multiple value at once
user.update({'age': 40, "city": "Paris"})
print(user)


print("-" * 30)
# remove single value
age = user.pop("age")
print("Removed item: ", age)
print(user)

# non existing value remove = error = not safe
# salary = user.pop("salary")
# print("Removed item: ", salary)
# print(user)

print("-" * 30)
# to make it safe use a default value. if there is no key in such name
salary = user.pop("salary", "NOT FOUND")
print("Removed item: ", salary)
print(user)


print("-" * 30)
# user.pop() # given error -> with out any value
# delete the most recent value form the dictionary
user.popitem()
print(user)


print("-" * 30)
# Dict creation with new keys all same default vaue

user1 = {
    "id": None,
    "age": None,
    "city": None
}

user1 = dict.fromkeys(["id", "name", "age", "city"], None)
print(user1)


