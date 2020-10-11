# SEQ

SEQ is a scriping language created by Eighting.
The files contain code about how an object in the game operates.

GNT4 has 101 possible OP codes, but only 76 are used.

## GameObject

Size 0x60?

Offset | Type | Description
--- | --- | ---
`0x00`|??|??
`0x04`|??|??
`0x08`|??|??
`0x0C`|??|??
`0x10`|??|??
`0x14`|??|??
`0x18`|??|??
`0x1C`|??|??
`0x20`|??|??
`0x24`|??|??
`0x28`|??|??
`0x2C`|??|??
`0x30`|??|??
`0x34`|??|??
`0x38`|??|??
`0x3C`|??|??
`0x40`|??|??
`0x44`|??|??
`0x48`|??|??
`0x4C`|??|??
`0x50`|??|??
`0x54`|int|??
`0x58`|int pointer|SEQ Position 
`0x5C`|int|SEQ Position

## Header

Offset | Type | Description
--- | --- | ---
`0x00`|int|Unknown
`0x04`|int|Unknown
`0x08`|int|Unknown
`0x0C`|int|Unknown

## Op-Codes

### Code 0x00 - 800A6068

### Code 0x01 - SEQ GOTO - 800A5698

Flags:
**0x00**
Sets seq position to 0 (exits seq file for frame)
**0x01**
**0x02**
**0x03**
**0x04**
**0x05**
**0x06**
**0x07**
**0x08**
**0x32**
01320000 XXXXXXXX
XXXXXXXX - goto position in seq file
**0x33**
**0x34**
**0x35**
**0x36**
**0x37**
**0x38**
**0x39**
**0x3A**
**0x3B**
**0x3C**
01320000 XXXXXXXX
XXXXXXXX - goto position in seq file
Continue executing at seq position + 8
0x3D
0x3E
0x3F
0x40
0x41
0x42
0x43
0x44
0x45
0x46
0x47
0x48
0x49
0x4A
0x4B
0x4C
0x4D
0x4E
0x4F
0x50
0x51
0x52
0x53
0x54
0x55
0x56
0x57
0x58
0x59
0x5A
0x5B
0x5C
0x5D
0x5E
0x5F

### Code 0x02 - 800A52F8

### Code 0x03 - Sets Value at 0x4C/0x54/0x58 - 800A51B0

### Code 0x04 - Stores Value at 0x54 - 800A4B40

Flags
**0x01**
**0x02**
**0x03**
**0x04**
**0x05**
**0x06**
**0x07**
0407XXXX
XXXX - Read FlagCode
Adds values together and stores at 0x54 of GOBJ
**0x08**
**0x09**
**0x0A**
**0x0B**
**0x0C**
**0x0D**
**0x0E**
**0x0F**
**0x10**
**0x11**
**0x12**
**0x13**
**0x14**
**0x15**
**0x16**
**0x17**
**0x18**

### Code 0x05 - 800A44C4
### Code 0x06 - 800A3ED4
### Code 0x07 - 800A3888
### Code 0x08 - 800A32C0
### Code 0x09 - 800A2A8C
### Code 0x0A - 800A274C
### Code 0x0B - 800A1C5C
### Code 0x0C - 800A1894
### Code 0x0D - 800A188C
Nothing
### Code 0x0E - 800AA9B8
### Code 0x0F - 800AA430
### Code 0x10 - 800A9C1C
### Code 0x11 - 800A99F0
### Code 0x12 - 800A8E68
### Code 0x13 - 800A8594
### Code 0x14 - 800A76EC
### Code 0x15 - 800A75C0
### Code 0x16 - 800A7204
### Code 0x17 - 800A713C
### Code 0x18 - 800A7054
### Code 0x19 - 800A6B1C
### Code 0x1A - 800A6458
### Code 0x1B - 800A6324
### Code 0x1C - 800A6228
### Code 0x1D - 800BB7A0
### Code 0x1E - 800BB5F8
### Code 0x1F - 800BB338
### Code 0x20 - 800BA19C
### Code 0x21 - 800B9458
### Code 0x22 - 800B832C
### Code 0x23 - 800B7D98
### Code 0x24 - 800B3EC4
### Code 0x25 - 800B3CE4
### Code 0x26 - 800C0288
### Code 0x27 - 800B097C
### Code 0x28 - 800B0320
### Code 0x29 - 800B214C
### Code 0x2A - 800B1750
### Code 0x2B - 800B1590
### Code 0x2C - 800B24B8
Nothing
### Code 0x2D - 800B24B0
Nothing
### Code 0x2E - 800B24A8
Nothing
### Code 0x2F - 800B24A0
Nothing
### Code 0x30 - 800B2498
Nothing
### Code 0x31 - 800B3580
### Code 0x32 - 800B3020
### Code 0x33 - 800B25D0
### Code 0x34 - 800B24C0
### Code 0x35 - 00000000
### Code 0x36 - 800960B4
### Code 0x37 - 800952F4
### Code 0x38 - 80094324
### Code 0x39 - 800924F0
### Code 0x3A - 80091248
### Code 0x3B - 8009228C
### Code 0x3C - 80091B8C
### Code 0x3D - 800C6228
### Code 0x3E - 80090EF8
### Code 0x3F - 800C5EDC
### Code 0x40 - 800C57BC
### Code 0x41 - 800C531C
### Code 0x42 - 800C5124
### Code 0x43 - 800C4FCC
### Code 0x44 - 800C4688
### Code 0x45 - 00000000
Unused
### Code 0x46 - 800C88A8
### Code 0x47 - 800C8404
### Code 0x48 - 800C8108
### Code 0x49 - 800C7D20
### Code 0x4A - 800C7C5C
### Code 0x4B - 800C7424
### Code 0x4C - 800C6900
### Code 0x4D - 800C676C
### Code 0x4E - 00000000
Unused
### Code 0x4F - 00000000
Unused
### Code 0x50 - 800C6534
### Code 0x51 - 00000000
Unused
### Code 0x52 - 00000000
Unused
### Code 0x53 - 00000000
Unused
### Code 0x54 - 00000000
Unused
### Code 0x55 - 800AAD24
### Code 0x56 - 800AAC68
### Code 0x57 - 00000000
Unused
### Code 0x58 - 00000000
Unused
### Code 0x59 - 00000000
Unused
### Code 0x5A - 00000000
Unused
### Code 0x5B - 800BFBB0
### Code 0x5C - 800BE9EC
### Code 0x5D - 00000000
Unused
### Code 0x5E - 00000000
Unused
### Code 0x5F - 00000000
Unused
### Code 0x60 - 00000000
Unused
### Code 0x61 - 800AB754
### Code 0x62 - 00000000
Unused
### Code 0x63 - 00000000
Unused
### Code 0x64 - 00000000
Unused