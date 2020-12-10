'''
Parses an opcode table and prints a csv. Useful when working with any Eighting game
that references an opcode table. Copy the opcode table to a file named opcode_table
and run this script.
'''

print('Opcode,Offset,Code Pointer,Purpose')
opcode = 0
offset = 0
code_ptr = ''
with open('opcode_table', 'r') as f:
    text = f.read()
for index, char  in enumerate(text):
    code_ptr += char
    if (index % 8 == 7):
        print('{},{},{},'.format(hex(opcode), hex(offset), code_ptr))
        code_ptr = ''
        opcode += 1
        offset += 4
