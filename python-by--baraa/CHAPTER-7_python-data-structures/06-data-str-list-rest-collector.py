# Rest collector
# Asterisk *
# We are only allowed to use one * one time

# first [*details] end
person = ['Maria', 29, 'Data Engineer', 'city', 'Spain']

name, *details, country = person

print(name)
print(details)
print(country)


print('-' * 30)

# first [*details]
person = ['Maria', 29, 'Data Engineer', 'city', 'Spain']
name, *details = person

print(name)
print(details)

print('-' * 30)
# [*details] end
person = ['Maria', 29, 'Data Engineer', 'city', 'Spain']
*details, country = person

print(country)
print(details)

print('-' * 30)
# [*details] 2nd-last-end ,end
person = ['Maria', 29, 'Data Engineer', 'city', 'Spain']
*details, city, country = person

print(country)
print(city)
print(details)


# SOME RULE FOR USING *
# variable must match the exact number of value not more not less
numbers = [1, 2, 3, 4]

first, second, third, fouth = numbers
first, *rest = numbers

# *Asterisk collects leftovers, and it's find if there are none
numbers = [1]
first, *rest = numbers

print(first)
print(rest)

# It works with any thing that has a sequence like lists, tuples, strings, etc.

numbers = "hi"

first, *rest = numbers
print(first)
print(rest)
