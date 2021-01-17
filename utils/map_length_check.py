# Checks the length of each function in the symbol map and prints which ones may be incorrect.
# The reason that some lengths are incorrect is because they may contain a branch that shouldn't
# count for the function length, but did count when Dolphin automatically generated the symbol
# map. It accomplished this by counting the difference in bytes between the start and end
# of the function.

with open('../general/symbol_maps/RNEEDA.map', 'r') as f:
    lines = f.readlines()
previous = None
for count, line in enumerate(lines):
    parts = line.split(' ')
    if line.startswith('8'):
        name = parts[4]
        addr = int(parts[0], 16)
        if (previous):
            previousLength = int(previous[1], 16)
            previousAddr = int(previous[0], 16)
            diff = addr - previousAddr
            if (diff < previousLength):
                print('Function: {}'.format(previous[4]))
                print('  Expected: {:02X} Actual: {:02X}'.format(previousLength, diff))
        previous = parts
