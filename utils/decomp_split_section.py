# For the gnt4 decomp, split certain sections like bss.s and put each entry in the respective asm file that uses it

import sys
import os
from collections import defaultdict

# Put text of all asm files into memory
asms = {}
output = defaultdict(list)
for root, dirs, files in os.walk('asm'):
    for file in files:
        if file not in ['bss.s', 'data.s', 'rodata.s', 'sbss.s', 'sdata.s', 'sdata2.s']:
            full_path = os.path.join(root, file)
            with open(full_path, 'r', newline='\n') as asm:
                asms[full_path] = asm.read()

# Find what files have what labels
target_file = 'asm/bss.s'
with open(target_file, 'r', newline='\n') as input_file:
    input_file.readline()
    input_file.readline()
    input_file.readline()
    input_file.readline()
    while True:
        first = input_file.readline()
        if (first == ''):
            break
        second = input_file.readline()
        third = input_file.readline()
        name = second.strip()[:-1]
        full = first + second + third
        found = False
        for asm_full_path, asm_text in asms.items():
            if name in asm_text:
                found = True
                output[asm_full_path].append(full)
                break
        if not found:
            print('Could not find ' + name)
            sys.exit(1)

# Add the labels to their respective files
for asm_file, labels in output.items():
    with open(asm_file, 'a', newline='\n') as output_file:
        output_file.write('\n.section .bss, "wa"\n\t.balign 8\n')
        output_file.writelines(labels)
    