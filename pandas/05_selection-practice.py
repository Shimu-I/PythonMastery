# Different selection type

import pandas as pd

df = pd.read_csv(
    "/home/shimu/Documents/PythonMastery/pandas/pokemon.csv", index_col="Name")


pokemon = input("Enter a Pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} no found")