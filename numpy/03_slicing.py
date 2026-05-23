import numpy as np

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print(array)

print("=" * 20)
# array[start:end:step]
# ==========================
# Row Selection
# ==========================


print(f"Print row: {array[0]}")
print(f"Print 3 rows: \n{array[0:3]}")
print(f"With step: \n{array[0:4:2]}")
print(f"Single row: {array[0]}")
print(f"All rows step 2: \n{array[::2]}")
print(f"Reverse order matrix: \n{array[::-1]}")
print(f"All rows step 2 Reverse: \n{array[::-2]}")


print("=" * 30)
# ==========================
# Column Selection
# ==========================

print(f"Single column: {array[:, 2]}")
print(f"Last column: {array[:, -1]}")
print(f"Print first 3 column: \n{array[:, 1:4]}")
print(f"Setting the step: \n{array[:, 1::2]}")
print(f"Reverse column: \n{array[:, ::-1]}")


print("=" * 30)
# ==========================
# COMBINE both Row and Column Selection
# ==========================

print(f"First two row, first two column: \n{array[0:2, 0:2]}")

print(f"First two row, last two column: \n{array[0:2, 2:]}")

print(f"Last two row, first two column: \n{array[2:, 0:2]}")

print(f"Last two row, last two column: \n{array[2:, 2:]}")
