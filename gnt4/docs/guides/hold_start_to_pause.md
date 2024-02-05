# Hold Start to Pause

This page documents my efforts to create a Gecko code to hold start to pause in player vs player fights. The benefit of such a code is to
prevent accidental pauses during matches.

## The Codes


### Hold Start to Pause

To change the amount of frames to hold start to pause, change the 0x14 at the end of `2C040014` to the number you wish to use.

```gecko
C20477B0 0000000B
801D0024 540004E7
4182003C 3C608027
80836B8C 2C040014
4081001C 38000000
90036B8C 38001000
3C608022 90032ED8
48000024 38040001
90036B8C 38000000
48000014 38800000
3C608027 90836B8C
38000000 00000000
04047824 800400e4
04047848 800300a4
04047864 80030064
04047880 80030024
```

### Display Player Who Paused

```gecko
042182f0 20504155
042182f4 53454420
042182f8 42592050
C204765C 00000002
3D008022 390882F0
60000000 00000000
C2047838 00000003
38003420 3C608022
B00382FC 38000003
60000000 00000000
C2047854 00000003
38003320 3C608022
B00382FC 38000002
60000000 00000000
C2047870 00000003
38003220 3C608022
B00382FC 38000001
60000000 00000000
C204788C 00000003
38003120 3C608022
B00382FC 38000000
60000000 00000000
C20478A4 00000009
2C000003 40820008
38003420 2C000002
40820008 38003320
2C000001 40820008
38003220 2C000000
40820008 38003120
3C608022 B00382FC
801D0038 2000FFFF
901C0028 00000000
```

## General Explanation

The goal for this code is to have an internal memory address that keeps track of how many frames start is held. If it reaches a certain value,
then and only then, will the pause menu actually be activated.

We store the start counter at memory address 0x80276B8C, which is unused space in the OdemuExi2 code (unreachable developer debugging code).
If start is being held by any player, we increment this value. If it is over the max value (currently 0x14 frames), then we reset the counter
and trigger the pause menu. Otherwise, we increment the counter and do not trigger the pause menu. If at any frame start is not held,
the counter is reset to 0.

One problem is that the memory address read for start being pressed is at offset 0x28 of a controller struct. This field is `pressed_buttons`
and each frame will only have new buttons that have been pressed. So pressing start will set it to 0x1000 the first frame, but will reset it to
0 every frame after until a new button is pressed. For this code, we instead use offset 0x24 of the controller struct which is `held_buttons`.
`held_buttons` will have every currently held button every frame, therefore we can use this to track how long start is held.

Another problem ran into is that at 0x80047824, 0x80047848, 0x80047864, and 0x80047880 we check pressed buttons on each controller to determine
the player who paused. Since start is being held and not pressed, none of these will ever show the button having been pressed. Therefore we must
instead read the memory address 4 bytes before these, which is the **held buttons** for each controller. Whichever controller is holding start
on the last frame of the frame count will be the one who paused. If multiple players are holding pause on the last frame, the lower controller
number will be the one to pause.

Last, there was an idea to identify visually which player paused. This can be done by modifying the "PAUSED" text in memory. Unfortunately,
the existing "PAUSED" text at 0x80278a50 only has 8 bytes available (7 characters with a null terminator). This limits the length of the text
we can use. But also, 0x80278a50 is in [sdata2](https://refspecs.linuxfoundation.org/LSB_3.1.0/LSB-Core-PPC32/LSB-Core-PPC32/sections.html)
which is initialized unmodifiable data anyways, so we must use text from somewhere else. 0x802182f0 was available so I used that.

The code will only work for non-training battle modes since it is currently in the function `battle_menu_handler`. To create a similar code for
training mode, the code would need to be written in the function `training_mode_menu_handler`.

## Hold Start to Pause Code Explanation

The following PowerPC assembly code is inserted at 0x800477B0. To change the amount of frames to hold start to pause,
change the 0x14 under the `update_counter` label to the number you wish to use.

```asm
check_start:
  # Check if start is pressed
  lwz r0, 36(r29)
  rlwinm. r0, r0, 0, 19, 19
  beq- reset_counter
  
update_counter:
  # Update the counter and compare with the max value
  lis r3, 0x8027
  lwz r4, 27532(r3)
  cmpwi r4, 0x14
  ble- increment_counter
  
complete_start:
  # Reset counter and return 0x1000 (successful start)
  li r0, 0x0
  stw r0, 27532(r3)
  li r0, 0x1000
  lis r3, 0x8022
  stw r0, 11992(r3)
  b end

increment_counter:
  # Increment the counter and return 0
  addi r0, r4, 0x1
  stw r0, 27532(r3)
  li r0, 0x0
  b end

reset_counter:
  # Reset counter and return 0
  li r4, 0x0
  lis r3, 0x8027
  stw r4, 27532(r3)
  li r0, 0x0

end:
```

```gecko
C20477B0 0000000B
801D0024 540004E7
4182003C 3C608027
80836B8C 2C040014
4081001C 38000000
90036B8C 38001000
3C608022 90032ED8
48000024 38040001
90036B8C 38000000
48000014 38800000
3C608027 90836B8C
38000000 00000000
```

Then, we must change the pressed button variables to held button variables for each controller,
or else they won't register which player paused. See below in **Explanation** for more info.

```gecko
04047824 800400e4
04047848 800300a4
04047864 80030064
04047880 80030024
```

## Display Player Who Paused Code Explanation

Now, we want to display in-game which player paused. First, we create the String " PAUSED BY P".
We will modify this String in memory to add the 1, 2, 3, or 4 to the end of it. We must make sure that
the bytes we plan to modify are not inserted by the 04 code, because the 04 code runs every frame and would
overwrite our changes.

```gecko
042182f0 20504155
042182f4 53454420
042182f8 42592050
```

Then, we must replace references to the old "PAUSED" text with the new one. We really just need to
update the main reference that battle modes use:

```asm
  lis r8, 0x8022
  subi r8, r8, 0x7D10
```

```gecko
C204765C 00000002
3C608022 386382F0
60000000 00000000
```

We also need to modify the P1 in the new String with P2, P3, and P4 respectively for each player.

```asm
  li r0, 0x3420
  lis r3, 0x8022
  sth r0, -32004(r3)
  li r0, 0x3
```

```gecko
C2047838 00000003
38003420 3C608022
B00382FC 38000003
60000000 00000000
```

```asm
  li r0, 0x3320
  lis r3, 0x8022
  sth r0, -32004(r3)
  li r0, 0x2
```

```gecko
C2047854 00000003
38003320 3C608022
B00382FC 38000002
60000000 00000000
```

```asm
  li r0, 0x3220
  lis r3, 0x8022
  sth r0, -32004(r3)
  li r0, 0x1
```

```gecko
C2047870 00000003
38003220 3C608022
B00382FC 38000001
60000000 00000000
```

```asm
  li r0, 0x3120
  lis r3, 0x8022
  sth r0, -32004(r3)
  li r0, 0x0
```

```gecko
C204788C 00000003
38003120 3C608022
B00382FC 38000000
60000000 00000000
```

Last, we must update the code where a controller disconnects and sets the player who disconnected.
This code is at 0x800478a0.

```asm
player_4:
  cmpwi r0, 0x3
  bne- player_3
  li r0, 0x3420

player_3:
  cmpwi r0, 0x2
  bne- player_2
  li r0, 0x3320

player_2:
  cmpwi r0, 0x1
  bne- player_1
  li r0, 0x3220

player_1:
  cmpwi r0, 0x0
  bne- store_and_reload_r0
  li r0, 0x3120

store_and_reload_r0:
  lis r3, 0x8022
  sth r0, -32004(r3)
  lwz r0, 56(r29)
  subfic r0, r0, -1
  stw r0, 40(r28)
```

```gecko
C20478A4 00000009
2C000003 40820008
38003420 2C000002
40820008 38003320
2C000001 40820008
38003220 2C000000
40820008 38003120
3C608022 B00382FC
801D0038 2000FFFF
901C0028 00000000
```

## Rev3 (US) Code

A similar code was written for Rev3, but unfortunately it is more complicated.

The main difference is that the pause is checked for every player every frame. Therefore, the counter if incremented every iteration will be increased by 2 every frame if there are two players. This is handled by simply doubling the number of frames to wait. Obviously this is a problem for 3 or 4 players, but this code wouldn't be used for 3 or 4 player modes.

Additionally, we need a check for the pressed button of the current player to start the counter or else it will always start on player 1, meaning that player 2 pausing will open the player 1 pause menu. The frames to wait also must be an odd number so that the player that starts the pause counter is the same player it ends on.

```gecko
C208A830 0000000D
80A30050 3C60803C
3863D7B0 8003004C
540005EF 41820040
808D828C 2C040000
4082000C 2C050100
4082002C 2C040029
40810014 38000000
900D828C 38000100
48000020 38040001
900D828C 38000000
48000010 38800000
908D828C 38000000
60000000 00000000
```

```asm
check_start:
  # Check if start is pressed
  lwz r5, 80(r3) # Load pressed button of current player
  lis r3, 0x803C 
  subi r3, r3, 0x2850
  lwz r0, 76(r3) # Load held buttons of all players
  rlwinm. r0, r0, 0, 23, 23
  beq- reset_counter
  lwz r4, -32116(r13)
  cmpwi r4, 0x0
  bne- compare_max
  cmpwi r5, 0x100 # This code is to make sure that the player actually holding start begins the counter
  bne- reset_counter

compare_max:
  cmpwi r4, 0x29 # Needs to be higher since it's incremented every frame for every player
  ble- increment_counter
  
complete_start:
  # Reset counter and return 0x1000 (successful start)
  li r0, 0x0
  stw r0, -32116(r13)
  li r0, 0x100
  b end

increment_counter:
  # Increment the counter and return 0
  addi r0, r4, 0x1
  stw r0, -32116(r13)
  li r0, 0x0
  b end

reset_counter:
  # Reset counter and return 0
  li r4, 0x0
  stw r4, -32116(r13)
  li r0, 0x0

end:
```
