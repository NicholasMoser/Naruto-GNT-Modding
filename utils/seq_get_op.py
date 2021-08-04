# Attempts to print out the number of words read after a call to `seq_get_op`.
# This is a function called in SEQ opcodes to retrieve values from registers
# or memory. The number of words read is a variable number that depends on
# the bits set for the opcode.
#
# Usage:
# python seq_get_op.py {opcode in hex}
#
# Example:
# python seq_get_op.py 0206003f

import sys

opcode = int(sys.argv[1], 16)
words = 1
# The op is the last byte of the opcode
op = opcode & 0xFF
if op == 0x3f:
    words += 1
elif op == 0x3e:
    words += 2
if op & 0x40 != 0:
    words += 1
elif op & 0x80 != 0:
    words += 1
print(words)
