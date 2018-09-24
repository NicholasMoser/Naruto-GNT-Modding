# Choji Chips

## Details

When Choji eats chips, it will increase his chakra and his attack power. His attack power starts at 1.0 and will increase by 0.04 for each chip to a maximum of 1.5. It takes 13 chips to reach 1.5 power. The damage multiplier is stored at each character block absolute pointer (e.g. 0x80226358) + 0x2C4. The multiplier only affects normal contact hits, so it does not affect projectiles and supers. Throws are affected by this. This applies to all characters in the game.

Here is the full list of possible attack powers for each chip eaten, with each row being an additional chip eaten:

| Hex      |  Decimal  | 
|----------|-----------| 
| 3f800000 |  1        | 
| 3f851eb8 |  1.039999 | 
| 3f8a3d70 |  1.079999 | 
| 3f8f5c28 |  1.119999 | 
| 3f947ae0 |  1.159999 | 
| 3f999998 |  1.199999 | 
| 3f9eb850 |  1.239999 | 
| 3fa3d708 |  1.279999 | 
| 3fa8f5c0 |  1.319999 | 
| 3fae1478 |  1.359999 | 
| 3fb33330 |  1.399999 | 
| 3fb851e8 |  1.439999 | 
| 3fbd70a0 |  1.479999 | 
| 3fc00000 |  1.5      | 

0x00000000 for the float value (0 in decimal) does not completely remove damage; it makes the amount of damage very small. The function that modifies this value on a chip eat is at address 0x80017020. When the new attack power is larger than the max, it will go to line 0x8001703c which resets it to the max (1.5).



## Gecko Codes

Here are Gecko codes related to Choji's chips.

**No limit to Choji Chip Eating Attack Boost**  
C201703C 00000001  
60000000 00000000

![No Chip Max Attack](/gnt4/images/gameplay/no_chip_max.gif?raw=true "No Chip Max Attack")

## Value Modifiers

Attack power gain from chips can be modified in Choji's 0000.seq file at offset 0x1C41C. It is set to 0x3D23D70A which in decimal is 0.03999999910593033 (better known as 0.04). You can change the power increase to a power decrease by changing the 0x00000001 to 0x00000000 at offset 0x1C418; any other value will effectively disable the power change.

The size of the effect can be modified in Choji's 0000.seq file at offset 0x1C458. Here's an example of changing the size from 0x3FC00000 (1.5) to 0x40A00000 (5):

![Chip Eating Large Effect](/gnt4/images/gameplay/chip_eating_large_effect.gif?raw=true "Chip Eating Large Effect")