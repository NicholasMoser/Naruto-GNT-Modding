# Checks that the address in the first and third spot of each line in a symbol map is identical.

with open('../general/symbol_maps/RNEEDA.map', 'r') as f:
    lines = f.readlines()
for count, line in enumerate(lines):
    parts = line.split(' ')
    if line.startswith('8'):
        first = parts[0]
        second = parts[2]
        if first != second:
            print('Not equal on line ' + str(count + 1))
