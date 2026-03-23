print("=" * 30)
print("TASK-1")
# Check if a user's name is not empty and the age is greater than or equal 18

user_name = "shimu"
age = 23
print(user_name != "" and age >= 18)


print("=" * 30)
print("TASK-2")
# Check if the password is at least 8 character long and does not contain spaces

password = "1w3e4r56y7"
print(len(password) >= 8 and " " not in password)


print("=" * 30)
print("TASK-3")
# Check if a user's email is not empty. contain '@'. and ends with '.com'

email = "user@gmail.com"
print( email != "" and "@" in email and email.endswith(".com"))


print("=" * 30)
print("TASK-4")
# Check if a username is a string, is not None, and is longer than 5 character

user_name = "user_name"
print(isinstance(user_name, str) and user_name is not None and len(user_name) > 5)

print("=" * 30)
print("TASK-5")
# Check if the user is eith an admin or moderator, and either they've not banned or they've verified their email


user = "admin"
not_banned = True
varified_email = True

print(user == "admin" or user == "moderator" or not_banned or varified_email)