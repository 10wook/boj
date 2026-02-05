input = str(input())
change = {'c=': 'x', 'c-': 'y', 'dz=': 'z', 'd-': 'w', 'lj': 'a', 'nj': 'b', 's=': 'c', 'z=': 'd'}
for key, value in change.items():
    input = input.replace(key, value)
print(len(input))