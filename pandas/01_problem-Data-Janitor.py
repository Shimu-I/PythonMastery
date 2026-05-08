
# Task 1: Import
import pandas as pd

df = pd.read_csv(
    "/home/shimu/Documents/PythonMastery/pandas/store_inventory.csv")


# Task 2: Remove Duplicate
df = df.drop_duplicates()

# Task 3: Fix inconsistency
df["Category"] = df["Category"].replace({"ELECTRO-NICS": "Electronics"})

# Task 4: Handle Missing Values
mean_value = df["Price"].mean(numeric_only=True)
print(mean_value)
df.loc[10, "Price"] = round(mean_value, 2)

# Task 5: Fill the missing value
df = df.fillna({"Quantity": 0})


# Task 6: Standrize Text
df["Product"] = df["Product"].str.lower()


# Task 7: Type Casting
df["In_stock"] = df["In_Stock"].astype(bool)
print(df.to_string())