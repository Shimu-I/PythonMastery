# SET's relationships method

# to check the quality of data we use subset and superset

a = {30, 40}
b = {30, 40, 50, 60}
c = {20, 90}


print(a.issubset(b)) # a small and b bigger
print(b.issubset(a)) 

print(b.issuperset(a)) # b bigger and a smaller

print(a.isdisjoint(b)) # has similarity
print(a.isdisjoint(c)) # no similarity