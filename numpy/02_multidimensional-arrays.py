import numpy as np

array = np.array('A')

print(f"Zero Dimention array: {array.ndim}")

print("=" * 30)

array = np.array(["A", "B", "C"])

print(f"One Dimention array: {array.ndim}")

print("=" * 30)

array = np.array(
    [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ]

)
print(f"Two Dimention array: {array.ndim}")
print("=" * 30)

array = np.array([
    [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ],

    [
        ["J", "K", "L"],
        ["M", "N", "O"],
        ["P", "Q", "R"]
    ],

    [
        ["S", "T", "U"],
        ["V", "W", "X"],
        ["Y", "Z", "_"]
    ]
]

)

print(f"Three Dimention array: {array.ndim}")
print(f"Array shape: {array.shape}")


print("=" * 30)

#===============================
# Chain indexing
#===============================

print(f"Array Chain indexing: {array[0][0][0]}")

# Multidimentional indexing > Chain indexing
# in term of speed

#===============================
# Multidimentional indexing
#===============================

print(f"Array Multidimentional indexing: {array[0, 0, 0]}")



#===============================
# Print a word
#===============================

word = array[2, 0, 0] + array[0, 2, 1] + array[0, 2, 2] + array[1, 1, 0] + array[2, 0, 2]
print(f"5 Letter word: {word}")




