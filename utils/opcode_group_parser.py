# Parses an opcode table and prints a csv

print('Opcode,Offset,Code Pointer,Purpose')
# 0x00   | 0x0    | 800A6068
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