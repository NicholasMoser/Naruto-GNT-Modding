# Find duplicate function names in the GNT4 map file.
# We need to avoid duplicates so that decomp can work.

with open('../general/symbol_maps/G4NJDA.map', 'r') as f:
    lines = f.readlines()
print(len(lines))
a = []
for count, line in enumerate(lines):
    if count >= 3520: # Just check musyx.a for now
        parts = line.split(' ')
        if len(parts) > 4:
            name = parts[4]
            if name in a:
                print('found: ' + name)
            if name:
                a.append(name)
