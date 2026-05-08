# Data clearning = The process of fixing/removing:
#                  incomplete, incorrect, or irrelevant data.
#                 ~75% of work done with Pandas in data cleaning


import pandas as pd

df = pd.read_csv("/home/shimu/Documents/PythonMastery/pandas/pokemon.csv")

# ========================================
# Drop Irrelevant Columns
# ========================================

# drop() create a new dataframe so keeping in the same df
# df = df.drop(columns=["Legendary", "No"])
# print(df)


# ========================================
# 1. Handle Missing Data
# ========================================
# dropna = Drop Not Available

# df = df.dropna(subset=["Type2"])
# print(df)

# fillna = Fill any not available values
# df = df.fillna({"Type2": "None"})

# print(df.to_string())


# ========================================
# 2. Fix any inconsistent values
# ========================================


df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                   "Fire": "FIRE",
                                   "Water": "WATER"})


# ========================================
# 3. Standardize text
# ========================================

df["Name"] = df["Name"].str.lower()



# ========================================
# 4. Fix data types
# ========================================

df["Legendary"] = df["Legendary"].astype(bool)


# ========================================
# 5. Remove duplicate values
# ========================================

df = df.drop_duplicates()
print(df.to_string())