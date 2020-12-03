# SEQ Files

Files ending with .seq dictate just about everything about the UI and characters that aren't art assets. This includes damage, speed, which animation to play, hitboxes, etc. For example, a character's `0000.seq` file contains action data, while `0010.seq` appears to contain data for CPU control (AI).

## Decompilation

There currently is an effort to decompile the seq parsing code of the game, which can be found under [SEQ Decompilation](/gnt4/docs/guides/seq_decomp.md).

## Table of Contents

1. **[How to Read Sequence Files](#how-to-read-sequence-files)**
2. **[Flag Tables](#flag-tables)**
3. **[Action ID References](#action-id-references)**
4. **[Action ID to Known Action States](#action-id-to-known-action-states)**
5. **[KF Attack Flags](#kf-attack-flags)**
6. **[K2F Special Attack Flags](#k2f-special-attack-flags)**
7. **[NF State Flags](#nf-state-flags)**
8. **[AF Action State Flags](#af-action-state-flags)**

*Credit to TheCape for writing the content of this page*

## How to Read Sequence Files

When reading through a .seq file using the pointers in the [tables below](#flag-tables) we can find the attack moves of particular characters. One such example is Naruto’s 5B.

Naruto 5B (located at A0 (1DA84) in his 0000.seq)

![Naruto 5B Example](/gnt4/images/functions/naruto5b.png?raw=true "Naruto 5B Example")

It is located at A0 (1DA84) and 6B begins at A1 (1DD4C), meaning that 5B takes place entirely between those two values. Since Naruto has a transformation, the move informs us at the beginning that his transformation (ZTK) has his 5B located at 01DBEC. This is seen at 010 of the picture with a GoTo/Pointer (01 34 00 00) at 010 and the location it is telling you to go to at 014. In this picture, that location is translated to: 168. Naruto’s 5B, after telling the game where to travel for ZTK, begins at 018. This is where we start to discuss the different types of flags on the move and how it makes them known. The move will state a type of flags (AF, KF, K2F, etc) at the beginning of the move, and if not given a modifier later, will last the entire length of the move.

All versions of flags are additive, and therefore can have any, all, or none of the flags in that realm. First at 018 is the AF flags, seen by 24 1A 00 00 as the prefix. The following 8 digits are the type of flags for that move, being 80 00 00 01, which is 80 00 00 00 as Attack and 00 00 00 01 as Stand. There is a list of what these flags mean at the bottom of this document. If a move has the “attack” portion listed, the character much remain in the animation until it ends, removing attack ends the animation early.

Secondly, at 020 we have 24 1A 12 00 which is the KF flags. These are your main attack flags as listed in the list below. Naruto 5B has the simple 00 00 03 08 which translates to:

| Hex         |  Flag          |
|-------------|----------------|
| 00 00 02 00 |  Punch         |
| 00 00 01 00 |  High          |
| 00 00 00 08 |  Weak Strength |

`24 1A 48 00` is K2F, which are special flags and generally not used for most moves.

`24 1A 09 00` is NF flags, which are generally seen as character state flags. This is where you find invulnerability, lighting, etc.

* 040 we have 04 02 02 3F which notates animations. 00 00 00 90 is Naruto’s first jab. Changing the animation ID changes which animation plays during the duration of the move, but does not change any of the other properties.
* 070 is 21 07 00 26 which is the frames the hitbox is active, listed in hex. Naruto’s 5B is 00 0E 00 11, which means that the hitbox first appears on frame 14 (0E) and disappears on 17 (11). This means that it has an active hitbox from 14 – 16.
* 078 begins to list 21 04 00 26 which are the hitbox locations and sizes. Hitboxes are always in a circle, but are dictated by the bone and the size of the hitbox. Following the prefix is always 00 BB 00 SS 00 00 00 00 where BB is the bone ID and SS is the size. The size, in some instances can take up more of the bits than just the two. For example: 00 10 01 00 would be bone 10 and size 1 00 (hex of course).
* 090 is 21 05 00 26 states the POW, DMG, and GRD of a move, in that order. POW is how much damage the move does to the lifebar. DMG, when combined with the strength of the move in the KF flags, is determined for how long a move stuns when it doesn’t do anything special in KF. GRD is how much damage the move does to an opponent’s guard. These numbers are generally the same across the board, but generally have more DMG for first jabs and certain move’s like Haku’s 2X stomp. GRD is slightly increased for characters like Tsunade as well.
* 0AC lists 21 06 00 26 XX XX YY YY where this lists the ANG, being the launching power of the move, or the lift if the opponent is airborne, and the DIR, being the direction the move hits. Moves like Sasuke 6B have a high enough DIR that they turn around back facing opponents on hit. When finding DIR, the number determines the direction the opponent is hit as well. To find the opposite number, subtract the value given (ex: E0 00) from 10000 in a hex calculator. 10000 – E000 = 2000
* 0B4 lists the first example of a Synchronous Timer. 20 11 26 3F is the prefix, 20 12 00 26 is the suffix. 00 00 00 0A tells us that the timer lasts 10 frames. This means that anything after this timer takes place after frame 10, the synchronous timers continue to give more information throughout the move. This is generally where adjustments to NF and AF flags will happen throughout a move.

In moves like Naruto’s 5A for example will show 47 00 00 26: Calls a projectile’s info. In the below example 00 00 75 00 is a pointer.

Ex: 47 00 00 26 00 00 00 05 00 00 00 02 00 00 75 00

This means at 75 00 in the 0000.seq file is where we start to see the information on Naruto’s 5A projectile, being the forward thrown Kunai. There are also stipulations in this move that show pointers for the 5A1C and 5A2C as well. Some examples of information with projectiles is as follows:

| Hex         |  Description                                |
|-------------|---------------------------------------------|
| 47 04 00 00 |  Projectile damage, stun, guard damage, etc |
| 47 05 00 00 |  # of times a projectile hits               |
| 48 04 00 00 |  Projectile KF Flags                        |
| 48 15 00 00 |  Projectile K2F flags                       |

A few other prefixes found so far:

| Hex                     |  Description                         |
|-------------------------|--------------------------------------|
| 24 14 01 0B             |  Horizontal mobility in a jump move. |
| 24 14 02 0B             |  Vertical mobility in a jump move.   |
| 2A 00 26 26             |  GFX                                 |
| 24 17 XX 00 XX XX XX XX |  SFX                                 |

`22 7F 20 00` is the requirements of meter to be used for an X move:

| Hex         |  Meter Requirement |
|-------------|--------------------|
| 00 00 3C 00 |  100%              |
| 00 00 2D 00 |  75%               |
| 00 00 1E 00 |  50%               |
| 00 00 0F 00 |  25%               |

`40 00 40 00` is the requirements of meter to be used for 3MC Z moves.

The first one is 5Z and the second one is 4Z. They are usually set at 25% and follow the same functions as the above.

`01 3C 00 00 00 00 XX XX` is the amount of meter used during a super attack.

Some examples, these values can be different. These translate to:

4388, 4364, 4340, 4316 in decimal. The values may change, but it is best to find the 100% value and then add 24 (decimal) to find each other value when you convert back to hex.

| Hex                     |  Meter Requirement |
|-------------------------|--------------------|
| 01 3C 00 00 00 00 11 24 |  25%               |
| 00 00 11 0C             |  50%               |
| 00 00 10 F4             |  75%               |
| 00 00 10 DC             |  100%              |

| Hex                     |  Description                                                                                                          |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 01 32 00 00             |  Pointer                                                                                                              |
| 01 33 00 00             |  Pointer                                                                                                              |
| 01 34 00 00             |  Pointer                                                                                                              |
| 24 15 0A 00 00 XX 00 00 |  Loop generally used on 4As to determine when the move removes the DEF frames and makes the character hittable again. |
| 24 17 03 00             |  Projectile charge                                                                                                    |
| 7F FF FF 28             |  Controls length of charge (01 highlighted above = length of charge & lowest time required to charge move)            |
| 7F FF FF 2A             |  Number of charges (01 = 1 charge, 02 = 2 charges, etc. Move defaults to original state after first charge)           |

Chouji 600 chakra per chip gained. This is an example, with the 0000.seq file location for Chouji, of the amount of Chakra he gains with each chip.  
`1C428: 3F 00 00 00 00 00 02 58`

A. Hinata chakra drain per frame on 4A (-180). This shows, with the 0000.seq location for A. Hinata, the amount of Chakra drained per frame doing her 4A. There is a loop that takes place before this, and then kicks off the draining from there.  
`1A0D4: 3F 00 00 00 FF FF FF 4C`

## Flag Tables

### Action ID References

| Hex |  Action ID |
|-----|------------|
| 030 |  00        |
| 070 |  10        |
| 0B0 |  20        |
| 0F0 |  30        |
| 130 |  40        |
| 170 |  50        |
| 1B0 |  60        |
| 1F0 |  70        |
| 230 |  80        |
| 270 |  90        |
| 2B0 |  A0        |
| 2F0 |  B0        |
| 330 |  C0        |
| 370 |  D0        |
| 3B0 |  E0        |
| 3F0 |  F0        |
| 430 |  100       |
| 470 |  110       |
| 4B0 |  120       |
| 4F0 |  130       |
| 530 |  140       |
| 570 |  150       |
| 5B0 |  160       |
| 5F0 |  170       |
| 630 |  180       |
| 670 |  190       |
| 6B0 |  1A0       |
| 6F0 |  1B0       |
| 730 |  1C0       |
| 770 |  1D0       |
| 7B0 |  1E0       |

### Action ID to Known Action States

| Hex |  Flag                   |  Description                                                                                  |
|-----|-------------------------|-----------------------------------------------------------------------------------------------|
| A0  |  5B                     |                                                                                               |
| A1  |  6B                     |                                                                                               |
| A2  |  4B                     |                                                                                               |
| A3  |  2B                     |                                                                                               |
| A5  |  RB                     |                                                                                               |
| B0  |  5A                     |                                                                                               |
| B1  |  6A                     |                                                                                               |
| B2  |  4A                     |                                                                                               |
| B3  |  2A                     |                                                                                               |
| B5  |  RA                     |                                                                                               |
| C0  |  RKnJ Ground            |                                                                                               |
| C1  |  RKnJ Air               |                                                                                               |
| C2  |  LKnJ                   |                                                                                               |
| C3  |  ZKnJ Incoming          |                                                                                               |
| C6  |  5Z outgoing            |                                                                                               |
| C7  |  4Z incoming            |                                                                                               |
| C8  |  5Z incoming            |                                                                                               |
| CB  |  ZKnJ outgoing          |                                                                                               |
| CF  |  4Z outgoing            |                                                                                               |
| E0  |  JB                     |                                                                                               |
| E1  |  JA                     |                                                                                               |
| E2  |  8B                     |                                                                                               |
| E3  |  8A                     |                                                                                               |
| 121 |  5X                     |  The X moves vary slightly in action ID number, but are always generally between 121 and 126. |
| 122 |  2X                     |                                                                                               |
| 130 |  Start of “combo moves” |                                                                                               |
| 190 |  Ground Throw           |                                                                                               |
| 191 |  Back Ground Throw      |                                                                                               |
| 192 |  Air Throw              |                                                                                               |
| 193 |  Activated X            |  Varies slightly between characters, but moves generally in this range.`                      |

### KF Attack Flags

`24 1A 12 00`

| Hex         |  Flag         |  Description                                                                    |
|-------------|---------------|---------------------------------------------------------------------------------|
| 00 00 00 00 |     none      |                                                                                 |
| 00 00 00 01 |     replay    |  No effect                                                                      |
| 00 00 00 02 |     BDrive    |  Changes lighting, no sub or tech roll, generally on Ougi moves                 |
| 00 00 00 04 |     Shot      |  ??                                                                             |
| 00 00 00 08 |     Pow_W     |  Weak hit. affects blockstun and hitstun                                        |
| 00 00 00 10 |     Pow_M     |  Medium hit                                                                     |
| 00 00 00 20 |     Pow_S     |  Strong hit                                                                     |
| 00 00 00 40 |     Low       |  Attack hits low, and can be evaded by AF float flag                            |
| 00 00 00 80 |     Middle    |  Attack hits middle                                                             |
| 00 00 01 00 |     High      |  Attack hits high, and can be evaded by AF sit flag                             |
| 00 00 02 00 |     Punch     |  Attack is classified as a punch                                                |
| 00 00 04 00 |     Kick      |  Attack is classified as a kick                                                 |
| 00 00 08 00 |     Throw     |  Attack is classified as a throw, no sub or tech roll                           |
| 00 00 10 00 |     Oiuchi    |  Hits later on OTG and during tech rolls (also called “Pursuit”)                |
| 00 00 20 00 |     Special   |  Builds no chakra, generally seen on Ougi moves                                 |
| 00 00 40 00 |     NoGuard   |  Unblockable                                                                    |
| 00 00 80 00 |     TDown     |  ??                                                                             |
| 00 01 00 00 |     SPTata    |  This is a large bounce. Ex: Naruto 4B                                          |
| 00 02 00 00 |     Break     |  This combines with other KF flags to affect the opponents guard.               |
| 00 04 00 00 |     Combo     |  Still not entirely understood                                                  |
| 00 08 00 00 |     Down      |  Spinout launcher. Launches higher than Uki flag                                |
| 00 10 00 00 |     Yoro      |  Stagger                                                                        |
| 00 20 00 00 |     Butt      |  Flying Screen knockback                                                        |
| 00 40 00 00 |     Uki       |  Launch on hit                                                                  |
| 00 80 00 00 |     Furi      |  Turns opponents around on hit. This is leftover from Bloody Roar and not used. |
| 01 00 00 00 |     Koro      |  Sweep: beats super armor, cannot be Y cancelled                                |
| 02 00 00 00 |     Reach_L   |  Unsure, but generally in attacks with a good deal of motion. Ex: Naruto 6B     |
| 04 00 00 00 |     Tata      |  Small Ground Bounce. Ex: Naruto 6B                                             |
| 08 00 00 00 |     NoSpeEp   |  ??                                                                             |
| 10 00 00 00 |     Beast     |  Slash hit effect and chip damage                                               |
| 20 00 00 00 |     Freeze    |  Opponent moves less during the attack, which allows moves to combo better      |
| 40 00 00 00 |     Cancel    |  Cancel the move when you press Y like an any frame feint (not used)            |
| 80 00 00 00 |     AtkCan    |  Super Cancel                                                                   |

### K2F Special Attack Flags

`24 1A 48 00`

| Hex         |  Flag          |  Description                                                   |
|-------------|----------------|----------------------------------------------------------------|
| 00 00 00 01 |     yoro2      |  Feet trapped. Ex: Kidomaru 5A1C                               |
| 00 00 00 02 |     hiki       |  Sink into the ground and pop out. Ex: Jiraya 2A               |
| 00 00 00 04 |     hiki2      |  Sink into the ground and fall from above. Ex: Shika 2X        |
| 00 00 00 08 |     mission    |  ??                                                            |
| 00 00 00 10 |     natemi     |  ??                                                            |
| 00 00 00 20 |     superarmor |  Gives the move super armor, must be turned off. Ex: Chouji 5A |
| 00 00 00 40 |     mato2      |  Trapped. Ex: Shino 2A                                         |
| 00 00 00 80 |     atkallcan  |  Can follow up with any other attack                           |
| 00 00 01 00 |     toji       |  ??                                                            |
| 00 00 02 00 |     hasa       |  Crumple. Ex: Jirobo stone clap crumple                        |
| 00 00 04 00 |     shave      |  For Kisame                                                    |
| 00 00 08 00 |     nemu       |  Sleep. Ex: Kabuto 2X                                          |
| 00 00 10 00 |     wing       |  ??. ex: Kabuto 2X                                             |
| 00 00 20 00 |     null1      |  Crumple. Ex: OTK 2X                                           |
| 00 00 40 00 |     null2      |  ??                                                            |

### NF State Flags

`24 1A 09 00`

| Hex         |  Flag           |  Description                                                 |
|-------------|-----------------|--------------------------------------------------------------|
| 00 00 00 01 |     kamae       |                                                              |
| 00 00 00 02 |     disp        |  Disappears, can even walk through opponent while invisible. |
| 00 00 00 04 |     tdmg        |  Used in conjuction with tdown for intangibility.            |
| 00 00 00 08 |     jump2       |  Flag that appears after doing your midair jump.             |
| 00 00 00 10 |     leverdir    |                                                              |
| 00 00 00 20 |     getup       |                                                              |
| 00 00 00 40 |     hiteft      |                                                              |
| 00 00 00 80 |     nfog        |                                                              |
| 00 00 01 00 |     takeon      |                                                              |
| 00 00 02 00 |     (blank)     |                                                              |
| 00 00 04 00 |     bdrivesleep |  Makes BDrive not active.                                    |
| 00 00 08 00 |     jump        |                                                              |
| 00 00 10 00 |     fall        |                                                              |
| 00 00 20 00 |     jspd        |                                                              |
| 00 00 40 00 |     shotdef     |  Expected this to block projectiles. It didn't.              |
| 00 00 80 00 |     move        |                                                              |
| 00 01 00 00 |     attack      |                                                              |
| 00 02 00 00 |     button      |                                                              |
| 00 04 00 00 |     combo       |                                                              |
| 00 08 00 00 |     disp_n      |  Disappears. Ends at the end of the action..?                |
| 00 10 00 00 |     kabehit     |                                                              |
| 00 20 00 00 |     bodytouch   |  Used for some throw attacks like Kisame. Disables sub.      |
| 00 40 00 00 |     aguard      |                                                              |
| 00 80 00 00 |     damage      |                                                              |
| 01 00 00 00 |     guard       |                                                              |
| 02 00 00 00 |     autodir     |  Determines if something has any tracking on it..?           |
| 04 00 00 00 |     eneauto     |                                                              |
| 08 00 00 00 |     njpturn     |                                                              |
| 10 00 00 00 |     ringout     |                                                              |
| 20 00 00 00 |     kabe        |                                                              |
| 40 00 00 00 |     tdown       |                                                              |
| 80 00 00 00 |     lever       |                                                              |

### AF Action State Flags

`24 1A 00 00`

| Hex         |  Flag       |  Description                                                                    |
|-------------|-------------|---------------------------------------------------------------------------------|
| 00 00 00 01 |     stand   |                                                                                 |
| 00 00 00 02 |     forward |                                                                                 |
| 00 00 00 04 |     back    |                                                                                 |
| 00 00 00 08 |     dash    |                                                                                 |
| 00 00 00 10 |     sit     |  Immune to high attacks.                                                        |
| 00 00 00 20 |     fuse    |                                                                                 |
| 00 00 00 40 |     ukemi   |                                                                                 |
| 00 00 00 80 |     kiri    |                                                                                 |
| 00 00 01 00 |     spmdmg  |                                                                                 |
| 00 00 02 00 |     slant   |                                                                                 |
| 00 00 04 00 |     quick   |                                                                                 |
| 00 00 08 00 |     float   |                                                                                 |
| 00 00 10 00 |     jump    |                                                                                 |
| 00 00 20 00 |     fall    |                                                                                 |
| 00 00 40 00 |     small   |                                                                                 |
| 00 00 80 00 |     damage  |                                                                                 |
| 00 01 00 00 |     downu   |                                                                                 |
| 00 02 00 00 |     downo   |                                                                                 |
| 00 04 00 00 |     getup   |                                                                                 |
| 00 08 00 00 |     turn    |                                                                                 |
| 00 10 00 00 |     tdown   |                                                                                 |
| 00 20 00 00 |     cantact |                                                                                 |
| 00 40 00 00 |     sdef    |  Side defense.                                                                  |
| 00 80 00 00 |     bdef    |  Back defense.                                                                  |
| 01 00 00 00 |     beast   |                                                                                 |
| 02 00 00 00 |     uki     |  Note: if this is added on an attacking move, that move can no longer Y cancel. |
| 04 00 00 00 |     butt    |                                                                                 |
| 08 00 00 00 |     ndown   |                                                                                 |
| 10 00 00 00 |     def     |  Defense from the front. Like 4B guard.                                         |
| 20 00 00 00 |     tfail   |  Missed throw                                                                   |
| 40 00 00 00 |     throw   |                                                                                 |
| 80 00 00 00 |     attack  |                                                                                 |
