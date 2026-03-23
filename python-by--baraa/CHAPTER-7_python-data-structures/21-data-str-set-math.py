# Mathematical operations in SET

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print(a.union(b))  # not changeing original
print(a | b)  # similar result

# for sheared item
print(a.intersection(b))
print(a & b)  # similar result


# show me the items only the first set
print(a.difference(b))
print(a - b)  # same reslut
print(b - a)

# for NOT sheared value
print(a.symmetric_difference(b))
print(a ^ b) # same result
