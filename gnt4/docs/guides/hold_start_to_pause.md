# Hold Start to Pause

This page documents my efforts to create a Gecko code to hold start to pause in player vs player fights. The benefit of such a code is to
prevent accidental pauses during matches.

## The Code

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
```

## Assembly

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

## Explanation

The goal for this code is to have an internal memory address that keeps track of how many frames start is held. If it reaches a certain value,
then and only then, will the pause menu actually be activated.

We store the start counter at memory address 0x80276B8C, which is unused space in the OdemuExi2 code (unreachable developer debugging code).
If start is being held, we increment this value. If it is over the max value (currently 0x14 frames), then we reset the counter and trigger the
pause menu. Otherwise, we increment the counter and do not trigger the pause menu. If at any frame start is not held, the counter is reset to 0.

One problem is that the memory address read for start being pressed is at offset 0x28 of a controller struct. This field is `pressed_buttons`
and each frame will only have new buttons that have been pressed. So pressing start will set it to 0x1000 the first frame, but will reset it to
0 every frame after until a new button is pressed. For this code, we instead use offset 0x24 of the controller struct which is `held_buttons`.
`held_buttons` will have every currently held button every frame, therefore we can use this to track how long start is held.

The code will only work for non-training battle modes since it is currently in the function `battle_menu_handler`. To create a similar code for
training mode, the code would need to be written in the function `training_mode_menu_handler`.
