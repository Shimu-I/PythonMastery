import pandas as pd

# Series = A Pandas 1-Dimensional labeled array that can hold any data type 
#          Think of it like a single column in a spreadsheet (1-Dimensional)


data = [100, 102, 103]
data1 = [100.0, 102.0, 103.0]
data2 = ["A", "B", "C"]
data3 = [True, False, True]


# adding new label
series = pd.Series(data, index=['a', 'b', 'c'])
series1 = pd.Series(data1)
series2 = pd.Series(data2)
series3 = pd.Series(data3)

print(series)
print("=" * 20)
print(series1)
print("=" * 20)
print(series2)
print("=" * 20)
print(series3)


# =======================
# access series value
# =======================
print("=" * 20)
# loc = location by label

print(series.loc['a'])

series.loc['a'] = 300
print(series)

# iloc = location by integer position
print(series.iloc[2])


# =======================
# filter by value
# =======================
print("=" * 20)

data_4 = [100, 102, 104, 200, 202]
series_4 = pd.Series(data_4, index=["a", "b", "c", "d", "e"])

print(series_4[series_4 >= 200])

# =======================
# how many calories eaten by a day
# =======================
print("=" * 20)

calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700
}

series_5 = pd.Series(calories)
print(series_5)

series_5.loc["Day 3"] += 500
print(series_5.loc['Day 3'])
print(series_5)


 # the day i stick to my diet

print(series_5[series_5 < 2000])