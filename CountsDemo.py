counts = dict()
supplies = open('items.txt')
for types in supplies:
    type(str(types))
print(types)
supply = types.split(',')
for name in supply :
    counts[name] = counts.get(name,0) + 1
    print(counts)