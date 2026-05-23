import numpy as np


# ============================
# Integer numbers
# ============================


rng = np.random.default_rng()
print(f"Integer random number: {rng.integers(1, 101)}")

print(
    f"Integer random number with keyword param: 1D{rng.integers(low=1, high=101, size=3)}")

print(
    f"Integer random number with keyword param: 2D\n{rng.integers(low=1, high=101, size=(3, 2))}")


print("=" * 30)
# inorder to get same results

rng2 = np.random.default_rng(seed=1)
print(
    f"Integer random number with seed: 2D\n{rng2.integers(low=1, high=101, size=(3, 2))}")


print("=" * 30)
# ============================
# Floating point number
# ============================

# random floating point number between 0 to 1
print(f"Floating random number: {np.random.uniform()}")
print(f"Floating random number:1D {np.random.uniform(low=-1, high=1, size=1)}")
print(
    f"Floating random number: 3D\n {np.random.uniform(low=-1, high=1, size=(3, 2))}")

np.random.seed(seed=1)
print(
    f"Floating random number with seed: 3D\n {np.random.uniform(low=-1, high=1, size=(3, 2))}")


print("=" * 30)
# ============================
# Shuffle an array
# ============================

rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])

print(f"Original: {array}")

rng.shuffle(array)


print(f"Shuffled: {array}")


print("=" * 30)
# ============================
# Random choice
# ============================

rng = np.random.default_rng()

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])

print(f"Original: {fruits}")


fruit = rng.choice(fruits)  # only one
print(f"Choice: {fruit}")

fruits = rng.choice(fruits, size=(3, 3))  # 3 random one
print(f"Choice: /n{fruits}")

# with emojis
fruits1 = np.array(["🍈", "🍉", "🍓", "🍋", "🍑", "🍇", "🫐", "🍏", "🍊"])

fruits1 = rng.choice(fruits1, size=(3,3))
print(f"Fruits: \n{fruits1}")
