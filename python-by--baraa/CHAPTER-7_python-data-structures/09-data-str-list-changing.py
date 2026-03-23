# Real life the data are changing countinuously overtime
# 3 type of changes

# new
# remove
# update

# changing list - add item
# append() - add list at the very end of old list
letters = ['a', 'b', 'c']
print(letters)
letters.append('x')
print(letters)
letters.append('y')
print(letters)

print('-' * 30)
# insert(index, value) - any place of the list -- flexable and control

letters2 = ['a', 'b', 'c']
letters2.insert(0, 'x')
print(letters2)
letters2.insert(3, 'y')
print(letters2)

print('-' * 30)
# adding in matrix
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

print(matrix)
matrix.append(['x', 'y', 'z'])
print(matrix)
matrix.insert(0, ['a', 'a', 'a'])
print(matrix)
matrix[1].append('x')
print(matrix)
matrix[0].insert(0, 'z')
print(matrix)


print('-' * 30)
# Remvoe data form the list
# clear() - remvoe all items

list1 = ['a', 'b', 'c']
list1.clear()
print(list1)

# remove('value') - first occurance
letters1 = list1 = ['a', 'b', 'c']
letters1.remove('a')
print(letters1)

# pop(position) - remove by position if the position is not given by defalut is always the last item - and also remove the return the item it removed
letters2 = list1 = ['a', 'b', 'c']
removed = letters2.pop(1)
print('Removed: ', removed)
print(letters2)

# remove form matrix
matrix1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
print(matrix1)
# matrix1.remove(['a', 'b', 'c'])
# print(matrix1)
# matrix1.pop()
# print(matrix1)

matrix1[1].remove('e')
print(matrix1)
matrix1[-1].pop(0)
print(matrix1)


print('-' * 30)
# Update the list
letters2 = ['a', 'b', 'c']
letters2[0] = 'x'
print(letters2)
letters2[1] = 'y'
print(letters2)
letters2 = 'z'
print(letters2)
print(type(letters2))

# update the matrix
matrix2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
print(matrix2)
matrix2[2] = ['x', 'y', 'z']
print(matrix2)
matrix2[0][0] = '-'
print(matrix2)
matrix2[1][1] = '-'
print(matrix2)
matrix2[-1][-1] = '-'
print(matrix2)
