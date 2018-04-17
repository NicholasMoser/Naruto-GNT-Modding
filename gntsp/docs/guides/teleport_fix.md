# Naruto GNT Special Teleport Fix

The Naruto GNT SP teleport fix is a change to the game to use Chakra for teleports instead of KnJ. Both the L and R teleports will use 75% of your chakra. You will not gain or use any meter from the KnJ meter. There will be no additional gain to chakra during gameplay to make up for this additional use for it.

![Teleport Uses Chakra](/gntsp/images/gameplay/teleport_chakra.gif?raw=true "Teleport Uses Chakra")

## Code

### Gecko Code
```
C2064E04 00000001
80030044 00000000
C2064E24 00000001
38001D4C 00000000
C2064B9C 00000001
38001D4C 00000000
C2064B3C 00000001
80630044 00000000
C2064B44 00000001
80DF0040 00000000
C2064B4C 00000001
907F0044 00000000
C2064B00 00000002
38800000 C8228848
60000000 00000000
```

### Assembly
```
@80064e04
lwz r0, 0x0044 (r3)

@80064e24
li r0, 7500

@80064b9c
li r0, 7500

@80064b3c
lwz r3, 0x0044 (r3)

@80064b44
lwz r6, 0x0040 (r31)

@80064b4c
stw r3, 0x0044 (r31)

@80064b00
li r4,0
lfd f1, -0x77B8 (rtoc)
```

## Explanation

This page will reference addresses and functions from [Useful Addresses and Functions](/gntsp/docs/guides/addresses_and_functions.md)

The [Teleport Checker](/gntsp/docs/guides/addresses_and_functions.md#teleport-checker) function will need to check Chakra instead of KnJ meter. It normally checks against max KnJ (since a teleport will require your entire bar). Therefore it must instead check against 75%. The current plan is to use the immediate value 0x00001D4C (7500) which is 75% of 0x00002710 (10000). So in the Teleport Checker function, change:

```
80064e04 lwz r0, 0x004C (r3)
```

to the following

```
80064e04 lwz r0, 0x0044 (r3)
```

This means it will use your current chakra value instead of your current KnJ value.
Now we will want to use 75% of our max chakra instead of our max KnJ value as the comparison. To do this, change:

```
80064e24 lwz r0, 0x0048 (r3)
```

to the following

```
80064e24 li r0, 7500
```

This will load the immediate value 7500 into register 0, serving as our basis for whether a teleport succeeds or not. Now we know whether or not a teleport suceeds when L or R is pressed, but we need to change the logic for KnJ adding and subtracting.

We want no KnJ added on hit (or it can be ignored anyways), and we do not want any additional chakra added for the hit. We also need to subtract from chakra instead of KnJ for a teleport. The amount to subtract will need to be 7500 instead of the max (10000). First let's change the [Teleport Handler](/gntsp/docs/guides/addresses_and_functions.md#teleport-handler) to subtract 7500 instead of 10000.

We will want to change the line:

```
80064b9c lwz r0, 0x0040 (r3)
```

to the following

```
80064b9c li r0, 7500
```

So that instead of using 10000 as the amount of KnJ to subtract we are using 7500. Interestingly here, it uses +0x40 (Max chakra) instead of +0x48 (Max KnJ), however it works since they are the same value (10000).

Now we need to make sure this subtraction occurs on the KnJ value and not the chakra value. In the [KnJ Adjuster](/gntsp/docs/guides/addresses_and_functions.md#knj-adjuster), we will need to change the references of Current KnJ and Max KnJ to Current Chakra and Max Chakra respectively. This can be done by changing line:

```
80064b3c lwz r3, 0x004C (r3)
```

to the following

```
80064b3c lwz r3, 0x0044 (r3)
```

and by changing line:

```
80064b44 lwz r6, 0x0048 (r31)
```

to the following

```
80064b44 lwz r6, 0x0040 (r31)
```

Now we are referencing chakra values when we usually would be referencing KnJ values. But now we need to make sure that we are storing the new value to the current chakra value. So you will also change line:

```
80064b4c stw r3, 0x004C (r31)
```

to the following

```
80064b4c stw r3, 0x0044 (r31)
```

The last change we need to make is to prevent any gain from occuring on hit. With the changes as they are now the amount of KnJ added on hit will be added to chakra on hit instead, IN ADDITION to the normal amount added to chakra on hit. I've solved this by setting the amount of chakra to be added to 0. Therefore we will change:

```
80064b00 lfd f1, -0x77B8 (rtoc)
```

to the following

```
80064b00 li r4,0
         lfd f1, -0x77B8 (rtoc)
```

Since Gecko codes replace the original line you put it at, it is important to also include the original line, since in this case we do not want to use it.
