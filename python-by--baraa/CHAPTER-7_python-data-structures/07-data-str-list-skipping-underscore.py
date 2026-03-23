# sking value and the data is not storeing in the memory
# this optimize the memory spaces

person = ['Maria', 29, 'Data Engineer', 'Spain']

name, _, role, _ = person

print(name)
print(role)

print("-" * 30)

person = ['Maria', 29, 'Data Engineer', 'Spain']

name, *_, country = person

print(name)
print(country)


print("-" * 30) 
*_, country = person
print(country)

