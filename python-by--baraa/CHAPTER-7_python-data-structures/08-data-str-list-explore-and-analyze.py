# explore and analyze
numbers = [1, 5, 5, 4, 3]

print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))

# all and any function
print("-" * 30)
print("All:", all(numbers))
print("All:", all([1, 0, 2]))
print("All", all(['a', '', 'b']))
print("All:", all(['a', 'c', 'b']))

print("-" * 30)
print("Any:", any(numbers))
print("Any:", any([1, 0, 2]))
print("Any", any(['a', '', 'b']))
print("Any:", any(['a', 'c', 'b']))
print("Any:", any([0, 0, 0]))


# count a item
print("-" * 30)
print("Count: ", numbers.count(5))

# index if a item
print("Index: ", numbers.index(5))

# Analysis and Checks
numbers = [1, 5, 5, 4, 3]
print(8 not in numbers)


print("-" * 30)
# operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)

list1 = [5, 8, 3]
list2 = [5, 2, 3]
print(list1 < list2)

list1 = [5, 8, 3]
list2 = [5, 8, 3]
print(list1 is list2)



