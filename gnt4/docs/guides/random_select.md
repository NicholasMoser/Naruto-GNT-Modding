# GNT4 Random Select

In Naruto GNT4, there is no character select in the character select menus. This page talks about the code to add a random select to the game. Using this code, random select is activated by holding **Start** and hitting **Down** on the control stick in any character select menu. It will also work for all four players if in multiplayer.

![Random Select](/gnt4/images/gameplay/random_select.gif?raw=true "Random Select")

## Code

### Gecko Code

```hex
C2091ED4 00000015
3C800145 7C043800
40820098 2C1F0020
4082001C 3C808022
60842D40 80840000
5484843E 2C041000
41820064 2C1F0021
4082001C 3C808022
60842D4C 80840000
5484843E 2C041000
41820044 2C1F0022
4082001C 3C808022
60842D58 80840000
5484843E 2C041000
41820024 2C1F0023
40820030 3C808022
60842D64 80840000
5484843E 2C041000
40820018 7F63DB78
3C80801C 6084CE50
7C8903A6 4E800421
808D8878 00000000
C2091EE8 00000003
2C030000 41820008
7C601B78 7C04292E
60000000 00000000
```

### Assembly

80091ed4: 
```assembly
lis r4, 0x145
cmpw r4, r7
bne 152
cmpwi r31, 0x20
bne 28
lis r4, 0x8022
ori r4, r4, 0x2d40
lwz r4, 0 (r4)
srwi r4, r4, 16
cmpwi r4, 0x1000
beq 100
cmpwi r31, 0x21
bne 28
lis r4, 0x8022
ori r4, r4, 0x2d4c
lwz r4, 0 (r4)
srwi r4, r4, 16
cmpwi r4, 0x1000
beq 68
cmpwi r31, 0x22
bne 28
lis r4, 0x8022
ori r4, r4, 0x2d58
lwz r4, 0 (r4)
srwi r4, r4, 16
cmpwi r4, 0x1000
beq 36
cmpwi r31, 0x23
bne 48
lis r4, 0x8022
ori r4, r4, 0x2d64
lwz r4, 0 (r4)
srwi r4, r4, 16
cmpwi r4, 0x1000
bne 24
mr r3, r27
lis r4, 0x801c
ori r4, r4, 0xce50
mtctr r4
bctrl
lwz    r4, -0x7788 (r13)
```

80091ee8:

```assembly
cmpwi r3, 0
beq 8
mr r0, r3
stwx r0, r4, r5
```

## Explanation

### Considerations

There are a handful of considerations with writing a code for random select:

* How to get a random value in the game
* How to make sure all players have the ability to use it
* How to make sure that the character select menu in all games modes have access to it
* How to make sure there are no side effects in other menus (or in general)
* Where is the best place to put the code at

I'll address each of these points, along with explain how each of them are solved by a specific line of the code. Let's start by talking about the most difficult portion, how to get a random value in the game.

### Random Value Retrieval

Video games have a variety of ways to get random values. My first strategy was to see how GNT4 handles random values in the code and hijack it for my random select. The only two places I could think of that would be using random values are the mission unlock order and the random stage select. Since the random stage select is much easier to access I decided to use that as my reference.

When hovering over random select, this block of code is hit continuously. This is the location where the currently selected random stage is set. Every 8th time it is hit, is for random stage value. Who knows what the other 7 are for.

![Random Selection State](/gnt4/images/functions/random_selection_state.png?raw=true "Random Selection State")

However we need to go back further to see where the random value is actually obtained.

![Kinda RNG](/gnt4/images/functions/kinda_rng.png?raw=true "Kinda RNG")

r5 is set to an offset, such as 0x0000243c or 0x00002430. r6 is set to 0x802c6780, the start of a list of "RNG values" in memory. r5 and r6 are added to get the associated random value. I mapped out the locations in memory to see the spread of values it chooses from:

r28 input and output:

```hex
     0 ->  0 + 23f0 = 23f0 + 802c6780 = [802c8b70] =  7
     1 ->  4 + 24f0 = 23f4 + 802c6780 = [802c8b74] =  8
     2 ->  8 + 23f0 = 23f8 + 802c6780 = [802c8b78] =  f
     3 ->  c + 23f0 = 23fc + 802c6780 = [802c8b7c] = 16
     4 -> 10 + 23f0 = 2400 + 802c6780 = [802c8b80] = 1d
     5 -> 14 + 23f0 = 2404 + 802c6780 = [802c8b84] =  6
     6 -> 18 + 23f0 = 2408 + 802c6780 = [802c8b88] =  a
     7 -> 1c + 23f0 = 240c + 802c6780 = [802c8b8c] =  b
     8 -> 20 + 23f0 = 2410 + 802c6780 = [802c8b90] = 18
     9 -> 24 + 23f0 = 2414 + 802c6780 = [802c8b94] = 19
     a -> 28 + 23f0 = 2418 + 802c6780 = [802c8b98] = 11
     b -> 2c + 23f0 = 241c + 802c6780 = [802c8b9c] = 12
     c -> 30 + 23f0 = 2420 + 802c6780 = [802c8ba0] =  d
     d -> 34 + 23f0 = 2424 + 802c6780 = [802c8ba4] =  4
     e -> 38 + 23f0 = 2428 + 802c6780 = [802c8ba8] = 13
     f -> 3c + 23f0 = 242c + 802c6780 = [802c8bac] = 15
    10 -> 40 + 23f0 = 2430 + 802c6780 = [802c8bb0] =  c
    11 -> 44 + 23f0 = 2434 + 802c6780 = [802c8bb4] =  e
    12 -> 48 + 23f0 = 2438 + 802c6780 = [802c8bb8] = 1a
    13 -> 4c + 23f0 = 243c + 802c6780 = [802c8bbc] = 1c
    14 -> 50 + 23f0 = 2440 + 802c6780 = [802c8bc0] = 14
    15 -> 54 + 23f0 = 2444 + 802c6780 = [802c8bc4] =  5
    16 -> 58 + 23f0 = 2448 + 802c6780 = [802c8bc8] = 1b
    17 -> 5c + 23f0 = 244c + 802c6780 = [802c8bcc] =  0
    18 -> 60 + 23f0 = 2450 + 802c6780 = [802c8bd0] =  9
    19 -> 64 + 23f0 = 2454 + 802c6780 = [802c8bd4] =  1
    1a -> 68 + 23f0 = 2458 + 802c6780 = [802c8bd8] = 10
    1b -> 6c + 23f0 = 245c + 802c6780 = [802c8bdc] =  2
    1c -> 70 + 23f0 = 2460 + 802c6780 = [802c8be0] = 17
    1d -> 74 + 23f0 = 2464 + 802c6780 = [802c8be4] = 1e
    1e -> 78 + 23f0 = 2468 + 802c6780 = [802c8be8] =  3
    1f -> 7c + 23f0 = 246c + 802c6780 = [802c8bec] = 1f
```

Unfortunately I can't use this same spread for my own purposes since there's not enough values here to cover the number of characters (0x26). But in addition to that I'm not even sure how the offset is generated, so I decided to look into other ways to do this.

#### Of Course Melee Did It Right

Super Smash Brothers Melee, another GameCube title, uses a [Linear Congruential Generator](https://en.wikipedia.org/wiki/Linear_congruential_generator). You can read more about what that means and how it uses it here: [The Basics of RNG in Melee](https://www.reddit.com/r/SSBM/comments/71gn1d/the_basics_of_rng_in_melee/). However, what is really interesting is that the Linear Congruential Generator assembly code that Melee uses comes from a standard in Microsoft Visual/Quick C/C++. It actually turns out that GNT4 has the **exact** same function in the game:

#### Melee Random Int

![Melee Random Int](/gnt4/images/functions/melee_random_int.png?raw=true "Melee Random Int")

#### GNT4 Random Int

![GNT4 Random Int](/gnt4/images/functions/gnt4_random_int.png?raw=true "GNT4 Random Int")

The main differences being them located in different places in the code, the different memory location offset (0x570c vs 0x7a20), and the order of the registers in the last three lines. There is also a function in both games for a random float, which you can see here:

#### Melee Random Float

![Melee Random Float](/gnt4/images/functions/melee_random_float.png?raw=true "Melee Random Float")

#### GNT4 Random Float

![GNT4 Random Float](/gnt4/images/functions/gnt4_random_float.png?raw=true "GNT4 Random Float")

The random float function in GNT4 is called in around 52 different locations, particularly for in-game effects like dust and hit effects. The random integer function in GNT4 however is only called in two places, 0x801cd374 and 0x801ce40c which are both in the function at 0x801cce8c. I wasn't able to figure out what these locations are for, but that doesn't matter for writing this code.

The random integer function takes in r3 as a parameter and return value. It additionally uses registers r0, r4, and r5 so we need to make sure we are okay with these values being overriden. The r3 parameter represents the maximum integer we want returned from the function (non-inclusive), with zero being the minimum. r3 also holds the return value, our random value. We can branch to this method whenever we want, so now we have the random portion figured out.

### Random Character Select

When in character select, there are two locations in memory that store the currently selected character in random select. One of these I call the visual value, the other I call the actual value. The visual value is what you see is actually selected in the game, but the actual value is what is truly selected. Modifying one but not the other means that what is selected on the screen does not much what is actually selected. Therefore we want to make sure that both are modified.

The actual value is written to first. The visual value grabs the actual value and uses that. Therefore we only need to change what value is written to the actual value to affect the visual value, assuming we insert the code before the visual value is set. Unfortunately, different gamemodes use different memory locations to store the actual value and visual value. Training mode uses 0x802D5D14 for the visual value and 0x802DB4E0 for the actual value whereas four player mode uses different locations. Therefore it makes sense to add the new code somewhere near the point that the actual value is set since we have the memory locations of the actual value in context.

So where is the actual value set at in the code? The actual value is written to on line 0x80091ee8 when down on the control stick is pressed and 80091e5c when up on the control stick is pressed. I decided to choose down (0x80091ee8) as the area I write my code for this case, although up would work just as fine. It is important to realize those that any menu in the game will hit this location, so we also need a way to distinguish between character select menus and other menus.

Also we need to make sure that the new code is only triggered when one of the players are holding Start. Therefore we need to retrieve the value stored in memory for each of their controllers. But we only want to get the value associated with the character that triggered the menu movement. So with all of this information we can now look at how to write the code.

### 0x80091ee8

0x80091ee8 is the location where the character select actual value is set. In order to examine this area of code, I took images of the register state in various scenarios:

![Menu Registers](/gnt4/images/functions/menu_registers.png?raw=true "Menu Registers")

So using this information, here are some of the important values stored in the registers at 80091ee8:

* r0: New index
* r1: Always 8028c4b0 (stack pointer?)
* r3: 0, until the selection overflow check. If overflow occurs, set to r29 + 20
* r4: Character selection base address
  * Menus:    802fd600
  * Versus:   802db440
  * Practice: 802db460
  * FFA:      802df560
* r5: Character selection offset
  * P1: 80
  * P2: 84
  * P3: 88
  * P4: 8c
* r7: Flag for character select is 0x01450000
* r13: Subtract 0x7788 from this address to get the address for the old value.
* r27: The max value for the list (inclusive). 27 for character select.
* r30: Amount to add for selection move (always 1)
* r31: Value used to get the character selection offset
  * P1: 20
  * P2: 21
  * P3: 22
  * P4: 23

Using these values we have everything we need to solve the original considerations in the first section.

> How to get a random value in the game

Use the random integer function at 0x801cce50

> How to make sure all players have the ability to use it

Check the value of r31 to see which player triggered the menu movement and then check that player's controller input memory location.

> How to make sure that the character select menu in all games modes have access to it

Since we are overriding the setting of the actual value we will always have the correct memory address in context

> How to make sure there are no side effects in other menus (or in general)

By checking the value of r7 in that it is 0x01450000 so that we know we're in the character select menu and not a different menu.

> Where is the best place to put the code at

Somewhere around 0x80091ee8.

So with this being said let's look at the location we will add our code in:

![GNT4 Down Menu](/gnt4/images/functions/gnt4_down_menu.PNG?raw=true "GNT4 Down Menu")

There is immediately an issue present in that r4 and r5 are used in this block of code, but random_int() also requires using r4 and r5. Therefore it makes the most sense to add our new code before r4 and r5 are set, so this will actually be added at 0x80091ed4. We first will check that r7 is equal to 0x01450000 so that we know we are in the character select menu and not a different menu. If it is not equal, ignore the rest of the newly added code. Once we know we're in the character select menu see which character performed the movement by seeing whether r31 is equal to 0x20. 0x21, 0x22, or 0x23. Once we know which player performed it, check the inputs of their respective controller and memory and see if Start is being held. If it is then go to the random_int() function. Use the return value as the new character select value.

### C Code

To help me understand what I want the code to do I decided to write a C program to show what I want to occur. Additionally, using the [Writing Codes for Melee in C Guide](https://smashboards.com/threads/writing-codes-for-melee-in-c.425351/) along with DevKitPro, I was able to compile the program into assembly to get a good baseline for what I want the end assembly to look like.

0x80091ed4:

```c
#include <stdint.h>

// Random Integer Function
#define GNT4_RANDOM_INT 0x801CCE50

// Player controller inputs memory locations
#define GNT4_PLAYER_1_CONTROLLER 0x80222D40
#define GNT4_PLAYER_2_CONTROLLER 0x80222D4C
#define GNT4_PLAYER_3_CONTROLLER 0x80222D58
#define GNT4_PLAYER_4_CONTROLLER 0x80222D64

// r7 set to this when in Character Select menu
#define GNT_CHARACTER_SELECT_VALUE 0x01450000

// r31 set to this when depending on which Player moved
#define GNT4_PLAYER_1_MOVEMENT 0x20
#define GNT4_PLAYER_2_MOVEMENT 0x21
#define GNT4_PLAYER_3_MOVEMENT 0x22
#define GNT4_PLAYER_4_MOVEMENT 0x23

// Movement to trigger random select, only Start in this case
#define RANDOM_INPUT 0x1000

int _main() {
    // Built-in function setup
    uint32_t * (*random_int)(int) = GNT4_RANDOM_INT;

    // Memory location setup
    int p1 = *(int*)GNT4_PLAYER_1_CONTROLLER;
    int p2 = *(int*)GNT4_PLAYER_2_CONTROLLER;
    int p3 = *(int*)GNT4_PLAYER_3_CONTROLLER;
    int p4 = *(int*)GNT4_PLAYER_4_CONTROLLER;

    // Set to 0 for example, will have actual values in the registers during runtime
    int r31 = 0;
    int r7 = 0;

    if (r7 == GNT_CHARACTER_SELECT_VALUE)
    {
        if (r31 == GNT4_PLAYER_1_MOVEMENT)
        {
            if (p1 == RANDOM_INPUT)
            {
                int rand = random_int(TEST1);
            }
        }
        else if (r31 == GNT4_PLAYER_2_MOVEMENT)
        {
            if (p2 == RANDOM_INPUT)
            {
                int rand = random_int(TEST1);
            }
        }
        else if (r31 == GNT4_PLAYER_3_MOVEMENT)
        {
            if (p3 == RANDOM_INPUT)
            {
                int rand = random_int(TEST1);
            }
        }
        else if (r31 == GNT4_PLAYER_4_MOVEMENT)
        {
            if (p4 == RANDOM_INPUT)
            {
                int rand = random_int(TEST1);
            }
        }
    }
}
```

One thing to note is that this C code has four separate calls to random_int(). Since the actual call is more than one line, I decided to use branching to make sure that each of the four places it can call the function instead branch to one location in the code that calls it to minimize the amount of code. Also the output assembly from DevKitPro has lots of unnecessary initialization we can remove since the values will already exist in memory where we put the code at. With that being said, I next wrote the final assembly along with comments describing what is occuring.

### Assembly Code with Comments

80091ed4:

```assembly
// First compare r4 with 0x145. For whatever reason, only character select menus use this value and any
// other menus use a different value. If r4 is not 0x145 branch to the end and ignore all of this new code.
lis r4, 0x145
cmpw r4, r7
bne 152

// See if this was a movement made by the first player by comparing r31 to 0x20.
// If it is not, go to the check for the second player.
cmpwi r31, 0x20
bne 28

// Load the buttons pressed for the first controller into r4
lis r4, 0x8022
ori r4, r4, 0x2d40
lwz r4, 0 (r4)

// The 16 high-order bits represent the buttons pressed, the 16 low-order bits represent the stick motion.
// We only want to compare against the buttons pressed, so we can do a 16-bit right shift to replace the low-order
// 16-bits with the high-order 16 bits. This will replace the 16 high-order bits with zeroes.
// We compare against 0x1000 since that would be only the start button being pressed.
// If start is being pressed branch to the random_int() portion ahead.
srwi r4, r4, 16
cmpwi r4, 0x1000
beq 100

// See if this was a movement made by the second player by comparing r31 to 0x21.
// If it is not, go to the check for the third player.
cmpwi r31, 0x21
bne 28

// Load the buttons pressed for the second controller into r4
// Load the
lis r4, 0x8022
ori r4, r4, 0x2d4c
lwz r4, 0 (r4)

// The 16 high-order bits represent the buttons pressed, the 16 low-order bits represent the stick motion.
// We only want to compare against the buttons pressed, so we can do a 16-bit right shift to replace the low-order
// 16-bits with the high-order 16 bits. This will replace the 16 high-order bits with zeroes.
// We compare against 0x1000 since that would be only the start button being pressed.
// If start is being pressed branch to the random_int() portion ahead.
srwi r4, r4, 16
cmpwi r4, 0x1000
beq 68

// See if this was a movement made by the third player by comparing r31 to 0x22.
// If it is not, go to the check for the fourth player.
cmpwi r31, 0x22
bne 28

// Load the buttons pressed for the third controller into r4
lis r4, 0x8022
ori r4, r4, 0x2d58
lwz r4, 0 (r4)

// The 16 high-order bits represent the buttons pressed, the 16 low-order bits represent the stick motion.
// We only want to compare against the buttons pressed, so we can do a 16-bit right shift to replace the low-order
// 16-bits with the high-order 16 bits. This will replace the 16 high-order bits with zeroes.
// We compare against 0x1000 since that would be only the start button being pressed.
// If start is being pressed branch to the random_int() portion ahead.
srwi r4, r4, 16
cmpwi r4, 0x1000
beq 36

// See if this was a movement made by the fourth player by comparing r31 to 0x23.
// If it is not, skip the rest of the new code and branch to the end.
cmpwi r31, 0x23
bne 48

// Load the buttons pressed for the fourth controller into r4
lis r4, 0x8022
ori r4, r4, 0x2d64
lwz r4, 0 (r4)

// The 16 high-order bits represent the buttons pressed, the 16 low-order bits represent the stick motion.
// We only want to compare against the buttons pressed, so we can do a 16-bit right shift to replace the low-order
// 16-bits with the high-order 16 bits. This will replace the 16 high-order bits with zeroes.
// We compare against 0x1000 since that would be only the start button being pressed.
// If start is NOT being pressed, skip the rest of the code and branch to the end.
srwi r4, r4, 16
cmpwi r4, 0x1000
bne 24

// This is the random_int() portion of the new code.
// The value of r27 is the maximum number of menu selections (characters in this case). The random_int() function
// for the game takes r3 as a parameter for the maximum int to return (non-inclusive). It will store the new
// random value in r3. Move the value of r27 to r3 so that we can use it as a parameter for random_int().
// Put the location of the random_int() function (801cce50) into r4 and branch to it.
mr r3, r27
lis r4, 0x801c
ori r4, r4, 0xce50
mtctr r4
bctrl
lwz    r4, -0x7788 (r13)
```

80091ee8:

```assembly
// After the portion of code where we increment or decrement the selected character value,
// we need to check if we're using a random select value instead and replace it.
// Check if there is a value set for r3. If there is, move the value of r3 to r0.
// This will override the selection that would have been used if start was not held to do random select.
cmpwi r3, 0
beq 8
mr r0, r3
stwx r0, r4, r5
```
