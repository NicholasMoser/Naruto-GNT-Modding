# Gecko Codetype Documentation

This page contains documentation for the different types of Gecko codes. Gecko codes are similar to [Action Replay](http://www.bsfree.org/hack/hacking_gcn.html#ar_code_types) codes and can be used for both Gamecube and Wii games. The information was taken from the now defunct [WiiRD Code Database](https://web.archive.org/web/20200807235652/https://geckocodes.org/index.php?arsenal=1), which lists the authors as kenobi, Nuke, Link, Brkirch, dcx2, Skiller, wiiztec, hetoan2, Romaap, mugwhump, and James0x57.

The PowerPC assembly to handle these codes can be found in [codehandler.bin](https://github.com/dolphin-emu/dolphin/blob/115ad825813d76e3ac8bd8aaab0d110c3fe378ad/Data/Sys/codehandler.bin)
which is loaded by Dolphin into the unused area [starting at 0x80001800](https://github.com/dolphin-emu/dolphin/blob/115ad825813d76e3ac8bd8aaab0d110c3fe378ad/Source/Core/Core/GeckoCode.h#L50).

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

## If Codes

### 32 bits (endif, then) If equal

```gecko
20______ XXXXXXXX
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If 32 bits at [ba+______]==XXXXXXXX,
then codes are executed (else code execution set to false)

To use po instead of ba, change the codetype from 20 to 30.
For values of ______ >= 0x01000000, add one to the codetype.

### 32 bits (endif, then) If not equal

```gecko
22______ XXXXXXXX
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If 32 bits at [ba+______]!=XXXXXXXX,
then codes are executed (else code execution set to false)

To use po instead of ba, change the codetype from 22 to 32.
For values of ______ >= 0x01000000, add one to the codetype.

### 32 bits (endif, then) If greater than (unsigned)

```gecko
24______ XXXXXXXX
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If 32 bits at [ba+______]>XXXXXXXX,
then codes are executed (else code execution set to false)

To use po instead of ba, change the codetype from 24 to 34.
For values of ______ >= 0x01000000, add one to the codetype.

### 32 bits (endif, then) If lower than (unsigned)

```gecko
26______ XXXXXXXX
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If 32 bits at [ba+______]<XXXXXXXX,
then codes are executed (else code execution set to false)

To use po instead of ba, change the codetype from 26 to 36.
For values of ______ >= 0x01000000, add one to the codetype.

### 16 bits (endif, then) If equal

```gecko
28______ MMMMXXXX
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If 16 bits at ([ba+______] & not(MMMM))==XXXX,
then codes are executed (else code execution set to false)

To use po instead of ba, change the codetype from 28 to 38.
For values of ______ >= 0x01000000, add one to the codetype.

### 16 bits (endif, then) If not equal

```gecko
2A______ MMMMXXXX
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If 16 bits at ([ba+______] & not(MMMM))!=XXXX,
then codes are executed (else code execution set to false)

To use po instead of ba, change the codetype from 2A to 3A.
For values of ______ >= 0x01000000, add one to the codetype.

### 16 bits (endif, then) If greater than

```gecko
2C______ MMMMXXXX
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If 16 bits at ([ba+______] & not(MMMM))>XXXX,
then codes are executed (else code execution set to false)

To use po instead of ba, change the codetype from 2C to 3C.
For values of ______ >= 0x01000000, add one to the codetype.

### 16 bits (endif, then) If lower than

```gecko
2E______ MMMMXXXX
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If 16 bits at ([ba+______] & not(MMMM))<XXXX,
then codes are executed (else code execution set to false)

To use po instead of ba, change the codetype from 2E to 3E.
For values of ______ >= 0x01000000, add one to the codetype.

## Base Address

### Load into Base Address

```gecko
40TYZ00N XXXXXXXX
```

40000 : ba = [XXXXXXXX]  
40001 : ba = [grN+XXXXXXXX]  
40010 : ba = [ba+XXXXXXXX]  
40011 : ba = [ba+grN+XXXXXXXX]

40100 : ba += [XXXXXXXX]  
40101 : ba += [grN+XXXXXXXX]  
40110 : ba += [ba+XXXXXXXX]  
40111 : ba += [ba+grN+XXXXXXXX]

50010 : ba = [po+XXXXXXXX]  
50011 : ba = [po+grN+XXXXXXXX]

50110 : ba += [po+XXXXXXXX]  
50111 : ba += [po+grN+XXXXXXXX]

### Set Base Address to

```gecko
42TYZ00N XXXXXXXX
```

42000 : ba= XXXXXXXX  
42001 : ba= grN+XXXXXXXX  
42010 : ba= ba+XXXXXXXX  
42011 : ba= ba+grN+XXXXXXXX

42100 : ba+= XXXXXXXX  
42101 : ba+= grN+XXXXXXXX  
42110 : ba+= ba+XXXXXXXX  
42111 : ba+= ba+grN+XXXXXXXX

52010 : ba= po+XXXXXXXX  
52011 : ba= po+grN+XXXXXXXX

52110 : ba+= po+XXXXXXXX  
52111 : ba+= po+grN+XXXXXXXX

### Store Base Address at

```gecko
440YZ00N XXXXXXXX
```

44000 : [XXXXXXXX] = ba  
44001 : [XXXXXXXX+grN] = ba  
44010 : [XXXXXXXX+ba] = ba  
44011 : [XXXXXXXX+ba+grN] = ba

54010 : [XXXXXXXX+po] = ba  
54011 : [XXXXXXXX+po+grN] = ba

### Put next code's location into the Base Address

```gecko
4600XXXX 00000000
```

XXXX is a signed 16bits value : 0xFFFF=-1  
ba will hold the address at which the next line of code is stored + XXXX

## Pointer Address

### Load into Pointer Address

```gecko
48TYZ00N XXXXXXXX
```

48000 : po = [XXXXXXXX]  
48001 : po = [grN+XXXXXXXX]  
48010 : po = [ba+XXXXXXXX]  
48011 : po = [ba+grN+XXXXXXXX]

48100 : po += [XXXXXXXX]  
48101 : po += [grN+XXXXXXXX]  
48110 : po += [ba+XXXXXXXX]  
48111 : po += [ba+grN+XXXXXXXX]

58010 : po = [po+XXXXXXXX]  
58011 : po = [po+grN+XXXXXXXX]

58110 : po += [po+XXXXXXXX]  
58111 : po += [po+grN+XXXXXXXX]

### Set Pointer Address to

```gecko
4ATYZ00N XXXXXXXX
```

4A000 : po = XXXXXXXX  
4A001 : po = grN+XXXXXXXX  
4A010 : po = ba+XXXXXXXX  
4A011 : po = ba+grN+XXXXXXXX

4A100 : po += XXXXXXXX  
4A101 : po += grN+XXXXXXXX  
4A110 : po += ba+XXXXXXXX  
4A111 : po += ba+grN+XXXXXXXX

5A010 : po = po+XXXXXXXX  
5A011 : po = po+grN+XXXXXXXX

5A110 : po += po+XXXXXXXX  
5A111 : po += po+grN+XXXXXXXX

### Store Pointer Address at

```gecko
4C0YZ00N XXXXXXXX
```

4C000 : [XXXXXXXX] = po  
4C001 : [XXXXXXXX+grN] = po  
4C010 : [XXXXXXXX+ba] = po  
4C011 : [XXXXXXXX+ba+grN] = po

5C010 : [XXXXXXXX+po] = po  
5C011 : [XXXXXXXX+po+grN] = po

### Put next code's location into the Pointer Address

```gecko
4E00XXXX 00000000
```

XXXX is a signed 16bits value : 0xFFFF=-1  
po will hold the address at which the next line of code is stored + XXXX

## Flow Control

### Set Repeat

```gecko
6000NNNN 0000000P
```

Store next code address and NNNN (number of times to repeat) in bP.

### Execute Repeat

```gecko
62000000 0000000P
```

If NNNN stored in bP is >0, it is decreased by 1 and the code handler jumps to the "next code address" stored in bP

### Return

```gecko
64000000 0000000P
```
If the code execution status is true, the code handler jumps to the "next code address" stored in bP (NNNN in bP is not touched).

```gecko
64100000 0000000P
```
If the code execution status is false, the code handler jumps to the "next code address" stored in bP (NNNN in bP is not touched).

```gecko
64200000 0000000P
```
No matter what the code execution status is, the code handler jumps to the "next code address" stored in bP (NNNN in bP is not touched).

### Goto

```gecko
6600XXXX 00000000
```
If the code execution status is true, the code handler jumps to (next line of code + XXXX lines). XXXX is signed.

```gecko
6610XXXX 00000000
```
If the code execution status is false, the code handler jumps to (next line of code + XXXX lines). XXXX is signed.

```gecko
6620XXXX 00000000
```
The code handler jumps to (next line of code + XXXX lines). XXXX is signed.

### Gosub

```gecko
6800XXXX 0000000P
```
If the code execution status is true, the code handler stores the next code address in bP, then it jumps to (next line of code + XXXX lines). XXXX is signed.

```gecko
6810XXXX 0000000P
```
If the code execution status is false, the code handler stores the next code address in bP, then it jumps to (next line of code + XXXX lines). XXXX is signed.

```gecko
6820XXXX 0000000P
```
No matter what the code execution status is, the code handler stores the next code address in bP, then it jumps to (next line of code + XXXX lines). XXXX is signed.

## Gecko Register

### Set Gecko Register to

```gecko
80SY000N XXXXXXXX
```

8000 : grN = XXXXXXXX  
8001 : grN = XXXXXXXX+ba

8010 : grN += XXXXXXXX  
8011 : grN += XXXXXXXX+ba

9001 : grN = XXXXXXXX+po  
9011 : grN += XXXXXXXX+po

### Load into Gecko Register

```gecko
82UY000N XXXXXXXX
```

8200 : grN = 8bits at [XXXXXXXX]  
8210 : grN = 16bits at [XXXXXXXX]  
8220 : grN = 32bits at [XXXXXXXX]

8201 : grN = 8bits at [XXXXXXXX+ba]  
8211 : grN = 16bits at [XXXXXXXX+ba]  
8221 : grN = 32bits at [XXXXXXXX+ba]

9201 : grN = 8bits at [XXXXXXXX+po]  
9211 : grN = 16bits at [XXXXXXXX+po]  
9221 : grN = 32bits at [XXXXXXXX+po]

### Store Gecko Register at

84T0YYYN XXXXXXXX : Starting Address is XXXXXXXX  
84T1YYYN XXXXXXXX : Starting Address is XXXXXXXX+ba  
94T1YYYN XXXXXXXX : Starting Address is XXXXXXXX+po

T = 0 : byte
T = 1 : halfword
T = 2 : word

Write grN's T to YYY+1 consecutive T-sized addresses.

### Gecko Register / Direct Value Operations

```gecko
86TY000N XXXXXXXX
```

86T0 : grN = (grN ? XXXXXXXX)  
86T1 : [ grN ] = ([ grN ] ? XXXXXXXX)  
86T2 : grN = (grN ? [XXXXXXXX])  
86T3 : [ grN ] = ([ grN ] ? [XXXXXXXX])

T : ?  
0 : add (+)  
1 : mul (*)  
2 : or (|)  
3 : and (&)  
4 : xor (^)  
5 : slw (<<)  
6 : srw (>>)  
7 : rol (rotate left)  
8 : asr (arithmetic shift right)  
9 : fadds (single float add)  
A : fmuls (single float mul)

### Gecko Register Operations

```gecko
88TY000N 0000000K
```

88T0 : grN = (grN ? grK)
88T1 : [ grN ] = ([ grN ] ? grK)
88T2 : grN = (grN ? [ grK ])
88T3 : [ grN ] = ([ grN ] ? [ grK ])

T : ?  
0 : add (+)  
1 : mul (*)  
2 : or (|)  
3 : and (&)  
4 : xor (^)  
5 : slw (<<)  
6 : srw (>>)  
7 : rol (rotate left)  
8 : asr (arithmetic shift right)  
9 : fadds (single float add)  
A : fmuls (single float mul)

### Memory Copy 1

```gecko
8AYYYYNK XXXXXXXX
```
copy YYYY bytes from [ grN ] to [ grK ]+XXXXXXXX, grK can't be F.

```gecko
8AYYYYNF XXXXXXXX
```
copy YYYY bytes from [ grN ] to ba+XXXXXXXX

```gecko
9AYYYYNF XXXXXXXX
```
copy YYYY bytes from [ grN ] to po+XXXXXXXX

### Memory Copy 2

```gecko
8CYYYYNK XXXXXXXX
```
copy YYYY bytes from [ grN ]+XXXXXXXX to [ grK ], grN
can't be F.

```gecko
8CYYYYFK XXXXXXXX
```
copy YYYY bytes from ba+XXXXXXXX to [ grK ]

```gecko
9CYYYYFK XXXXXXXX
```
copy YYYY bytes from po+XXXXXXXX to [ grK ]

## Gecko Register If Codes

### 16 bits (endif, then) If equal

```gecko
A0______ KN00MMMM
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If ([ grN ] and not(MMMM))==([ grK ] and not(MMMM)) then codes are executed (else code execution set to false).

If N or K is F, it will use ba+______ instead of grF!

To use po instead of ba (when grN or grK is F), change the codetype from A0 to B0.
For values of ______ >= 0x01000000, add one to the codetype.

### 16 bits (endif, then) If not equal

```gecko
A2______ KN00MMMM
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If ([ grN ] and not(MMMM))!=([ grK ] and not(MMMM)) then codes are executed (else code execution set to false).

If N or K is F, it will use ba+______ instead of grF!

To use po instead of ba (when grN or grK is F), change the codetype from A2 to B2.
For values of ______ >= 0x01000000, add one to the codetype.

### 16 bits (endif, then) If greater

```gecko
A4______ KN00MMMM
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If ([ grN ] and not(MMMM))>([ grK ] and not(MMMM)) then codes are executed (else code execution set to false).

If N or K is F, it will use ba+______ instead of grF!

To use po instead of ba (when grN or grK is F), change the codetype from A4 to B4.
For values of ______ >= 0x01000000, add one to the codetype.

### 16 bits (endif, then) If lower

```gecko
A6______ KN00MMMM
```

Adding 1 to ______ will make this code first apply an Endif.
(It will still use ______ for address calculation; without the added 1)

If ([ grN ] and not(MMMM))<([ grK ] and not(MMMM)) then codes are executed (else code execution set to false).

If N or K is F, it will use ba+______ instead of grF!

To use po instead of ba (when grN or grK is F), change the codetype from A6 to B6.
For values of ______ >= 0x01000000, add one to the codetype.

## Counter If Codes

### 16 bits (endif, then) If counter value equal

```gecko
A80ZZZZT MMMMXXXX
```

ZZZZ : The code's counter.  
Code's Operation : If current execution status is true, increase counter by 1. If it's false, reset counter to 0.  
Condition : If (XXXX and not(MMMM))==ZZZZ, codes following this are executed (else code execution set to false).

T = 0 : Do Code's Operation, then run Condition.  
T = 1 : Apply an Endif, then do Code's Operation, finally run Condition.  
T = 8 : Do Code's Operation, then run Condition (and if it is true, reset counter to 0).  
T = 9 : Apply an Endif, then do Code's Operation, finally run Condition (and if it is true, reset counter to 0).

### 16 bits (endif, then) If counter value not equal

```gecko
AA0ZZZZT MMMMXXXX
```

ZZZZ : The code's counter.  
Code's Operation : If current execution status is true, increase counter by 1. If it's false, reset counter to 0.  
Condition : If (XXXX and not(MMMM))!=ZZZZ, codes following this are executed (else code execution set to false).

T = 0 : Do Code's Operation, then run Condition.  
T = 1 : Apply an Endif, then do Code's Operation, finally run Condition.  
T = 8 : Do Code's Operation, then run Condition (and if it is true, reset counter to 0).  
T = 9 : Apply an Endif, then do Code's Operation, finally run Condition (and if it is true, reset counter to 0).

### 16 bits (endif, then) If counter value greater

```gecko
AC0ZZZZT MMMMXXXX
```

ZZZZ : The code's counter.  
Code's Operation : If current execution status is true, increase counter by 1. If it's false, reset counter to 0.  
Condition : If (XXXX and not(MMMM))>ZZZZ, codes following this are executed (else code execution set to false).

T = 0 : Do Code's Operation, then run Condition.  
T = 1 : Apply an Endif, then do Code's Operation, finally run Condition.  
T = 8 : Do Code's Operation, then run Condition (and if it is true, reset counter to 0).  
T = 9 : Apply an Endif, then do Code's Operation, finally run Condition (and if it is true, reset counter to 0).

### 16 bits (endif, then) If counter value lower

```gecko
AE0ZZZZT MMMMXXXX
```

ZZZZ : The code's counter.  
Code's Operation : If current execution status is true, increase counter by 1. If it's false, reset counter to 0.  
Condition : If (XXXX and not(MMMM))<ZZZZ, codes following this are executed (else code execution set to false).

T = 0 : Do Code's Operation, then run Condition.  
T = 1 : Apply an Endif, then do Code's Operation, finally run Condition.  
T = 8 : Do Code's Operation, then run Condition (and if it is true, reset counter to 0).  
T = 9 : Apply an Endif, then do Code's Operation, finally run Condition (and if it is true, reset counter to 0).

## ASM Codes

### Execute ASM

```gecko
C0000000 NNNNNNNN
ZZZZZZZZ ZZZZZZZZ
ZZZZZZZZ ZZZZZZZZ
4E800020 00000000
```

Executes the NNNNNNNN lines of instruction placed under the code.
The instructions MUST end with a blr (0x4E800020).

### Insert ASM

```gecko
C2______ NNNNNNNN
ZZZZZZZZ ZZZZZZZZ
ZZZZZZZZ ZZZZZZZZ
ZZZZZZZZ 00000000
```

This code will replace the instruction at `ba+______` with a branch that will point to ZZZZZZZZ.
The replaced is not saved, the code creator must then put it in their code manually (if needed).
The instruction MUST end with ONE 00000000, because the code handler will add a `b (ba+______)` instruction there.  
If your asm code fills all the line, add a `60000000 00000000` under it (and count this line in NNNNNNNN).

To use po instead of ba, change the codetype from C2 to D2.
For values of `______ >= 0x01000000`, add one to the codetype.

### Create a branch

```gecko
C6______ YYYYYYYY
```

Writes, at ______+ba, a single `b YYYYYYYY` instruction.

To use po instead of ba, change the codetype from C6 to D6.
For values of ______ >= 0x01000000, add one to the codetype.

## Other

### On/Off Switch

```gecko
CC000000 00000000
```

This code will only work correctly if an If... code is placed before it.
Each time the code execution status goes from true to false to true, and the switch code is reached, the "switch" is moved. The switch moves from on<->off, and set the code execution accordingly to its state. The value of the switch is stored inside the code.
It is NOT an If... code. It only changes the current code executions status.

### Address Range Check

```gecko
CE00000T XXXXYYYY
```

T = 0, Don't apply Endif.  
T = 1, Apply Endif.  
Then check if `ba >= 0xXXXX0000` and `ba < 0xYYYY0000`.
If `XXXX>=YYYY`, then the code will always set the code execution to false.

To use po instead of ba, change the codetype from CE to DE.

### Full Terminator

```gecko
E0000000 XXXXYYYY
```

Clears the code execution status.  
If `XXXX<>0`, ba = 0xXXXX0000  
If `YYYY<>0`, po = 0xYYYY0000

### Endif (+else)

```gecko
E2T000VV XXXXYYYY
```

T = 0, Applies VV Endifs.  
T = 1, Applies VV Endifs and inverse the code execution status (="else").

If `XXXX<>0`, ba = 0xXXXX0000
If `YYYY<>0`, po = 0xYYYY0000

### End of Codes

```gecko
F0000000 00000000
```

Tells the code handler that there are no more codes in the code list. The code handler exits.

## Gecko 1.8+ Only

### Insert ASM With 16 bit XOR Checksum

```gecko
F2______ YYZZZZNN
ZZZZZZZZ ZZZZZZZZ
ZZZZZZZZ ZZZZZZZZ
ZZZZZZZZ 00000000
```

YY (signed) 16-bit values after (if positive) or before (if negative) `[ba + ______]` will be XOR'ed together. If the result is equal to ZZZZ, the code will be executed.
The rest of the code functions the exact same way as the C2 codetype (Insert ASM), with NN as the number of lines.

To use po instead of ba, change the codetype from F2 to F4.
For values of `______ >= 0x01000000`, add one to the codetype.

### (If) Search, Set Pointer

```gecko
F60000NN XXXXYYYY
ZZZZZZZZ ZZZZZZZZ
ZZZZZZZZ ZZZZZZZZ
```

Creates an if (so this code requires an endif), then searches for the NN lines of Z values between XXXX0000 and YYYY0000 (or, if XXXX is 8000, between 80003000 and YYYY0000).
To prevent this code from causing game lag, it will only search the first time it is read by the code handler (the result is saved to the code and reused).
If the Z values are found, set po to the starting address of the values (SSSSSSSS) and replace the F6 line with F60003NN SSSSSSSS.
If the Z values are not found, then set code execution status to false and replace the F6 line with F60001NN XXXXYYYY.

## Appendix

### Codetypes in depth

A hex digit actually represents 4 bits, and you need to look at the underlying bits to understand why the code types are defined the way they are. Normally, we refer to a 32-bit RAM write as an "04 code type", but this is actually a misnomer. It misleadingly implies that the 8 bits belonging to the two hex digits "04" are the code type, when the actual code type only has 7 bits! The 8th bit belongs to the address, which creates the "05" code type. People also think that the address is only comprised of 24 bits (the other 6 hex digits), when the address is actually 25 bits (the other 6 hex digits + the last bit of the second digit).

A picture may help; Here's the binary breakdown of the first word of a code.

![Gecko Code Bits](/general/images/gecko_code_bits.PNG?raw=true "Gecko Code Bits")
