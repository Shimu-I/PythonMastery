# methods of set
a = {10, 20, 30, 40}

a.add(50)
print(a)

a.update("Hi")
a.update({1, 2}) # add several value at once
# alternative for update
a |= {3, 4}
print(a)

a.remove(10)
print(a)

# if the removed item is not in the set it will give error

# safest way to remove is discard
a.discard(100) # for unexisting value nothing happens better than remove()
print(a)
a.pop() # remove totally random number not reliable