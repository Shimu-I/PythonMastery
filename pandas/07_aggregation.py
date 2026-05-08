# Affregate functions = Reduce a set of value into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function

import pandas as pd

df = pd.read_csv("/home/shimu/Documents/PythonMastery/pandas/pokemon.csv")

# ==========================
# 1. Apply to whole data frame (all columns)
# ==========================
# MEAN, SUM, MIN, MAX, COUNT
print("=" * 40)

# Get Mean value of all numeric columns
print(df.mean(numeric_only=True))

# Get Sum of all numeric columns
print(df.sum(numeric_only=True))

# Get MIN of all numeric columns
print(df.min(numeric_only=True))

# Get MAX of all numeric columns
print(df.max(numeric_only=True))

# Count the number of value in each column
print(df.count())

# ==========================
# 2. Apply to single column
# ==========================
# these single column is already numeric so no need to write numaric_only

print("=" * 40)

print(df["Height"].mean())
print("-" * 40)

print(df["Height"].min())
print("-" * 40)

print(df["Height"].sum())
print("-" * 40)

print(df["Height"].max())
print("-" * 40)

print(df["Type2"].count())


# ==========================
# 3. group by
# ==========================

print("=" * 40)

group = df.groupby("Type1")

print(group["Height"].mean())

print("-" * 40)
print(group["Height"].sum())

print("-" * 40)
print(group["Height"].min())

print("-" * 40)
print(group["Height"].max())
print("-" * 40)
print(group["Height"].count())
