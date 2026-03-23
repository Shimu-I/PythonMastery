# Validate the QUality and Correctness of Passwords

# CONDITIONS

# Must not be emtpy
# Must be at least 8 characters
# Must include at least 1 uppercase
# Must include at least 1 lowercase
# Must not be same as the email
# Must not contain any spaces
# Must start and end with a letter or digit

# Solution

password = "12UUUUUUUUUUUU".strip()
email = " user@gmail.com".strip()
value = True

if (password == ""):
    print("Your password is empty.")
    value = False
if not (len(password) >= 8):
    print("Your password must be at least 8 characters.")
    value = False
if password != password.lower():
    print("Password must include at least 1 lowercase.")
    value = False
if password != password.upper():
    print("Password must include at least 1 uppercase.")
    value = False
if password == email:
    print("Your password can not be same as your email.")
    value = False
if " " in password:
    print("Your password can not have any spaces.")
    value = False
if value:
    print("The Password is valid.")
