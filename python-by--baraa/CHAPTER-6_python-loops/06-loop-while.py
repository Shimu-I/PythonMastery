# Repeats a block of code - over and over as long as condition True!

# We define our own loop

# while has two condition

# 1. while Condition
# 2. While True



# 1. while condition usage case-------------------
# TASK 1 : Build a counter from 1 to 5
print("-" * 30)
count = 1
while count <= 5:
    print(count)
    count += 1


# TASK 2 : Write a program that keeps asking "Do you Agree?" until the user types "yes"

answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no):")
print('Thank you!')



# 2. While True ------------------------
# most powerful and most risky
# this loop is infinite
# while True:
#     print("I'm unstoppable!")

answer = ""
while True:
    answer = input("Do you agree?(yes/no):")
    if answer == "yes" :
        break
print('Thank you!')