
# Iterator
# ------------------------
# Itertors & Iterables
# ------------------------

# why do we need iterators
# mainly for 3 reasons

# 1. looping
# 2. save memory - one data at a time
# 3. for speed ans flexibility

# Iterator - This is the process or machine
# Iterable - List that can be loop over

letters = ['a', 'b', 'c']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)


print("-" * 30)
# ------------------------
# enumorate Reveresed zip
# ------------------------
# it return two items (position and value)
letters = ['a', 'b', 'c']
print(list(enumerate(letters)))
print(list(enumerate(letters, start=1)))
for index, value in enumerate(letters):
    print(index, " ", value)

print(list(reversed(letters)))
for index in reversed(letters):
    print(index)

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
print(list(zip(letters, numbers)))
for i, j in zip(letters, numbers):
    print(i, " ", j)




