import pandas as pd

# DataFrame = A tabular data structure with rows AND columns. (2Dimensional)
#             Similar to an Excel spreadsheet

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

print(df)

print("=" * 40)

print(df.loc['Employee 2'])

print("=" * 40)

print(df.iloc[0])

# ===========================
# ADD a new column
# ===========================
# number of values must match the number or rows
print("=" * 40)

df['Job'] = ["Cook", "N/A", "Cashier"]
print(df)

# ===========================
# ADD a new row
# ===========================
# easy way create a df then concatinate
print("=" * 40)

new_row = pd.DataFrame([
    {"Name": "Sandy", "Age": 28, "Job": "Engineer"},
    {"Name": "Lily", "Age": 20, "Job": "Scientist"}
], index=["Employee 4", "Employee 5"])

df = pd.concat([df, new_row])

print(df)
