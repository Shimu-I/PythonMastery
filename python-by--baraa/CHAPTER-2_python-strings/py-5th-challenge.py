text = "968-Maria, ( D@t@ Engineer ) ;; 27y  "

name = text[4:9]
print(name)
role = text[13:26].strip().replace("@", "a")
print(role)

age = text[-5:-3]
print(age)

print(f"name: {name} | role: {role} | age: {age}")
