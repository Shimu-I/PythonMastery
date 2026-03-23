# string function - searching

phone = "+49-176-12345"
print(phone.startswith("+49"))

email = "shimu@outlook.com"
print(email.endswith("gmail.com"))

file = "data_backup.csv"
print(file.endswith(".csv"))

print("@" in email)

url = "https://api.company.com/v1/data"
print("/api" in url)

# search with find() method

phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"
print(phone1[phone.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])
