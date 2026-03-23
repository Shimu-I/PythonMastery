# 3. Orchestrator Function
# alternative names
# work flow function
# controller funtion
# pipeline function
# coredinator function

# Project
print("*" * 30)
print("--------Project - 1 --------")
# project requirement
# 1. receive an email form the user
# 2. validate the email
# 3. if it is invalid, log an error in a file
# 4. if it is valid, clean and structure the email
# 5. log each step of the program


# action funtion
def write_log(message):
    with open("CHAPTER-8_python-functions/app.log", "a") as file:
        file.write(message + "\n")

# validation funtion
def is_valid_email(email):
    return "@" in email and "." in email

# transformation funtion
def clean_and_split_email(email):
    cl_email = email.strip().lower()
    username, domain = cl_email.split("@")
    return {
        "username": username,
            "domain": domain
            }




# process of calling other function this is orchestration
# correct order of calling other funtion
# ORCHESTRATOR Function
def process_user_email(email):
    write_log("App Started")
    # 2. validate the email
    # 3. if it is invalid, log an error in a file
    if not is_valid_email(email):
        write_log(f"Invalid Email received: {email}")
    # 4. if it is valid, clean and structure the email
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email: {clean_email}")
    write_log("App stopped")
    # 5. log each step of the program


 # 1. receive an email form the user
email = input('Please enter your email: ')
process_user_email(email)