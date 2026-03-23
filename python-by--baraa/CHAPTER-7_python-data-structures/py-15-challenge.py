# Dict challenge

user = {
    "id": 1,
    "name": "John",
    "age" : 30,
    "city" : "Berlin"
}

# requirements
# create new dict
# keep only pairs with string value
# convert values to UPPERCASE
# elegant and shortest way possible

# CHALLENGE: keep only string values and Convert them to uppercase

# user_str = {
#     # Expression
#     # Loop
#     # Filter
# }

user_str = {
    k: v.upper()
    for k, v in user.items()
    if isinstance(v, str)
}

print(user_str)