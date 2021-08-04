# Attempts to print out the number of words read after a call to `seq_get_ops`.
# This is a function called in SEQ opcodes to retrieve values from registers
# or memory. The number of words read is a variable number that depends on
# the bits set for the opcode.
#
# Usage:
# python seq_get_ops.py {opcode in hex}
#
# Example:
# python seq_get_ops.py 0616157b

import sys

opcode = int(sys.argv[1], 16)
words = 1
second_op_set = False
# First op is the third byte of the opcode
first_op = (opcode >> 0x8) & 0xFF
if first_op == 0x3f:
    words += 1
elif first_op == 0x3e:
    words += 2
if first_op & 0x40 != 0:
    words += 1
elif first_op & 0x80 != 0:
    words += 1
elif first_op < 0x30:
    print('Second op is the fourth byte of the opcode')
    second_op = opcode & 0xff
    second_op_set = True

if not second_op_set:
    print('Second op is the first byte of the next word')
    print('Enter the next word after this many 4-byte words: ' + str(words))
    second_op = (int(input(), 16) >> 0x18) & 0xff
    words += 1

if second_op == 0x3f:
    words += 1
elif second_op == 0x3e:
    words += 2
if second_op & 0x40 != 0:
    words += 1
elif second_op & 0x80 != 0:
    words += 1

print('Opcode full length number of 4-byte words: ' + str(words))
