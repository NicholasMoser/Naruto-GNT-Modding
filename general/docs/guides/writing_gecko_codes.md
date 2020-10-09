# Writing Gecko Codes

## Direct Ram Writes

### 8 bits Write & Fill

```gecko
00______ YYYY00XX
```

Writes the value XX to YYYY+1 consecutive byte-sized addresses, starting with the address ba+______

To use po instead of ba, change the codetype from 00 to 10. For values of ______ >= 0x01000000, add one to the codetype.

### 16 bits Write & Fill

```gecko
02______ YYYYXXXX
```

Writes the value XXXX to YYYY+1 consecutive halfword-sized addresses, starting with the address ba+______

To use po instead of ba, change the codetype from 02 to 12. For values of ______ >= 0x01000000, add one to the codetype.

### 32 bits Write

```gecko
04______ XXXXXXXX
```

Writes the value XXXXXXXX to ba+______

To use po instead of ba, change the codetype from 04 to 14. For values of ______ >= 0x01000000, add one to the codetype.

### String Write (Patch Code)

```gecko
06______ YYYYYYYY
d1d2d3d4 d5d6....
```

Writes each byte (d1, d2, d3, ...) consecutively, starting at address ba+______
YYYYYYYY is the number of bytes to write

To use po instead of ba, change the codetype from 06 to 16.
For values of ______ >= 0x01000000, add one to the codetype.

### Slider/Multi Skip (Serial)

```gecko
08______ XXXXXXXX
TNNNZZZZ VVVVVVVV
```

______ + ba = Initial Address  
X = Initial value for the RAM write  
T = Value Size (0 = byte, 1 = halfword, 2 = word)  
N = Amount of additional addresses to write to (the first is assumed)  
Z = Address Increment; in bytes (How many To skip By)  
V = Value Increment (How much to add to the value after each additional RAM write)  

To use po instead of ba, change the codetype from 08 to 18.
For values of ______ >= 0x01000000, add one to the codetype.
