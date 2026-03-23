# For loop
# do someting for each item
# sequence can be tuple, list, string, range, file, dictionary --> any object file that is iterable we can use it in for loop
# range(start, stop, step)


for i in (1, 2, 3, 4, 5):
    print(f"Round: {i}")

print("=" * 30)
items = (1, 2, 3, 4, 5)
for item in items:
    print(f"Round: {item}")


print("=" * 30)
items = [1, 2, 3, 4, "Hi"]
for item in items:
    print(f"Round: {item}")

print("=" * 30)
items = "Pyt hon"
for item in items:
    print(f"Round: {item}")


print("=" * 30)
for item in range(1, 10, 2):
    print(f"Round: {item}")

print("=" * 30)
# even numbers
for item in range(1, 10, 2):
    print(f"Round: {item}")

print("=" * 30)
# odd numbers
for item in range(2, 10, 2):
    print(f"Round: {item}")


# for loop usage: for aggregate data like summing, counting, or averaging
print("-" * 30)
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print("Current Total:", total)
print("Final Total:", total)

# we use for loops to transform data like cleaning data before processing
print("-" * 30)
files = [' Report.csv', 'DATA.csv ', ' final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing {file}")

print("-" * 30)
