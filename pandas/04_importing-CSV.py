import pandas as pd

#===================================
# How to import CSV and JSON files
#===================================

# CSV = Comma-seperated values
# JSON = JavaScript Object Notation

df = pd.read_csv("/home/shimu/Documents/PythonMastery/pandas/pokemon.csv")

# print(df)

# Print entire data frame

# Be careful with Big data

print(df.to_string())

# by default python print the first 5 rows and last 5 rows

