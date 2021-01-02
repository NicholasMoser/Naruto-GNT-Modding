'''
This script will read the GNT4 symbol map and fill out function names in the GNT4 decomp
project. It takes two arguments, the first line of the symbol map to fill out and the
last line of the symbol map to fill out (both inclusive).
The GNT4 decomp project can be found at: https://github.com/doldecomp/gnt4
'''
import os
import sys

if len(sys.argv) != 3:
    print('Please include exactly two arguments, the start line and end line of the symbol map (both inclusive).')
    sys.exit(1)
start = int(sys.argv[1]) - 1
end = int(sys.argv[2]) - 1
asm_dir = 'D:/Code/gnt4/asm'

with open('../general/symbol_maps/G4NJDA.map', 'r') as f:
    lines = f.readlines()
dupe_check = []
for count, line in enumerate(lines):
    if (count >= start and count <= end):
        parts = line.split(' ')
        addr = parts[0].upper()
        name = parts[4].strip()
        old_name = 'func_' + addr
        found = False
        for root, dirs, files in os.walk(asm_dir):
            for _file in files:
                full_path = os.path.join(root, _file)
                with open(full_path, 'r') as f:
                    text = f.read()
                if old_name in text:
                    if not found:
                        found = True
                        # All function names are global right now, therefore we must avoid
                        # duplicates. This is accomplished by appending '_'.
                        if name in dupe_check:
                            name = name + '_'
                        dupe_check.append(name)
                    text = text.replace(old_name, name)
                    with open(full_path, 'w', newline='\r\n') as w:
                        w.write(text)
        if not found:
            print('Did not find {} ({}). Maybe try lbl_{}'.format(old_name, name, addr))
                
