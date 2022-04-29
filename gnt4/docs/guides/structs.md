# Structs

## Character Struct

Holds values related to a player character in battle. Named `chr_p` in the decompilation. They appear to have a size of `0xA08` bytes.

### Where to Find

The absolute positions of these structs can be found at the locations listed below. Additional locations can be found in `chr_init_dummy_team`, `chr_init_player`, `chr_init_static`, or `chr_init_team` after the call to `TRK_memset`.

- Player 1: `80226358`
- Player 2: `80226614`
- Player 3: `802268D0`
- Player 4: `80226B8C`
- CPU 1: `802283F8`
- CPU 2: `802283FC`
  - This also serves as the address for P2 in training mode
- CPU 3: `80228400`
- CPU 4: `80228404`

- Partner Character 1: `80228424`
- Partner Character 2: `80228420`
- Partner Character 3: `8022841C`
- Partner Character 4: `80228418`
- Partner Character 5: `80228414`
- Partner Character 6: `80228410`
  - i.e. Naruto and Itachi clones, Tayuya doki demon, Kankuro's puppet, and Kiba's dog. Anything non-playable character with a char struct.
    You can have up to 6 by doing a 3v3 battle where each character has a Partner Character. The order doesn't correlate to the player number,
    but rather is added as Partner Characters are needed. In a 1v1 match where P2 has a Partner Character, their Partner Character will be
    Partner Character 1.

### Values

#### 0x00: **Flags**

- 00000001: If set to 0, the character is removed. Probably used to remove clones and such.
- 00000008: Invincibility; all damage becomes 0. Used in `damage_handler()`.
- 01000000: If this char is a Partner Character. Used for opcodes like `241A3C00`.

#### 0x04: **Player ID**

The "controller" of the player, e.g. 0x0 through 0x3.

#### 0x10: **CPU Flags**

  - 0 if a player, other values if non-player controlled.

#### 0x14: **Player ID**

The "controller" of the player, e.g. 0x0 through 0x3.

#### 0x18: **Player ID**

The "controller" of the player, e.g. 0x0 through 0x3.

#### 0x1c: **Character ID**

  - See [INTERNAL_CHAR_ORDER](https://github.com/NicholasMoser/GNTool/blob/3.7/src/main/java/com/github/nicholasmoser/gnt4/GNT4Characters.java#L105)

#### 0x30: **Health Multipler**

A multipler for calculating health. For example, Naruto has 0xDC total health and a health multiplier of 0x64. After some calculations around instruction 0x8003f674,
this results in a total health of 0xDC. But, when using the character modifier flag of "Health Boost Lv2", the health multiplier will instead be 0xC8. This will
result in a total health of 0x1B8.

#### 0x38: **Own SEQ struct**

  - Contains information about the SEQ, starting offset found at offset 0x5C from the address stored in offset 0x1C

#### 0x3C: **Opponent SEQ struct**

  - Contains information about the SEQ, starting offset found at offset 0x5C from the address stored in offset 0x1C

#### 0x40: **Opponent chr_p**

Seems to be an opponent chr_p pointer. Referenced at dol address 0x800c02c8.

#### 0x44 **Some Seq Pointer**

Seems to be some pointer to an offset in an seq file, probably 0010.seq. Referenced at dol address 0x800c3ab8.
  
#### 0x110: **Movement Stuff**

Pointer to some movement related stuff.

#### 0x114: **Animation Stuff**

Pointer to animation related stuff. Offset 0x1c contains the current gnta data being executed by the chr.

#### 0x118: **Knockback Function Curve 1**

The first function curve value for the animation of being knocked back by a hit.

#### 0x11c: **Knockback Function Curve 2**

The second function curve value for the animation of being knocked back by a hit.

#### 0x120: **Knockback Speed**

How long the knockback animation takes as a float. Lower is slower. Derived from the above two function curve values.

#### 0x124: **MF Flags**

<details>
  <summary>MF Flag Values</summary>

  - `00000001` - GUARD
  - `00000002` - MUTEKI
  - `00000004` - BUTT
  - `00000008` - DEBUG
  - `00000010` - DEKA
  - `00000020` - TIBI
  - `00000040` - UDE
  - `00000080` - TYAKURA
  - `00000100` - TYAKURAREC
  - `00000200` - 09
  - `00000400` - 10
  - `00000800` - 11
  - `00001000` - 12
  - `00002000` - 13
  - `00004000` - 14
  - `00008000` - 15
  - `00010000` - 16
  - `00020000` - 17
  - `00040000` - 18
  - `00080000` - 19
  - `00100000` - 20
  - `00200000` - 21
  - `00400000` - 22
  - `00800000` - 23
  - `01000000` - 24
  - `02000000` - 25
  - `04000000` - 26
  - `08000000` - 27
  - `10000000` - 28
  - `20000000` - 29
  - `40000000` - 30
  - `80000000` - 31

</details>

#### 0x128: **AF Flags (Action State)**

<details>
  <summary>AF Flag Values</summary>

  - `00000001` - STAND
  - `00000002` - FORWARD
  - `00000004` - BACK
  - `00000008` - DASH
  - `00000010` - SIT
  - `00000020` - FUSE
  - `00000040` - UKEMI
  - `00000080` - KIRI
  - `00000100` - SPMDMG
  - `00000200` - SLANT
  - `00000400` - QUICK
  - `00000800` - FLOAT
  - `00001000` - JUMP
  - `00002000` - FALL
  - `00004000` - SMALL
  - `00008000` - DAMAGE
  - `00010000` - DOWNU
  - `00020000` - DOWNO
  - `00040000` - GETUP
  - `00080000` - TURN
  - `00100000` - TDOWN: Cannot be thrown.
  - `00200000` - CANTACT
  - `00400000` - SDEF: Special defense
  - `00800000` - BDEF: Seems to appear when hit by a move with beast
  - `01000000` - BEAST
  - `02000000` - UKI
  - `04000000` - BUTT
  - `08000000` - NDOWN
  - `10000000` - DEF: 4B guard
  - `20000000` - TFAIL: Missed throw
  - `40000000` - THROW: When placed on an attack, turns off follow ups
  - `80000000` - ATTACK: Used in `counter_hit_check()`
  
</details>

#### 0x12c: **PF Flags**

<details>
  <summary>PF Flag Values</summary>

  - `00000001` - DEFOK
  - `00000002` - BDEFOK
  - `00000004` - BGUARD
  - `00000008` - HIT
  - `00000010` - REVERSAL
  - `00000020` - GHIT
  - `00000040` - COMBO
  - `00000080` - FLOAT
  - `00000100` - FALL
  - `00000200` - ENEDMG
  - `00000400` - DIRNOGRD
  - `00000800` - ENEDWN
  - `00001000` - ENEATK
  - `00002000` - BDEF
  - `00004000` - THROWOK
  - `00008000` - BTNOMOVE
  - `00010000` - NECKTURN
  - `00020000` - ABSTURN
  - `00040000` - AIR
  - `00080000` - RINGOUT
  - `00100000` - TURN
  - `00200000` - ZOMBIE
  - `00400000` - BACK
  - `00800000` - BODY: Colliding with a player, likely used to stop you from moving.
  - `01000000` - M_KABE: Colliding with a wall, likely used to stop you from moving.
  - `02000000` - GUARD
  - `04000000` - DAMAGE: Makes your face in the HUD shake and the background of it to go red
  - `08000000` - ABSTURNR
  - `10000000` - NORMAL
  - `20000000` - DMG
  - `40000000` - DEF
  - `80000000` - OUT

Note: 0x00810000 is invincibility; all damage becomes 0. Used in `damage_handler()`.

</details>

#### 0x130: **NF Flags**

<details>
  <summary>NF Flag Values</summary>

  - `00000001` - KAMAE
  - `00000002` - DISP: Disappears. Can even walk through opponent while invisible.
  - `00000004` - TDMG
  - `00000008` - JUMP2: Double jump.
  - `00000010` - LEVERDIR
  - `00000020` - GETUP
  - `00000040` - HITEFT
  - `00000080` - NFOG
  - `00000100` - TAKEON
  - `00000200` - FOG
  - `00000400` - BDRIVESLEEP
  - `00000800` - JUMP
  - `00001000` - FALL
  - `00002000` - JSPD
  - `00004000` - SHOTDEF: Expected this to block projectiles. It didn't.
  - `00008000` - MOVE
  - `00010000` - ATTACK
  - `00020000` - BUTTON
  - `00040000` - COMBO
  - `00080000` - DISP_N
  - `00100000` - KABEHIT
  - `00200000` - BODYTOUCH
  - `00400000` - AGUARD
  - `00800000` - DAMAGE
  - `01000000` - GUARD
  - `02000000` - AUTODIR: Determines if something has any tracking on it..?
  - `04000000` - ENEAUTO
  - `08000000` - NJPTURN
  - `10000000` - RINGOUT
  - `20000000` - KABE
  - `40000000` - TDOWN
  - `80000000` - LEVER

</details>

#### 0x134: **N2F Flags**

<details>
  <summary>N2F Flag Values</summary>

  - `00000001` - UKEMI
  - `00000002` - KAWARIMI
  - `00000004` - NAGENUKE: Turn on throw escape in BR.
  - `00000008` - PUSH
  - `00000010` - DEFEFT
  - `00000020` - HITSHOCK
  - `00000040` - DEFSHOCK
  - `00000080` - GAGE
  - `00000100` - TYAKURA: Appears during supers that drain, stays on for a while after Oro super.
  - `00000200` - CAMERAOFF: Shifts the camera.
  - `00000400` - CUTOFF: Seen when hit by Tayuya 5X. This Flag turns off the music.
  - `00000800` - KABEHITSP
  - `00001000` - NULL
  - `00002000` - NULL
  - `00004000` - NULL
  - `00008000` - NULL
  - `00010000` - NULL
  - `00020000` - NULL
  - `00040000` - NULL
  - `00080000` - NULL
  - `00100000` - NULL
  - `00200000` - NULL
  - `00400000` - NULL
  - `00800000` - NULL
  - `01000000` - NULL
  - `02000000` - NULL
  - `04000000` - NULL
  - `08000000` - NULL
  - `10000000` - NULL
  - `20000000` - NULL
  - `40000000` - NULL
  - `80000000` - NULL

</details>

#### 0x138: **KF Flags**

<details>
  <summary>KF Flag Values</summary>

  - `00000001` - REPLAY: No effect
  - `00000002` - BDRIVE: Changes lighting, no sub or tech roll
  - `00000004` - SHOT: ??
  - `00000008` - POW_W: Weak hit. affects blockstun and hitstun
  - `00000010` - POW_M: Medium hit
  - `00000020` - POW_S: Strong hit
  - `00000040` - LOW: Attack hits low, and can be evaded by small flag
  - `00000080` - MIDDLE: Attack hits middle
  - `00000100` - HIGH: Atack hits high, and can be evaded by sit flag
  - `00000200` - PUNCH: Attack is classified as a punch
  - `00000400` - KICK: Atack is classified as a kick
  - `00000800` - THROW: Attack is classified as a throw
  - `00001000` - OIUCHI: Hits later on OTG
  - `00002000` - SPECIAL: Builds no chakra
  - `00004000` - NOGUARD: Unblockable
  - `00008000` - TDOWN: Makes a move grabbable while active
  - `00010000` - SPTATA: This is a large bounce (like Naruto 4B)
  - `00020000` - BREAK: Used in combination with other flags to move guard
  - `00040000` - COMBO: Seen in attacks that are only follow ups
  - `00080000` - DOWN: Spinout launcher. Launches higher than Uki flag
  - `00100000` - YORO: Stagger
  - `00200000` - BUTT: Flying Screen knockback
  - `00400000` - UKI: Launch on hit
  - `00800000` - FURI: Turns opponents around on hit
  - `01000000` - KORO: Sweep
  - `02000000` - REACH_L: ?? (Set on counter hit. Used in `counter_hit_check()`)
  - `04000000` - TATA: Small Ground Bounce
  - `08000000` - NOSPEEP: ??
  - `10000000` - BEAST: Slash hit effect and chip damage
  - `20000000` - FREEZE: Opponent does not move from the attack (Kimi multihit moves)
  - `40000000` - CANCEL: Cancel the move when you press Y (combine with RF for feint)
  - `80000000` - ATKCAN: Super Cancel

Note: 0x30000000 causes counter hits. Used in `counter_hit_check()`

</details>

#### 0x13c: **K2F Flags**

<details>
  <summary>K2F Flag Values</summary>

  - `00000001` - YORO2: Feet trapped (air and ground)
  - `00000002` - HIKI: Swamp hole sink (jiraiya 2A)
  - `00000004` - HIKI2: Fall into ground and appear above (shikamaru 2X)
  - `00000008` - MISSION: In mission mode this pops up when you achieve the objective and is on incoming Zsubs
  - `00000010` - NATEMI: Used on Ino 5X
  - `00000020` - SUPERARMOR: Gives the move super armor
  - `00000040` - MOTO2: Feet trapped 2 (ground only)
  - `00000080` - ATKALLCAN: Can follow up with any other attack
  - `00000100` - TOJI: Jirobo 2X drain
  - `00000200` - HASA: Jirobo stone clap crumple (air and ground grabbable crumple)
  - `00000400` - SHAVE: For Kisame
  - `00000800` - NEMU: Sleep
  - `00001000` - WING
  - `00002000` - NULL: (Grounded only crumple; OTK 2X)
  - `00004000` - NULL
  - `00008000` - NULL
  - `00010000` - NULL
  - `00020000` - NULL
  - `00040000` - NULL
  - `00080000` - NULL
  - `00100000` - NULL
  - `00200000` - NULL
  - `00400000` - NULL
  - `00800000` - NULL
  - `01000000` - NULL
  - `02000000` - NULL
  - `04000000` - NULL
  - `08000000` - NULL
  - `10000000` - NULL
  - `20000000` - NULL
  - `40000000` - NULL
  - `80000000` - NULL

</details>

#### 0x140: **DF Flags**

<details>
  <summary>DF Flag Values</summary>

  - `00000001` - F
  - `00000002` - B
  - `00000004` - R
  - `00000008` - L
  - `00000010` - W
  - `00000020` - M
  - `00000040` - S
  - `00000080` - SPECIAL
  - `00000100` - DOWN
  - `00000200` - YORO
  - `00000400` - BUTT
  - `00000800` - UKI
  - `00001000` - FURI
  - `00002000` - KORO
  - `00004000` - TATA
  - `00008000` - NODIS
  - `00010000` - A_LOW
  - `00020000` - A_MIDDLE
  - `00040000` - A_HIGH
  - `00080000` - BREAK
  - `00100000` - NBREAK: Guard break.
  - `00200000` - OIUCHI
  - `00400000` - TESCAPE: Turn on for throw breaks.
  - `00800000` - MEKURI
  - `01000000` - BDRIVE
  - `02000000` - COUNTER_N
  - `04000000` - SHOT
  - `08000000` - COUNTER
  - `10000000` - HITCNT
  - `20000000` - HITCNT2
  - `40000000` - OFFSET
  - `80000000` - SPMDMG

</details>

#### 0x144: **D2F Flags**

<details>
  <summary>D2F Flag Values</summary>

  - `00000001` - MATO
  - `00000002` - HIKI
  - `00000004` - HIKI2
  - `00000008` - MISSION
  - `00000010` - BDGUARD
  - `00000020` - MOTO2
  - `00000040` - TOJI
  - `00000080` - HASA
  - `00000100` - NEMU
  - `00000200` - NULL
  - `00000400` - NULL
  - `00000800` - NULL
  - `00001000` - NULL
  - `00002000` - NULL
  - `00004000` - NULL
  - `00008000` - NULL
  - `00010000` - NULL
  - `00020000` - NULL
  - `00040000` - NULL
  - `00080000` - NULL
  - `00100000` - NULL
  - `00200000` - NULL
  - `00400000` - NULL
  - `00800000` - NULL
  - `01000000` - NULL
  - `02000000` - NULL
  - `04000000` - NULL
  - `08000000` - NULL
  - `10000000` - NULL
  - `20000000` - NULL
  - `40000000` - NULL
  - `80000000` - NULL

</details>

#### 0x148: **EF Flags**

<details>
  <summary>EF Flag Values</summary>

  - `00000001` - KABE
  - `00000002` - KABEN
  - `00000004` - KABEC
  - `00000008` - PAUSE
  - `00000010` - COMNUKE
  - `00000020` - RESCAPE
  - `00000040` - HOKAN
  - `00000080` - WARPHIP
  - `00000100` - TDOWNFAIL: State of getting combo'd?
  - `00000200` - NULL
  - `00000400` - BKOUT
  - `00000800` - ATK
  - `00001000` - SPOSE
  - `00002000` - LEVERREV
  - `00004000` - ATKCAN
  - `00008000` - OFFBEAST: Screen flash.
  - `00010000` - HOPUP
  - `00020000` - WARP
  - `00040000` - FIX
  - `00080000` - TAKEON
  - `00100000` - RINGOUT
  - `00200000` - TFAIL
  - `00400000` - THROW
  - `00800000` - TDOWN
  - `01000000` - COMBO0
  - `02000000` - COMBO1
  - `04000000` - TESCAPE
  - `08000000` - BDRIVE
  - `10000000` - FLAG0
  - `20000000` - FLAG1
  - `40000000` - FLAG2
  - `80000000` - 31

</details>

#### 0x14c: **RF Flags**

<details>
  <summary>RF Flag Values</summary>

  - `00000001` - COLOR
  - `00000002` - TYAKURASUB: Meter drain
  - `00000004` - HAZIKI: Allows kunai deflect Neji 2X
  - `00000008` - HAZIKIR
  - `00000010` - ALLGUARD: Guards all sides when DEF is active
  - `00000020` - EFTREV: Removes GFX
  - `00000040` - TARGETDIRA
  - `00000080` - GCANCELCHK: Hyuuga cancel, must be on at the start of the move
  - `00000100` - GCANCELOK: Appears after you confirm the cancel, is set on the cancel frame
  - `00000200` - GCANCEL: Shows until a cancel can be done
  - `00000400` - GATTACK
  - `00000800` - NKAWARIMI: Applies confusion on damage (Used by Tsunade)
  - `00001000` - AUTOMOTION
  - `00002000` - EVENT00
  - `00004000` - SHADOWOFF: Makes character shadow disappear while on
  - `00008000` - NOBACK: Removes slide back while blocking
  - `00010000` - NSOUSAI
  - `00020000` - TAG2SP
  - `00040000` - TAG3SP
  - `00080000` - VANISH: On sakura 6A
  - `00100000` - INTRUDE
  - `00200000` - NOSTIFF
  - `00400000` - MOTIONREG
  - `00800000` - BDRIVEDEFDMG
  - `01000000` - ATTACKOK
  - `02000000` - DEFAULTTEXREV: On Oro 5X
  - `04000000` - PARDIR
  - `08000000` - ATKCHANGE
  - `10000000` - KAWARIMI
  - `20000000` - ACTCAN
  - `40000000` - 30: Affects the camera?
  - `80000000` - 31: Affects the camera?

</details>

#### 0x150: **CF Flags**

<details>
  <summary>CF Flag Values</summary>

  - `00000001` - DMGOFF
  - `00000002` - TYAKURASUB
  - `00000004` - DISPOFF: Turns off the display for the character model. Halts synchronous timers.
  - `00000008` - TAKEONOFF
  - `00000010` - CHGNOATTACK
  - `00000020` - CHGNODMG
  - `00000040` - ANMCHG
  - `00000080` - COPYPFHIT
  - `00000100` - CLR
  - `00000200` - TYAKURAADD
  - `00000400` - PARENTMOVE
  - `00000800` - PINCH
  - `00001000` - CAMERAON
  - `00002000` - COMBOONLY
  - `00004000` - TARGETPARENT
  - `00008000` - NORESULT
  - `00010000` - TARGETPARENT2
  - `00020000` - PARDMGOFFCOPYTHROW
  - `00040000` - 19
  - `00080000` - 20
  - `00100000` - 21
  - `00200000` - 22
  - `00400000` - 23
  - `00800000` - 24
  - `01000000` - 25
  - `02000000` - 26
  - `04000000` - 27
  - `08000000` - 28
  - `10000000` - 29
  - `20000000` - 30
  - `40000000` - 31
  - `80000000` - (empty): The name of this flag is blank.

</details>

#### 0x154: **Character Modifier Flag**

<details>
  <summary>Character Modifier Flag</summary>

All of these are available to be selected in GNT Clash of Ninja 2, but only a few are available in GNT4.
You can view the English names given to them by Eighting in CON2 in the item viewer menu.

  - `00000001` - Attack Boost Lv1
  - `00000002` - Attack Boost Lv2
  - `00000004` - Disable Chakra Gain
  - `00000008` - Auto-Recover Chakra
  - `00000010` - Special Jutsu Boost
  - `00000020` - Health Absorption
  - `00000040` - Reverse Directions
  - `00000080` - Health Boost Small
  - `00000100` - Health Boost Medium (This is the Lv1 boost in GNT4)
  - `00000200` - Health Boost Large (This is the Lv2 boost in GNT4)
  - `00000400` - Auto-Throw Escape
  - `00000800` - Auto-Ground Tech
  - `00001000` - Super Armor
  - `00002000` - Auto-Recover Health
  - `00004000` - Invincibility for 10 Seconds
  - `00008000` - Absolute Defense
  - `00010000` - Halve Chakra Consumption
  - `00020000` - Disable Ground Tech
  - `00040000` - Disable Substitution
  - `00080000` - Disable Sidestep
  - `00100000` - Disable B Button
  - `00200000` - Disable A Button
  - `00400000` - Disable X Button
  - `00800000` - Disable Y Button
  - `01000000` - Disable Throw Escape
  - `02000000` - Disable Chakra Use
  - `04000000` - Disable Jump
  - `08000000` - Disable Guard
  - `10000000` - Disable Projectiles
  - `20000000` - Health Drain
  - `40000000` - Halve Attack Power
  - `80000000` - Delete HP and Chakra Guard

</details>

#### 0x15c: **Active Hitbox Check**

  - FFFFFFFF when no hitbox is active
  - 00000000 when hitbox is active

#### 0x164: **Combo Count 1**

  - Normal tally.
  - Added to Combo Count 2 to get combo count

#### 0x166: **Combo Count 2**

  - Capture state tally, for attacks that add to combo counter inside of capture state, e.g. supers, or anko 4B(B) second hit
  - Added to Combo Count 1 to get combo count

#### 0x19c: **X Position**

#### 0x1a0: **Y Position**

#### 0x1a4: **Z Position**

#### 0x1cc: Movement Flags

  - Set to 0x1 if being pushed horizontally or vertically (fields 0x1d4 and 0x1dc). Sometimes set to 0x2 when doing other things like walking.

#### 0x1bc: **Facing Opponent**

  - A signed short representing the degree to which you are facing the opponent. 0 is directly facing the opponent, −32,767 is directly facing away from your opponent.

#### 0x1d4: **Horizontal Push Speed**

  - A float value representing a push or pull horizontally on the character. Normally 0. Positive pushes the character forward, negative pulls them backwards. Kinda looks like a [Raging Demon](https://streetfighter.fandom.com/wiki/Shun_Goku_Satsu).

#### 0x1d4: **Horizontal Push Acceleration**

  - A float value representing the amount to decrease Horizontal Push Speed (field 0x1d4) per frame. Positive increases it, negative decreases it.

#### 0x1dc: **Vertical Push Speed**

  - A float value representing how fast you are moving up or down. Normally 0. When jumping starts at 1.42, peaks at 0, and ends at -1.56. Positive is moving up, negative is moving down.

#### 0x1e0: **Gravitational Constant**

#### 0x1e8: **Horizontal Air Speed**

#### 0x1f4: **Knockback Velocity**

#### 0x1f8: **Knockback Acceleration**

#### 0x230: **chr_tbl**

  - Pointer to memory address for characters chr_tbl

#### 0x238: **Act Counter Difference**

  - The amount to add to the **Act Counter** every frame.

#### 0x23c: **Act ID**

  - Current Action ID

#### 0x240: **Act ID2**

  - Current Action ID again

#### 0x24c: **Something about jumping and attacking**

    - Start round at FFFFFFFF
    - Set to 1D when jumping
    - Set to E4 at start of dive kick
    - Set to FFFFFFFF at end of dive kick or start of air throw

#### 0x250: **Changes on start of actions that moves character**

    - Getting thrown
    - Doing any attack

#### 0x254: **Unknown**

    - Start round at FFFFFFFF
    - Set to 0 first jump

#### 0x258: **Act Counter**

  - Resets to 0 at the end of your last action. Can be displayed in the debug menu under the ACT mess, labeled on the right side as ACT.

#### 0x25c: **Current Recoverable Damage**

  - Current recoverable health. Counts up from 0.
  - REMAIN in debug mode (LIFE)

#### 0x260: **Current Damage**

  - Current health. Counts up from 0.
  - TOTAL in debug mode (LIFE)

#### 0x264: **Current REC**

  - REC in debug mode (LIFE)

#### 0x26c: **Health Frame Counter**

  - Used to count frames for damage/healing over time. e.g. Tsunade heal.

#### 0x27c: **Max Damage**

  - The total health of your character. You die when **Current Damage** >= **Max Damage**

#### 0x280: **New Damage**

  - This gets added to **Current Damage**. Can be negative, which results in healing.

#### 0x288: **Last Damage**

  - The **New Damage** of the previous attack.

#### 0x28c: **Current Chakra**

#### 0x290: **New Chakra**

  - Signed integer, this gets added to **Current Chakra**. Can be negative, which results in drain.

#### 0x294: **Current Block Guard**

#### 0x298: **Max Block Guard**

#### 0x29c: **GRD**

  - GRD value current attack

#### 0x2a0: **Confusion Flag**

  - The flag for which Tsunade confusion effect you are afflicted with. `0` is reverse directions. `1` is reverse buttons (A with B, Y with X).
  Set at dol address 0x8003bad0.

#### 0x2a4: **Confusion Timer**

  - The timer for how long you are affected by Tsunade's confusion effect. Initialized to 300 frames (5 seconds) at dol address 0x8003bad4.

#### 0x2a8: **Idle Counter 2**

  - Appears to be a duplicate of **Idle Counter**

#### 0x2ac: **Hitbox Removal Timer**

  - Count down 100 each frame, hitbox disappear when timer reach 0.

#### 0x2b0: **Hitbox Appearance Timer**

  - Count down 100 each frame, hitbox appear when timer reach 0.

#### 0x2b4: **Synchronous timer after hitbox**

  - FFFFFFFF in neutral
  - 00000000 at start of action
  - Count up 100 from 0 each frame after hitbox disappear

#### 0x2b8: **Attack Angle**

  - What angle the attacking character was turned away from the opponent when the attack connected

#### 0x2bc: **POW**

  - Current attack POW value

#### 0x2c0: **ANG**

  - Current attack ANG value

#### 0x2c4: **Attack Multiplier**

  - A multiplier that is applied to the damage you do. Defaults to 1. Choji chips can raise it up to a max of 1.5.

#### 0x2c8: **DMG**

  - Current attack DMG value

#### 0x2d0: **REV**

#### 0x2d4: **REV2**

#### 0x2d8: **Block Stun**

  - Shows how many frames blockstun last received attack gave

#### 0x2dc: **Stand up timer**

  - Timer idling on the ground before standing up

#### 0x2ec: **Inactionable timer**

  - No inputs possible before timer reach 0
  - Used at round start or after reset

#### 0x2f0: **Intangible timer**

  - Reset when moving
  - Set when standing up
  - Count down 100 each frame

#### 0x2f4: **Anti Super timer?**

  - Count down 100 each frame
  - If super connect when not 0, character freeze

#### 0x2f8: **Grab Break Counter**

  - A counter that while it is not zero, you can break a grab. Seems to always be set to 0x300 at instruction 0x800b5144. Every frame subtracts 0x100 at instruction 0x8001aaec.

#### 0x54c: **Active Throws**

  - Pointer to where in memory the available throws are defined

#### 0x7d8: **Start String Offset**

  - Where the offsets for all the characters strings start

#### 0x7e0: **Something with Strings**

  - 2 Bytes
  - Set upon controller input
  - POW is added to it
  - If early, can be overwritten at a later frame
  - Set to 0 if **PF FLAG** combo is not set and the value in 0x7f8 is < 0

#### 0x7e2: **String Next ATK ID**

  - 2 Bytes
  - Set upon controller input

#### 0x7e4: **Something with Strings**

  - 2 Bytes
  - Set to 0 if **PF FLAG** combo is not set and the value in 0x7f8 is < 0

#### 0x7e6: **Something with Strings**

  - 2 Bytes
  - Set sometimes in strings
  - Set to 0 if **PF FLAG** combo is not set and the value in 0x7f8 is < 0

#### 0x7ec: **Something with Strings**

  - 4 Bytes
  - Set sometimes in strings

#### 0x7f4: **Something with Strings**

  - 2 Bytes
  - Compared with 0x7f6

#### 0x7f6: **Something with Strings**
  
  - 2 Bytes
  - Seem to oscillate between 0 and 1

#### 0x7f8: **0x7f6 previous value**

  - 2 Bytes
  - Value in 0x7f6 backed up here before being manipulated

#### 0x854: **Transformation Flag**

  - 0 is Naruto, 2 is ZTK.
  - 0 is Sasuke, 2 is Sharingan Sasuke.
  - 0 is Kakashi, 2 is Sharingan Kakashi.
  - 0 is Lee, 2 is First Gate, 6 is Second Gate.
  - 0 is Gai, 2 is First Gate.
  - 0 is Sakon, 0x2002 is Ukon.
  - 0 is Tsunade, 2 is Tsunade Healing from 2X
  - 8 is unknown but used in some places like 0x8003e470

#### 0x894: **Air Fall Combo Counter**

The current combo count against this character, used to slowly increase gravity as the combo continues. Written to at 0x8003a884 and sometimes 0x8003bb04 in `damage_stuff`. Read from functions `calculate_air_fall_1` and `calculate_air_fall_2`.

#### 0x87c: **SF Flags**

<details>
  <summary>SF Flag Values</summary>

  - `00000001` - HIT
  - `00000002` - GHIT
  - `00000004` - DAMAGE
  - `00000008` - GUARD
  - `00000010` - DEFOK
  - `00000020` - CATCH
  - `00000040` - 06
  - `00000080` - 07
  - `00000100` - 08
  - `00000200` - 09
  - `00000400` - 10
  - `00000800` - 11
  - `00001000` - 12
  - `00002000` - 13
  - `00004000` - 14
  - `00008000` - 15
  - `00010000` - 16
  - `00020000` - 17
  - `00040000` - 18
  - `00080000` - 19
  - `00100000` - 20
  - `00200000` - 21
  - `00400000` - 22
  - `00800000` - 23
  - `01000000` - 24
  - `02000000` - 25
  - `04000000` - 26
  - `08000000` - 27
  - `10000000` - 28
  - `20000000` - 29
  - `40000000` - 30
  - `80000000` - 31

</details>

#### 0x8C8: **Synchronous timer**

Set by opcode 2011263F.

#### 0x954 **Throw Target**

Pointer to the character struct of the target of a throw.

#### 0x960 **Opponent Target**

Pointer to potentially the target of an attack. Set at dol address 0x8003ba78

#### 0x974: **Opponent Character Struct**

Pointer to potentially one or more enemy character structs.
