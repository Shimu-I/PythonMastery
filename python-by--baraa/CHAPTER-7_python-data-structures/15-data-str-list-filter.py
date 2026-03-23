print("-" * 30)
# ------------------------
# filter
# ------------------------

letters = ['a', '', 'b', None, 'c', False]
print(list(filter(None, letters)))  # all  invlaid data filtered
print(list(filter(bool, letters)))  # all false value is filtered
# both has same effect

items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items)))

for i in filter(str.isalpha, items):
    print(i)


print("-" * 30)
# ------------------------
# Lambda - custom logic (Anonymous Function)
# ------------------------
# can have expression or conditions
def multiple(x): return x*2
print(multiple(2))

def add(x, y): return x + y
print(add(1, 2))

def check(i): return i in "python"
print(check("n"))



print("-" * 30)
# ------------------------
# Lambda + Map
# ------------------------

prices = ['$12.50', '$9.99', '$100.00']

print(list(map (lambda p : float(p.replace('$', '')), prices)))

p = '$12.50'
print(type(float(p.replace('$', ''))))



print("-" * 30)
# ------------------------
# Lambda + Filter
# ------------------------
prices = [120, 30, 300, 80]
# priecs >= 100

print(list(filter(lambda p: p >= 100, prices)))

students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]

#print(students[x][y] > 70)
print(list(filter(lambda row: row[1] > 70, students)))