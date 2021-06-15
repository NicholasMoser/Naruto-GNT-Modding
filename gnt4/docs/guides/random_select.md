# Random Select

An idea was proposed to replace Akamaru with a random select option. When Akamaru is selected, make a call to the internal RNG function
and return a value between 1 and 28 (the valid character ids).

You can see an example of this code in action here: https://imgur.com/a/kGYeQTG

## Code

```gecko
C215B9E8 00000003
2C000011 40820008
38006DAD 7C04412E
60000000 00000000
C2092154 0000000A
7CA6282E 2C056DAD
40820044 9421FFF0
90610004 90010008
9081000C 38600029
3CA0801C 60A5CE50
7CA903A6 4E800421
2C030000 4182FFE8
7C651B78 8081000C
80010008 80610004
38210010 00000000
04213fb4 00000026
04214014 00000011
```

## Implementation

There are many structs in game relating to the character order in the CSS. Ideally, we want to modify the earliest referenced ones
such that the changes are propogated to other necessary structs. I have found that an early point we could hijack the selected
character id is at the instruction 0x80092158. The instruction at 0x80092158 is located in the function for SEQ opcode 3C16.
The problem with this instruction is that it is called for much more than the CSS menu, it is called for what appears to be
all menus. This makes modifying it to only affect Akamaru difficult. Akamaru's character id is 11, so if we check for 11 we
may have Akamaru but it also may be a value for a different menu. I could not find an easy way to determine the current menu
at this instruction.

The idea then becomes, what if we replace 11 at this point with a large magic number that likely would not be encountered in
the menus? The 11 is loaded from a struct in the heap that is set in the function at 0x8015b7c8. I call this function
`css_update_values(...)`. Instead of setting 11, set the magic number 0x6DAD. Then, in the code for SEQ opcode 3C16, check
for the value 0x6DAD. If this value is found, replace it with a random number between 1 and 28 (the valid character ids).

Furthermore, we should consider replacing the location in the CSS for Akamaru so that it is closer to the starting point.
A good replacement would be swapping Awakening Hinata and Akamaru, so that random select is 1 slot above the starting point.

## Proof of Concept

First I wrote a proof of concept that simply replaces Akamaru with a different character.

### Code Part 1

This code is injected in `css_update_values(...)` to check for Akamaru's character id, 11. If it sees 11, it will replace it
with 0x6DAD.

```asm
cmpwi   r10, 0x11
bne     0x8
li      r10, 0x6DAD
stwx    r10, r9, r8
```

```gecko
C215B9A4 00000003
2C0A0011 40820008
39406DAD 7D49412E
60000000 00000000
```

### Code Part 2

This code is injected in the function for SEQ opcode 3C16. It will load the currently selected character id. If it sees 0x6DAD,
it will replace it with the character id for Sasuke, 1.

```asm
lwzx    r5, r6, r5
cmpwi   r5, 0x6DAD
bne     0x8
li      r5, 0x1
```

```gecko
C2092154 00000003
7CA6282E 2C056DAD
40820008 38A00011
60000000 00000000
```

### Code Part 2 with Random

Now that we can replace Akamaru with Sasuke, let's replace Akamaru with a random character.

```asm
loc_0x0:
  # Load the current character id and check if it is the magic number 0x6DAD
  lwzx  r5, r6, r5
  cmpwi r5, 0x6DAD
  # If it is the magic number, run the following code
  bne-  loc_0x3C
  # Store current values of r0, r3, and r4 on the stack.
  # This is because HSD_Randi will modify all three of these registers.
  stwu  r1, -16(r1)
  stw   r3, 0x4(r1)
  stw   r0, 0x8(r1)
  stw   r4, 0xC(r1)
  # Use 0x29 as the max number (exclusive) to return from HSD_Randi
  li    r3, 0x29
  # Load the address of HSD_Randi and call it
  lis   r5, 0x801C
  ori   r5, r5, 0xCE50
  mtctr r5
  bctrl
  # If the return value is 0 call HSD_Randi again
  cmpwi r3, 0
  beq   -0x18
  mr    r5, r3
  # Restore the values of r0, r3, and r4.
  lwz   r4, 0xC(r1)
  lwz   r0, 0x8(r1)
  lwz   r3, 0x4(r1)
  addi  r1, r1, 0x10

loc_0x3C:
```

```gecko
C2092154 0000000A
7CA6282E 2C056DAD
40820044 9421FFF0
90610004 90010008
9081000C 38600029
3CA0801C 60A5CE50
7CA903A6 4E800421
2C030000 4182FFE8
7C651B78 8081000C
80010008 80610004
38210010 00000000
```

### Swap Awakened Hinata and Akamaru

Now we need to swap the order in the CSS of Awakened Hinata and Akamaru. The CSS_CHR_ID_ORDER
struct is stored at 0x80213f7c. We simply swap the offsets for Awakened Hinata and Akamaru.

```gecko
04213fb4 00000026
04214014 00000011
```

### Code Part 1 with CSS Order Swap

Now that we've swapped the order in the CSS of Awakened Hinata and Akamaru, Code Part 1 will
no longer be hit. Akamaru will now be set to the heap in a different part of `css_update_values(...)`.
To fix this, we simply replace the other set instruction with the same logic as Code Part 1.

```asm
cmpwi   r0, 0x11
bne     0x8
li      r0, 0x6DAD
stwx    r0, r4, r8
```

```gecko
C215B9E8 00000003
2C000011 40820008
38006DAD 7C04412E
60000000 00000000
```

### The Final Code

Combining everything together, we can now merge these into a single code for the full functionality.

```gecko
C215B9E8 00000003
2C000011 40820008
38006DAD 7C04412E
60000000 00000000
C2092154 0000000A
7CA6282E 2C056DAD
40820044 9421FFF0
90610004 90010008
9081000C 38600029
3CA0801C 60A5CE50
7CA903A6 4E800421
2C030000 4182FFE8
7C651B78 8081000C
80010008 80610004
38210010 00000000
04213fb4 00000026
04214014 00000011
```
