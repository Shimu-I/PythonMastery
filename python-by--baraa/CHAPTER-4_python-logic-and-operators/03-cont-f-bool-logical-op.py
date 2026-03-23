# Logical operators
print(3 > 1 and 5 < 1)
print(3 > 1 and 5 > 1)

print(3 > 1 or 5 < 1)
print(3 < 1 or 5 < 1)

# checks if the system is under pressure
cpu_usage = 90
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)

#Checking usre credentials before login
email = True
password = False
print(email and password)


# Not operator

print(not 3 > 2)
print(not True)
print(not False)
print(not not False)


name = ""
print(not name)
print(not 0)


# TASK
# Allow access only if the user is logged in
# or they are guest
# but they must not banned

is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned)



