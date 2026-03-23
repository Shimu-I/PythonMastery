# We also somethimes call this ternary operator
# In this case the ELSE is must included
# Can't use ELIF in here
# Can only be used if the logic is simple

score = 100

grade = "A" if score >= 90 else "F"
print(grade)

grade = ("A" if score >= 90 
         else "B" if score >= 80 
         else "F")
print(grade)