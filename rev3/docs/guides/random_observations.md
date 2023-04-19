# Random Observations

## Obstacles and Stage Transitions

- 0x80395b64 - Stage Transitions Off
- 0x80395b68 - Obstacles Off

## Find Attack Damage

You can find it for just about any move by setting a code breakpoint at 0x8006b2a0 in Dolphin, and calculate the offset of r4 + 0x24.
Then copy that address and set a write memory breakpoint on it. Then do the attack and it will be written in an opcode.
Step out of that opcode and progress to the next opcode. Get the memory address of r5 which is the program counter.
Look at the bytes of that address and compare them in the SEQ file.
