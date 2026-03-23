# List Comprehension
# loop + Transformation + Filtering

# the serial is: loop -> filter -> transformation

# filtering is optional


# Data transformation + Filtering
# Only Data transformation
# Only Data filtering

domains = [
    'www.google.com',
    'openai.com',
    'localhost',
    'www.DATAWITHBARAA.COM'
]

cleaned = [
    d.lower().replace('www.', '')  # data transformation
    for d in domains               # data looping
    if '.' in d                    # data filtering
]

print(cleaned)



cleaned = [
    d                              # NO data transformation
    for d in domains               # data looping
    if '.' in d                    # data filtering
]

print(cleaned)