for x in range(3):
    for y in range(2):
        for z in range(2):
            print(f"({x}, {y}, {z})")


# nested loops use cases
# we have two major use cases
# 1. Crossing or Combining Data o pairing data
# 2. Navigate Hierarchy

colors = ['red', 'blue', 'green']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f'{color} - Size {size}')


# Example: we have to create multiple report for each year and each date
years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 29)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")


# Example : we navigate through tables and columns
# SELECT count(*) FROM customers where id is NULL;

tables = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']

for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM {t} WHERE {c} is NULL")