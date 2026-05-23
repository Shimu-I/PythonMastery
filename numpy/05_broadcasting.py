# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape
# example: (4 x 3) x (1 x 3) = (4 x 3)

# The dimensions have the same size.
# OR
# One of the dimensions has a size of 1.


import numpy as np

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([
    [1],
    [2],
    [3],
    [4]
])

array3 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print(f"array1 shape: {array1.shape}")
print(f"array2 shape: {array2.shape}")
print(f"Array multiplication: \n{array1 * array2}")

print("=" * 30)

print(f"array3 shape: {array3.shape}")
print(f"array2 shape: {array2.shape}")
print(f"Array multiplication: \n{array3 * array2}")


# # Wrong
# (1, 4)
# (4, 2)
# # does not work
# (4, 4)
# (4, 2)
# # does not work

print("=" * 30)

#==============================
# Exercise
#==============================

# create a multiplication table via broadcasting
array5 = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ])
array6 = np.array([
    [1], 
    [2], 
    [3], 
    [4], 
    [5], 
    [6], 
    [7], 
    [8], 
    [9], 
    [10]
    ])

print(f"array5 shape: {array5.shape}")
print(f"array6 shape: {array6.shape}")

print(f"Multiplication Table: \n{array5 * array6}")
