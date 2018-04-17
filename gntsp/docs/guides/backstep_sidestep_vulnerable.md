# Naruto GNT Special Vulnerable Backstep/Sidestep

In Naruto GNT Special, there are ~7 frames of invincibility frames when you sidestep (L or R) or backstep (double back). This page talks about the code to disable these invincibility frames.

![Backstep Fix](/gntsp/images/gameplay/backstep_fix.gif?raw=true "Backstep Fix")

![Sidestep Fix](/gntsp/images/gameplay/sidestep_fix.gif?raw=true "Backstep Fix")

## Code

### Gecko Code

```
C2135B18 00000006
3C604200 60630008
7C001800 40820008
74004200 3C600200
60630008 7C001800
40820008 74000200
90050000 00000000
```

### Assembly

```
@80135b18
lis r3,0x4200
ori r3,r3,0x0008
cmpw r0,r3
bne- 0x8
andis. r0,r0,0x4200
lis r3,0x0200
ori r3,r3,0x0008
cmpw r0,r3
bne- 0x8
andis. r0,r0,0x0200
stw r0, 0 (r5)
```

## Explanation

This page will reference addresses and functions from [Useful Addresses and Functions](/gntsp/docs/guides/addresses_and_functions.md)

There is a flag located in the player block at [character_block_pointer] + 60.
When it ends in an 8, you are invincible. Backsteps are set to 0x4200_0008 and sidesteps are set to 0x0200_0008. Essentially we want to remove the invincibility (the 8 from the end) of these states. For more information on the states this address can be set to, see [Character State Flags](/gntsp/docs/guides/addresses_and_functions.md#character-state-flags) I looked into removing the addition of 8 to add invincibility, but I'm too afraid of side effects where things that should have invincibility lose it. Therefore I decided to program it as a literal edge case and say:

if 42000008 set to 42000000  
if 02000008 set to 02000000

The actual line we care about is at 80135B18. Every frame of the battle it will store the state of the character in the character block.

First let's check if it's a backstep by seeing if the character state is set to 0x4200_0008. Since this value is larger than 2 bytes, we will need to use two separate assembly commands to store the whole value in a register.

```
lis r3,0x4200
ori r3,r3,0x0008
```

Now that we've stored this value in register 3, let's compare it to the character state and see if it matches:

```
cmpw r0,r3
bne- 0x8
```

If they do not match, branch ahead to the next check. If they do match, do the following:

```
andis. r0,r0,0x4200
```

By doing an AND immediate shifted, we can AND 0x4200_0008 with 0x4200_0000. This will result in storing 0x4200_0000 in r0, removing invincibility. Now do the same for sidestep:

```
lis r3,0x0200
ori r3,r3,0x0008
cmpw r0,r3
bne- 0x8
andis. r0,r0,0x0200
```

And last we need to add back the original line we are replacing:

```
stw r0, 0 (r5)
```

