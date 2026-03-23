# When to stop(break), skip(continue), pass(pass)

# Break statement
names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        print("Empty value detected!")
        break
    print(f"Name = {name}")

print("-"*30)
# Continue statement
# just skiping the current round ang go to the start
names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        print("Empty value detected!")
        continue
    print(f"Name = {name}")


print("-"*30)
# pass statement
# it is a placeholder where nothing happeans
# for now just keep going do nothing
names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        pass #toto: Handle Empty value
    print(f"Name = {name}")

print('-'*10)
# when i think i am ready to write the code
names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        name = name.replace('', 'unknown')
    print(f"Name = {name}")