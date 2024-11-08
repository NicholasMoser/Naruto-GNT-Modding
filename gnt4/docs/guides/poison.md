# Poison

This page describes my efforts to create a poison effect in-game.

## Existing Poison

There already exists health drain as a selectable handicap in-game. The code for it is in the function `damage_handler` at 0x8003e5f8.
There is also a health recovery effect that may be selected instead.

```c
/* Check if both health drain and auto recover health are enabled */
if ((chr_p->chr_modifiers & 0x20002000) != 0x20002000) {
    /* Check if health drain is enabled */
    if (((chr_p->chr_modifiers & 0x20000000) != 0) &&
        (chr_p->health_recovery_drain_counter = chr_p->health_recovery_drain_counter + 1,
        chr_p->health_recovery_drain_counter == 0x14)) {
        chr_p->health_recovery_drain_counter = 0;
        if (chr_p->current_dmg < (int)chr_p->max_damage) {
            chr_p->current_dmg = chr_p->current_dmg + 1;
        }
    }
    /* Check if auto recover health is enabled */
    if (((chr_p->chr_modifiers & 0x2000) != 0) &&
        (chr_p->health_recovery_drain_counter = chr_p->health_recovery_drain_counter + 1,
        chr_p->health_recovery_drain_counter == 0x14)) {
        chr_p->health_recovery_drain_counter = 0;
        chr_p->current_dmg = chr_p->current_dmg + -1;
        if (chr_p->current_dmg < 0) {
            chr_p->current_dmg = 0;
        }
    }
}
```

## New Poison

### How to Use It

First, if you just want the Gecko code to enable it:

```gecko
Enable Poison

C203EB9C 00000012
809C0148 54800043
4182007C 801C0274
5403843E 5404043E
38630001 38840001
5460801E 7C800378
901C0274 80BC0278
54A0843E 7C030000
4082002C 38600000
5460801E 7C800378
901C0274 807C0260
801C027C 7C030000
4080000C 38030001
901C0260 54A3043E
7C032000 40820018
38000000 901C0274
809C0148 54840080
909C0148 807C0280
60000000 00000000
```

Then to actually enable it, you must do three things:

1. Enable EF flag 0x40000000 (located at chr_p->0x148).
2. Initialize the timers to 0x00000000 (located at chr_p->0x274).
3. Set the **Damage Every X Frames** and **End Poison at Frame X**. Each is two bytes,
   so for example if you want to do damage every 3 frames and end on frame 9, you
   would use the value 0x00030009 (located at chr_p->0x278).

For 2 and 3, you would apply this to yourself with

```
04026600 00000274 3F000000 00000000
04026600 00000278 3F000000 00030009
```

and to the opponent with

```
04026700 00000274 3F000000 00000000
04026700 00000278 3F000000 00030009
```

### How it Works

To create a new poison effect, we need a few different components.
First we need a poison flag; we can use the unused EF Flag 0x40000000.
Then we need 4 variables:

1. A timer to track frames until damage should be done.
2. A frame count to do damage on (e.g. frame 20).
3. A timer to track how long the poison has lasted.
4. A frame count to end the poison on (e.g. frame 300).

Each of these may end up larger than 255 frames, so we will want to use at least 2 bytes for each.
We also need to make sure these values are cleaned up at the appropriate time in-game, i.e. at round end.
Because of these reasons, I think it makes sense to hijack existing `chr_p` variables.
We can re-use the existing health drain/recovery variable, as well as use what appears to be an unused variable.
These are located at `chr_p` offset 0x274 and 0x278 respectively. So when packed:

```
- 0x274
  - (2 bytes) -> damage_frame_count (should start at 0)
  - (2 bytes) -> total_frame_count (should start at 0)
- 0x278
  - (2 bytes) -> damage_every_x_frames (e.g. damage every 0x14 frames)
  - (2 bytes) -> end_poison_at_frame_x (e.g. end at frame 0x12C, aka 300)
```

The new code should look something like this:

```c
// Extract the four variables from the two 32-byte addresses
uint32_t word1 = chr_p->0x274;
uint16_t damage_frame_count = (word1 >> 16) & 0xFFFF; // Extract the upper 16 bits (first 2 bytes)
uint16_t total_frame_count = word1 & 0xFFFF;          // Extract the lower 16 bits (second 2 bytes)

uint32_t word2 = chr_p->0x278;
uint16_t damage_every_x_frames = (word2 >> 16) & 0xFFFF; // Extract the upper 16 bits (first 2 bytes)
uint16_t end_poison_at_frame_x = word2 & 0xFFFF;         // Extract the lower 16 bits (second 2 bytes)

// Increment the counters
damage_frame_count = damage_frame_count + 1;
total_frame_count = damage_frame_count + 1;

// If we are on a damage frame, do damage
if (damage_frame_count == damage_every_x_frames) {
    // Reset counter
	damage_frame_count = 0;
    // Will avoid killing, change this to <= to kill
	if (chr_p->current_dmg < chr_p->max_damage) {
		chr_p->current_dmg = chr_p->current_dmg + 1;
	}
}

// If we are at the end of poison, remove poison flag and reset counters
if (total_frame_count == end_poison_at_frame_x) {
	total_frame_count = 0;
	damage_frame_count = 0;
	chr_p->ef_flags &= ~(0x40000000);
}
```

Which results in the following assembly code:

```ppc
@8003EB9C

/* We have registers r0, r3, r4, r5 available */
start:
  lwz r4, 328(r28)
  /* Check bitflag 0x40000000 */
  rlwinm. r0, r4, 0, 1, 1
  beq- end

  /* Poison flag is turned on, start running poison code */
  lwz r0, 0x274 (r28)

  /* damage_frame_count set to r3 */
  srwi    r3,r0,0x10

  /* total_frame_count set to r4 */
  clrlwi  r4,r0,0x10

  /* Increment both damage_frame_count and total_frame_count */
  addi r3, r3, 0x1
  addi r4, r4, 0x1

  /* Repack and store to chr_p->0x274 */
  slwi    r0,r3,0x10
  or      r0,r4,r0
  stw r0, 0x274 (r28)
  
  /* Load damage_every_x_frames into r0 */
  lwz r5, 0x278 (r28)
  srwi    r0,r5,0x10

  /* damage_frame_count == damage_every_x_frames */
  cmpw r3, r0
  bne- check_poison_end

  /* Reset damage_frame_count and store to chr_p->0x274 */
  li r3, 0x0
  slwi    r0,r3,0x10
  or      r0,r4,r0
  stw r0, 0x274 (r28)

  /* Check that current damage is under max damage */
  lwz r3, 608(r28)
  lwz r0, 636(r28)
  cmpw r3, r0
  bge- check_poison_end

  /* Do 1 damage to character */
  addi r0, r3, 0x1
  stw r0, 608(r28)

check_poison_end:
  /* Set r3 to end_poison_at_frame_x */
  clrlwi  r3,r5,0x10

  /* total_frame_count == end_poison_at_frame_x */
  cmpw r3, r4
  bne end

  /* Reset total_frame_count and damage_frame_count */
  li r0, 0
  stw r0, 0x274 (r28)

  /* Unset poison flag */
  lwz r4, 328(r28)
  rlwinm  r4,r4,0,2,0
  stw r4, 328(r28)
end:
  lwz r3, 640(r28)


```
