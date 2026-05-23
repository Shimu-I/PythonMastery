# Filtering = Refers to the process of selecting elements
#            form an array that match a given condition

import numpy as np

ages = np.array([
    [21, 17, 19, 20, 16, 30, 18, 65],
    [39, 22, 15, 99, 18, 19, 20, 21]

])


# Boolean indexing -- does not preserve shape - faster
teenagers = ages[ages < 18]  # boolen indexing
adults = ages[ages >= 18]
adults1 = ages[(ages >= 18) & (ages < 65)]
adults2 = ages[(ages < 18) | (ages >= 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]


print(f"Teenagers: {teenagers}")
print(f"Adults: {adults}")
print(f"Adults2: {adults2}")
print(f"Seniors: {seniors}")
print(f"Even ages: {evens}")
print(f"Odd ages: {odds}")


print("=" * 30)
# where function -- preserve shape - slower

# where(condition, array, replacement)
adults = np.where(ages >= 18, ages, 0)
print(adults)
