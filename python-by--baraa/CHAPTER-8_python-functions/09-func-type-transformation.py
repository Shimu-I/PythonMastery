# 2. Transformation function
# Alternative names for this function
# Utility
# Calculation
# Mapper
# Data function

# TASK - 1
print("*" * 30)
print("--------TASK - 1 --------")
# cleans email addresses and splits then into structure data (username and domain)


def clean_and_split_email(email):
    cl_email = email.strip().lower()
    # sara@gmail.com
    username, domain = cl_email.split("@")
    return {
        "username": username,
            "domain": domain
            }


print(clean_and_split_email("  SaRa@gmail.com"))
