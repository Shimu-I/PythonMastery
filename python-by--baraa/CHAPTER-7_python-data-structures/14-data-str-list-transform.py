print("-" * 30)
# ------------------------
# map - does data transformation
# ------------------------

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
print(list(map(str.upper, letters)))

for i in map(str.upper, letters):
    print(i)

number = ['1', '2', '3']
print(list(map(int, numbers)))

names = [' Maria', 'John ', ' Kumar']
# print(list(map(str.strip, names)))

for n in map(str.strip, names):
    print(n)
