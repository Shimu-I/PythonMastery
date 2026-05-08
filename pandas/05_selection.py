# Different selection type

import pandas as pd

df = pd.read_csv(
    "/home/shimu/Documents/PythonMastery/pandas/pokemon.csv", index_col="Name")


# ==============================
# SELECTION by column
# ==============================

# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[
#     ["Name", "Weight", "Height"]
# ].to_string())


# ==============================
# SELECTION by ROWS
# ==============================

print(df.loc["Dragonite"])

print("=" * 30)

# single row information
print(df.loc["Charizard", ["Height", "Weight"]])

print("=" * 30)

# multi row information
print(df.loc["Moltres":"Mewtwo", ["Height", "Weight"]])

print("=" * 30)

print(df.iloc[0:11:2, 0:3])
