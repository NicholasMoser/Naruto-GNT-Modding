# Projectile struct

Found at address `802773b8`
Size `0x204`
Mentioned offsets are all explicitly initiated, all offsets are originally initiated to 0

## 0x0 KF

## 0x4 K2F

## 0x8 Probably NF

## 0xc Probably N2F

## 0x10 Some flag

## 0x14 Some flag

## 0x18 Unknown
- Initiated to -1

## 0x20 POW

## 0x24 DMG

## 0x28 Unknown
- Initiated to -1

## 0x2c Unknown
- Initiated to *(int *)(DAT_802283f4 + 0x34) + 1
- Set to *(projectile+0x34)+1 in op_4718

## 0x34
- Incremented in op_4718

## 0x3C
- Set value = op1 in op_4719

## 0x40
- Set value = op1 in op_471a

## 0x48
- Set to 0 in op_471c

## 0x4c
- Set value = op1 in op_471b

## 0x50
- Set value = op1 in op_471c

## 0x54
- Set to 0 in op_471c

## 0x58 Unknown
- (*(int *)((&DAT_802435b4)[tp\_id] + pc1 * 4) + DAT_802773b4 * 4 + -4);

## 0x60 chr\_p
- Pointer to chr\_p belonging to player who spawned the projectile

## 0x64 Unknown
- Initiated to 0

## 0x6c Self reference
- Pointer to start of struct

## 0x70 Probably number of hits

## 0x74 Some combination of w1 and w2
- Equal to ((w1 * 0x60) >> 2) + (w3 * (w1-1))

## 0x7c w1

- First word projectile + 1

## 0x80 w2

- Second word projectile

## 0x84 w3

- Third word projectile

## 0x88 allocated memory

- size w1 * 0x60
- initiated to 0
- offset 0x34 contains pointer to this struct

## 0x8c something

- Value stored at given offset from 0x8024361c in memory + 4 or 0 if nothing found + (w1 * 0x60)

## 0x90 something else

- something + w2 * 4

## 0x94 OFF

- offset from the start of seq file where projectile data is located

## 0x98 SEQ

- pointer to start of seq file where the projectile is located

## 0x9c Depending on op4
- Either 1 or 0

## 0xa8 Self reference
- Pointer to start of this struct

## 0xa0
- Written to in op_4716
- \*(\*(seq\_p + 0x14) + 0x5c) + op1
- op_4717 sets value to 0

## 0xac Unknown
- &DAT_80243578 + p_id2 * 0xC

## 0xb0 Unknown
- *(&DAT_80243578 + p_id2 * 0xC) + 8

## 0xb4 op4
- Fourth operand following 47000026 op\_code

## 0xb8
- Written to in op_470d

## 0xc4 op1
- First operand following 47000026 op\_code

## 0xc8 chr\_p
- Pointer to chr\_p belonging to player who spawned the projectile

## 0xcc p\_id
- Player id of player who spawned the projectile

## 0xd0 DAT_802773bc
- Whatever was stored in memory address 802773bc when the projectile was created

## 0xd4 tp\_id
- Player ID of the target of the projectile

## 0xd8 Unknown
- Return value from zz_80107bd4_(*((&DAT_802435e8)[tpid] + op2 * 4),-1) & 0x10881 | 0x20000 & 0xfffffffe
- Used in op_470b
- Used in op_470c

## 0xdc Unknown
- Return value from zz_80107bd4_(*((&DAT_802435e8)[tpid] + op2 * 4),0)

## 0xe0 height
- signed short
- Set in op_470e

## 0xe2 height_companion
- signed short
- Set in op_470e
- Seems to be -1 from seq files

## 0xfc
- Used in op_470c

## 0xfc Velocity
- Written to in op_470a

## 0x130
- Used in op_4710
- Used in op_471e with operand 0 (randomized)

## 0x134
- Used in op_4710
- Used in op_471e with operand 1 (randomized)

## 0x138
- Used in op_4710
- Used in op_471e with operand 2 (randomized)

## 0x144 Probably number of hits

## 0x1b0
- Used in op_4715

## 0x1b4
- Used in op_4715

## 0x1b8
- Used in op_4715

## 0x1bc
- Used in op_4715

## 0x1cc
- Used in op_4715

## 0x1d0
- Used in op_4715

## 0x1d4
- Used in op_4715

## 0x1d8
- Used in op_4715

## 0x1fc Unknown
- Initiated to 0
- Written to in op_4701

## 0x200 Unknown
- Initiated to 0
