# Data transformation

# replace() method
price = "1234,56"
print(price.replace(",", "."))

phone = "176-1234-56"
print(phone.replace("-", "/"))

phone = "176-1234-56"
print(phone.replace("-", ""))

price = "$1,299.99"
print(price.replace("$", "").replace(",", ""))

# + or data concatenation of string
first_name = "Michael"
last_name = "Scott"
last_name = first_name + "-" + last_name
print(last_name)

folder = "C:/Users/Shimu/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)

# f-string
name = "Sam"
age = 34
is_student = False
print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student)) 

print(f"My name is {name}, I am {age} years old, and student status is {is_student}")

print(f"2 + 3 = {2 + 3}")

print(f"{{This is me}}")

# method split() 
stamp = "2026-09-20 14:30"
print(stamp.split(" "))

stamp = "2026-09-20"
print(stamp.split("-"))

csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(','))

# String Repetition
print("ha" * 3)
print("-" * 10)
print("+" * 30)

# Data Extraction (Indexing & Slicing)
text = "Python"

#  extract the first character
print(text[0])
print(text[-6])

#  extract the last character
print(text[5])
print(text[-1])

# extrach h
print(text[3])

date = "2026-09-20"
# extrac the year
print(date[0:4])
print(date[:4])

# extract the month
print(date[5:7])

# extract the date
print(date[8:])
print(date[-2:])