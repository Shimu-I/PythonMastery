# Difference bewteen the BREAK and CONTINUE

# Loop through a list of days and print only the working days skipping the weekends
print("-" * 40)
print("TASK-1")
days = ["Mon", "Sun", "Wed", "Tue"]
weekends = ["Sat", "Sun"]
for day in days:
    if day in weekends:
        continue
    print(F"Workkday: {day}")


print("-" * 40)
print("TASK-2")
# Scan emails to block unsafe data from entering your system

emails = [
    'data@gmail.com',
    'baraa@gmail.com',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]
for email in emails:
    if ';' in email:
        print("SQL Injection: Hacker Attack")
        break
    print(f'Processing Email: {email}')