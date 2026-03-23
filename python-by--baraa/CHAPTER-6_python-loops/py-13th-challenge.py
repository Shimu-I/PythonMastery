# while True:
#     answer = input("Do you agree? (yes/no):")
#     if answer == "yes":
#         break
# print("Thank You")

# REQUIREMENTS
# Allow up to 3 attempts
# if the user types "yes", print "Glad" we are on the same page"
# Otherwise, print "3 Strike, You are Oue!"

attempts = 1
while attempts <= 3:
    answer = input("Do you agree? (yes/no):")
    if answer == "yes":
        print("Glad we are on the same page")
        break
    attempts += 1
else:
    print("3 Strikes, You are Out!")

