# GNT Special Addresses and Functions

The following memory locations can be used to modify game values while the game is running. This is useful for writing Gecko codes to change game logic. They can be modified by using Dolphin's built-in debug mode. Please note that these values may be used for other things in the game (many are used while the intro cutscene is playing), so side effects can occur.

## Addresses

**character_block_pointer** = 803E324C  
**Max Chakra** = [character_block_pointer] + 40  
**Chakra** = [character_block_pointer] + 44  
**Max KnJ** = [character_block_pointer] + 48  
**KnJ** = [character_block_pointer] + 4C  
**Character State** = [character_block_pointer] + 60  
*Note: Each of the above four values are 0x2710 by default*

A teleport will add the 2's compliment of the Max KNJ (0x00002710), which results in 0xFFFFE2B4.

### Character State Flags

Here are all of the flags that can be set for the character state address ([character_block_pointer] + 60).

**Intro Cutscene**  
8086_0002  
8086_0009

**Standing**  
0000_0000

**Moving Forward or Backwards**  
0200_0000

*Note: Includes running*

**Jump Once**  
0200_0000  
0800_0000  
4200_0000 (first touch ground)  
0200_0000  
0800_0000

*Note: Direction does not influence these values*

**Double Jump (from 08000000)**  
8000_0010  
4200_0010 (first touch ground)  
0200_0000 

**Throw Whiff**  
(no change)

**Successful Throw**  
0020_0000  
1020_0000 (released from throw)  
1000_0000 

**B**  
0200_0000 (begin animation)  
0600_0000 (active damage frames)

*Note: Whether it hits or not does not influence these values*

**A**  
0200_0000 (begin animation)

**X Whiff**  
4240_0008 (begin animation and invincibility)  
4240_0808 (???)  
4240_0008 (???)  
0240_0000 (exit cutscene)  
0640_0000 (active frames)

**X Hit**  
4240_0008 (begin animation and invincibility)  
4240_0808 (???)  
4240_0008 (???)  
0240_0000 (exit cutscene)  
6030_000A (hit)  
6030_0008 (begin cutscene)

**Sidestep (L or R)**  
0200_0000 (begin animation)  
0200_0008 (invincibility frames)

*Note: invicibility lasts 7 frames*

**Backstep (double back)**  
0200_0000 (begin animation)  
4200_0008 (invincibility frames)  
0200_0000 (non-invincible part of animation)

*Note: invicibility lasts 7 frames*

## Functions

### Teleport Checker

![Teleport Checker](/gntsp/images/functions/teleport_checker.png?raw=true "Teleport Checker")

First register 1 (sp) will be set to the character block. Then it will get the current KnJ amount and store it in register 0.

### KnJ Adjuster

![KnJ Adjuster](/gntsp/images/functions/knj_adjuster.png?raw=true "KnJ Adjuster")

Input:
* **Register 4**: KnJ Increase

This method will be called for every hit and the first teleport of battle[1]. It will load the current KnJ into register 3 on line 0x80064B3C and the max KnJ into register 6 on line 80064B44. The amount to add to your current KnJ is stored in register 4. The lowest amount of KnJ, zero, is stored in register 5. These values are used in the [KnJ Adder](#knj-adder) on line 0x80064B48. The new KnJ value is returned in register 3 and will be stored to your current KnJ value at [character_block_pointer] + 4C.

This method is called from one of two locations depending on if you are hit or if you are teleporting. If you are hit it will come from here:

![KnJ Adjust On Hit](/gntsp/images/functions/knj_adjust_on_hit.png?raw=true "KnJ Adjust On Hit")

If you are teleporting it will come from this function:

![KnJ Adjust On Teleport](/gntsp/images/functions/knj_adjust_teleporting.png?raw=true "KnJ Adjust On Teleport")

*[1] I am not entirely sure why it is only the first teleport.*

For more information about the second function (the one from teleporting), see [Teleport Handler](#teleport-handler)

### Teleport Handler

![Teleport Handler](/gntsp/images/functions/teleport_handler.png?raw=true "Teleport Handler")

This function will be called the first time you teleport in battle. It loads the Max KnJ into register 0 on line 0x80064B9C. It then calculates the 2's compliment of that value and stores the float double result in register 4 on line 0x80064BC4.

### KnJ Adder

![KnJ Adder](/gntsp/images/functions/knj_adder.png?raw=true "KnJ Adder")

Input:
* **Register 3**: KnJ Actual
* **Register 4**: KnJ Increase
* **Register 5**: KnJ Minimum
* **Register 6**: KnJ Maximum

Return:
* **Register 3**: New KnJ Actual

Located on line 0x8016DDB4, this function is called from the KnJ Adjuster to retrieve the new KnJ value. It will first add the *KnJ Increase* to the *KnJ Actual*. It will then set this new value to the *KnJ Minimum* if it is below the *KnJ Minimum*. Last, it will set this new value to the *KnJ Maximum* if it is above the *KnJ Maximum*. An example of when it will be above the maximum is when you take damage but are at full KnJ. It will return this new added KnJ value.
