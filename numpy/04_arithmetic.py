import numpy as np

# ===========================
# Scalar arithmetic
# ===========================
# scalar = single value
array = np.array([1, 2, 3])

print(f"Addition: {array + 1}")
print(f"Subtraction: {array - 2}")
print(f"Multiplication: {array * 3}")
print(f"Divition: {array / 4}")
print(f"To the power of: {array ** 5}")


print("=" * 30)
# ===========================
# Vectorized math functions
# ===========================
# vector = single dimention

array1 = np.array([1.01, 2.5, 3.99])

print(f"Square Root: {np.sqrt(array)}")
print(f"Round value: {np.round(array1)}")
print(f"Round down: {np.floor(array1)}")
print(f"Round up: {np.ceil(array1)}")


# Constant value
print(f"Content valu of PI: {np.pi}")


# Exercises
# Cricle Area
print(f"Circle area: {np.pi * array ** 2}")


print("=" * 30)
# ===========================
# Element wise arithmetic
# ===========================
# element [] element

array2 = np.array([1, 2, 3])
array3 = np.array([4, 5, 6])

print(f"Addition: {array2 + array3}")
print(f"Subtraction: {array2 - array3}")
print(f"Multiplication: {array2 * array3}")
print(f"Division: {array2 / array3}")
print(f"To the power: {array2 ** array3}")


print("=" * 30)
# ===========================
# Comparison operators
# ===========================
# [boolean array, filtered data, element wise comparison]

scores = np.array([91, 55, 100, 73, 82, 64])

print(f"Prefect score: {scores == 100}")
print(f"Passing score: {scores >= 100}")
print(f"Failing score: {scores < 100}")


scores[scores < 60] = 0
print(scores)
