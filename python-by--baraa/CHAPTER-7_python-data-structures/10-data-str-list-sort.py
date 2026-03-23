# list sorting
letters = ['c', 'a', 'b']
# letters.sort()
# print(letters)
# letters.sort(reverse=True)
# print(letters)
# new_list = sorted(letters)
new_list = sorted(letters, reverse=True)
print(letters)
print(new_list)

print('-' * 30)
matrix = [
    ['d', 'e', 'f'],
    ['a', 'z', 'i'],
    ['a', 'a', 'c']
]
# first item of each list
print(matrix)
# matrix.sort()
# print(matrix)
# matrix[1].sort()
print(matrix)

print('*' * 30)
# Reversing the list

letters = ['c', 'a', 'b']
# letters.reverse()
# new_list = reversed(letters) # new list is not created instade a new object of iterator is created
new_list = list(reversed(letters))
print("Original Lis: ", letters)
print("Reversed List: ", new_list)

