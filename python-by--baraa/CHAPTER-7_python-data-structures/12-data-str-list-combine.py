# Combining lists
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = letters + numbers
print(comb)
print(letters * 2)
comb = [letters, numbers]
print(comb)


print("*" * 30)
# change one of the list with expand()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)
print(numbers)


print("*" * 30)
# Combining using zip()
# output of zip is iterator if we output this we will get a weird number
# to prevent that can convert the iterator into list
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
comb = list(zip(letters, numbers))
comb1 = list(zip(letters, numbers, "Hi"))
print(comb)
print(comb1)

# example for zip
ids = [101, 102, 103]
names = ['Ali', 'Sara', 'John']
print(list(zip(ids, names)))
