# Aggriegate functions = summarize data and typically
#                        return a single value


import numpy as np

array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(f"Sum of total values: {np.sum(array)}")
print(f"Average: {np.mean(array)}")
print(f"Standard deviation: {np.std(array)}")
print(f"Standard deviation ** 2: {np.var(array)}")
print(f"Minimum value: {np.min(array)}")
print(f"Maximum value: {np.max(array)}")
print(f"Minimum value position: {np.argmin(array)}")
print(f"Maximum value position: {np.argmax(array)}")

# sum all columns
print(f"All columns sums: {np.sum(array, axis=0)}")
# sum all rows
print(f"All rows sums: {np.sum(array, axis=1)}")

