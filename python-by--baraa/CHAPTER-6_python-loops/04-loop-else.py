# this is not if else
# this is for else


items = [1, 3, 4, 7]
for i in items:
    print(i)
else:  # useless
    print("END")


print("-"*10)
# else is useless unless we combine it using break
# here is has a use case whether we iterate through every one or we encounter intruption
items = [1, 3, 4, 7]
for i in items:
    print(i)
    if i % 2 == 0:
        print("Even numm found", i)
        break
else:
    print("ALL the numbers are odd")


# for else usage
# search and validate

print('=' * 30)
print("TASK-1")
# check for missing names in a list

names = ['Kamara', 'Tuba', None, 'Monika']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are avaiable")


print('=' * 30)
print("TASK-2")
# check if all files are CSV files

files = ['file1.csv', 'file2.pdf','data2.txt', 'file3.csv']
for file in files:
    if not file.endswith('.csv').endswith():
        print(f"{file} is not a CSV")
        break
else:
    print("All the files are CSV")
