

# copying list
# Copying list assignments =

import copy
letters = ['a', 'b', 'c']
letters_copy = letters
letters_copy.append('z')
letters_copy.pop()
print("Original:", letters)
print("Copy:", letters_copy)


print("*" * 30)
# Shallow COPY - first level indepedent and others are referecne
letters = ['a', 'b', 'c']
letters_copy = letters.copy()
letters_copy.append('z')
letters.pop()
print("Original:", letters)
print("Copy:", letters_copy)

print("*" * 30)

matrix = [
    ['d', 'e'],
    ['a', 'z']
]
# first item of each list
print(matrix)
matrix_copy = matrix.copy()
# changes can be seen in both in the original and copied version
matrix_copy[0].append('z')
matrix.pop()
print("Original:", matrix)
print("Copy:    ", matrix_copy)


print("*" * 30)
# Deep COPY - safest one
# need importing copy

matrix = [
    ['a', 'b'],
    ['c', 'd']
]

print(matrix)
# matrix_copy = copy.copy(matrix) # exacly the shallow copy
matrix_copy = copy.deepcopy(matrix)
matrix_copy[0].append('z')
matrix.pop()
print("Original:", matrix)
print("Copy:    ", matrix_copy)


print("*" * 30)
# Testing is Operator
original = [
    ['a', 'b'],
    ['c', 'd']
]

# assignment
copy1 = original
print("Same Object?", original is copy1, "\n")
# shallow copy
copy2 = original.copy()
print("Same Object?", original is copy2)
print("Shared Lists?", original[0] is copy2[0])

print()
# deep copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)
print("Shared Lists?", original[0] is copy3[0])