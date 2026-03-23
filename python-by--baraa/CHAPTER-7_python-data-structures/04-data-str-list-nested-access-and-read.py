# Nested access and read

matrix = [
    ['a', 'b', 'c'], # Row 0
    ['d', 'e', 'f'], # Row 1
    ['g', 'h', 'i']  # Row 2
]

print(matrix)
print(matrix[2])
print(matrix[-1][-1])
print(matrix[0][0])
print(matrix[1][1])

# slicing

lst = ['a', 'b', 'c', 'd']
print(lst)
print(lst[0])
print(lst[-1])
print(lst[-2])
print(lst[:2])
print(lst[2:])
print(lst[:])

# slicing for the matrix
print(matrix[:2])
print(matrix[1:])
print(matrix[2][:2])