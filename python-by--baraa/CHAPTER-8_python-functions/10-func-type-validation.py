# 2. Validation Function
# to protect your system form bad data
# alternative names
# checker function

# TASK - 1
print("*" * 30)
print("--------TASK - 1 --------")
# check whether the password meets the minimum requirement of 8 characters


def is_valid_password(password):
    return len(password) >= 8


print(is_valid_password("123456"))
print(is_valid_password("123456789"))


# TASK - 2
print("*" * 30)
print("--------TASK - 2 --------")
# check whether an email has a basic valid format.


def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("sara@gmail.com"))
print(is_valid_email("saragmail.com"))
print(is_valid_email("sara@gmailcom"))
print(is_valid_email("saragmailcom"))

