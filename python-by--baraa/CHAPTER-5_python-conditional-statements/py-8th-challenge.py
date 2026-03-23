# We do here quality checks
# Validate the Quality and Correctness of Email Values

# CONDITIONS
# Must not be empty
# Must contain '.' and '@'
# Must contain exactly one '@' symbol
# Must end with '.com' '.org', or '.net'
# Must not be longer than 254 characters
# Must start and end with a letter or dight



# step 1 : clean the data

email = " user@gmai.com "
email = email.strip()
valid = True

if email == "":
    print("Email cannot be empty")
    valid = False
if not("." in email and '@' in email):
    print("Email must contain . and @")
    valid = False
if email.count("@") != 1:
    print("Email must contain exacly one @.")
    valid = False
if not email.endswith(('.com', '.org', '.net')):
    print("Email must end with .com, .org, or .net")
    valid = False
if len(email) > 256:
    print("Email must not be longer than 256 character")
    valid = False
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or dight")
    valid = False
if valid:
    print("Email is valid.")
