# keep only students with names starting with 'M'

students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]

print(list(filter(lambda row: row[0].startswith('M'), students)))