import pandas as pd

#===================================
# How to import CSV and JSON files
#===================================

# CSV = Comma-seperated values
# JSON = JavaScript Object Notation

df = pd.read_json("/home/shimu/Documents/PythonMastery/pandas/pokemon.json")

#print(df)

# Print entire data frame

# Be careful with Big data

print(df.to_string())

