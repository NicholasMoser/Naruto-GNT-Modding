# Character Struct

Holds values related to a player character in battle. Named `chr_p` in the decompilation. They appear to have a size of `0xA08` bytes (per `memset` at address 0x800560d4)

## Where to Find

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

The addresses `80228408` and `8022840c` also appear to be used for 3v3 Training Mode.

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

## Values

### 0x00: **Flags**

- 00000001: If set to 0, the character is removed. Probably used to remove clones and such.
- 00000008: Invincibility; all damage becomes 0. Used in `damage_handler()`.
- 01000000: If this char is a Partner Character. Used for opcodes like `241A3C00`.
- 80000000: Used for the Naruto clone when it is active.

### 0x04: **Player ID**

The "controller" of the player, e.g. 0x0 through 0x3.

### 0x10: **CPU Flag**

The flag for what action the CPU is doing. Flags 0x10 - 0x1B are selectable in the training menu.
<details>
<summary>CPU Flag</summary>
  
  - 0x00: Player controlled, no CPU action.
  - 0x01: Dash forward continuously.
  - 0x02: Simple AI, just does 5B and 5A. Maybe Oboro AI?
  - 0x03: Stand. Will turn around if you get behind them (character head tracks the player).
  - 0x04: Jump, no air block or throw tech. Will turn around if you get behind them.
  - 0x05: Jump, air block but no throw tech. Will turn around if you get behind them.
  - 0x06: Unknown, looks like Stand but might do other things.
  - 0x07: Jump, air block and throw tech. Will turn around if you get behind them.
  - 0x08: Continuously attack with 5BB.
  - 0x09: Unknown, looks like Stand but might do other things.
  - 0x0A: Unknown, looks like Stand but might do other things.
  - 0x0B: Unknown, looks like Stand but might do other things.
  - 0x0C: Unknown, looks like Stand but might do other things.
  - 0x0D: Unknown, looks like Stand but might do other things.
  - 0x0E: Unknown, looks like Stand but might do other things.
  - 0x10: Unknown CPU level
  - 0x11: Stand
  - 0x12: Jump
  - 0x13: 2P Control
  - 0x14: Approach and Throw
  - 0x15: Substitution Jutsu
  - 0x16: Tech Roll Recovery
  - 0x17: Quick Stun Recovery
  - 0x18: COM Difficulty Lv1
  - 0x19: COM Difficulty Lv2
  - 0x1A: COM Difficulty Lv3
  - 0x1B: COM Difficulty Lv4
  - 0x1C: Unknown, looks like Stand but might do other things.
  - 0x1D: Unknown, looks like Stand but might do other things.
  - 0x1E: Unknown, looks like Stand but might do other things.
  - 0x1F: Unknown, looks like Stand but might do other things.
  - 0x20: Unknown, looks like Stand but might do other things.
  - 0x21: Character will mash 5B until the combo ends and then resets the CPU Flag to 0.
  - 0x22: Nothing
  - 0x23: Nothing
  - 0x24: Nothing
  - 0x25: Nothing
  - 0x26: Nothing
  - 0x27: Nothing
  - 0x28: Nothing
  - 0x29: Nothing
  - 0x2A: Nothing
  - 0x2B: Nothing
  - 0x2C: Nothing
  - 0x2D: Nothing
  - 0x2E: Nothing
  - 0x2F: Nothing
  - 0x30: Unknown, looks like Stand but might do other things.
</details>

### 0x14: **Player ID 2**

The "controller" of the player, e.g. 0x0 through 0x3.

### 0x18: **Player ID 3**

The "controller" of the player, e.g. 0x0 through 0x3.

### 0x1c: **Character ID**

  - See [INTERNAL_CHAR_ORDER](https://github.com/NicholasMoser/GNTool/blob/3.7/src/main/java/com/github/nicholasmoser/gnt4/GNT4Characters.java#L105)

### 0x20: **Costume ID**

  - The costume selected for the character.
    - 1st (A): 0
    - 2nd (Y): 1
    - 3rd (X): 2
    - 4th (Z): 3

### 0x24: **Transform Model Flag**

A flag to set if the character model is to be transformed in some way. One example is to set it to 1 when Choji enlarges during certain attacks. It is also apparently used by Akamaru for something. Used by opcode `2108`.

### 0x30: **Health Multipler**

A multipler for calculating health. For example, Naruto has 0xDC total health and a health multiplier of 0x64. After some calculations around instruction 0x8003f674,
this results in a total health of 0xDC. But, when using the character modifier flag of "Health Boost Lv2", the health multiplier will instead be 0xC8. This will
result in a total health of 0x1B8.

### 0x38: **Own SEQ struct**

  - Contains information about the SEQ, starting offset found at offset 0x5C from the address stored in offset 0x1C

### 0x3C: **Opponent SEQ struct**

  - Contains information about the SEQ, starting offset found at offset 0x5C from the address stored in offset 0x1C

### 0x40: **Opponent chr_p**

Seems to be an opponent chr_p pointer. Referenced at dol address 0x800c02c8.

### 0x44 **Some Seq Pointer**

Seems to be some pointer to an offset in an seq file, probably 0010.seq. Referenced at dol address 0x800c3ab8.

### 0x48

[Set here](https://nicholasmoser.github.io/iru_0000.html#15390)
  
### 0x110: **Movement Stuff**

Pointer to some movement related stuff.

### 0x114: **Animation Stuff**

Pointer to animation related stuff. Offset 0x1c contains the current gnta data being executed by the chr.

### 0x118: **Knockback Function Curve 1**

The first function curve value for the animation of being knocked back by a hit.

### 0x11c: **Knockback Function Curve 2**

The second function curve value for the animation of being knocked back by a hit.

### 0x120: **Knockback Speed**

How long the knockback animation takes as a float. Lower is slower. Derived from the above two function curve values.

### 0x124: **MF Flags**

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

### 0x128: **AF Flags (Action State)**

Action state flags.

<details>
  <summary>AF Flag Values</summary>

  - `00000001` - STAND: This action is in the default stance on this frame (No crush)
  - `00000002` - FORWARD
  - `00000004` - BACK
  - `00000008` - DASH
  - `00000010` - SIT: This action is invulnerable to "High" attacks on this frame (High Crush)
  - `00000020` - FUSE: This action is invulnerable to "High" and "Middle" attacks on this frame (Middle Crush)
  - `00000040` - UKEMI
  - `00000080` - KIRI
  - `00000100` - SPMDMG
  - `00000200` - SLANT
  - `00000400` - QUICK
  - `00000800` - FLOAT: This action is considered to not be grounded (not to be confused with AIR flag)
  - `00001000` - JUMP
  - `00002000` - FALL
  - `00004000` - SMALL: This action is invulnerable to "Low" attacks on this frame (Low Crush)
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
  - `40000000` - THROW: This attack is considered a throw (substitution is not possible, turns off follow ups)
  - `80000000` - ATTACK: Used in `counter_hit_check()`
  
</details>

### 0x12c: **PF Flags**

Animation related flags.

<details>
  <summary>PF Flag Values</summary>

  - `00000001` - DEFOK: The character's attack will have Auto Guard (in conjunction with DEF flag)
  - `00000002` - BDEFOK
  - `00000004` - BGUARD
  - `00000008` - HIT: A clean hit on the opponent
  - `00000010` - REVERSAL
  - `00000020` - GHIT: When you hit the opponent's guard
  - `00000040` - COMBO
  - `00000080` - FLOAT: In air, similar to AIR. Tayuya 8B sets AIR but not FLOAT, so there is a difference.
  - `00000100` - FALL
  - `00000200` - ENEDMG
  - `00000400` - DIRNOGRD
  - `00000800` - ENEDWN
  - `00001000` - ENEATK
  - `00002000` - BDEF
  - `00004000` - THROWOK: The character is in a throwable state
  - `00008000` - BTNOMOVE
  - `00010000` - NECKTURN
  - `00020000` - ABSTURN
  - `00040000` - AIR: This action is considered airborne on this frame (getting hit will result in a juggle).
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

### 0x130: **NF Flags**

Direction/generic flags.

<details>
  <summary>NF Flag Values</summary>

  - `00000001` - KAMAE
  - `00000002` - DISP: Disappears. Can even walk through opponent while invisible.
  - `00000004` - TDMG: The character is invincible in their current state
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
  - `02000000` - AUTODIR: The "tracking" flag; during this move, the character will automatically pivot towards the opponent in an attempt to align their attack with them if they are off-axis.
  - `04000000` - ENEAUTO
  - `08000000` - NJPTURN
  - `10000000` - RINGOUT
  - `20000000` - KABE
  - `40000000` - TDOWN: If not present, the attack will not allow Throws to be used until the flag dissapears (regardless of distance with the opponent)
  - `80000000` - LEVER

</details>

### 0x134: **N2F Flags**

More direction/generic flags.

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

### 0x138: **KF Flags**

Attack flags.

<details>
  <summary>KF Flag Values</summary>

  - `00000001` - REPLAY: No effect
  - `00000002` - BDRIVE: This attack is considered a super (substitution is not possible)
  - `00000004` - SHOT: This attack is considered a projectile (almost always seen combined with REACH_L flag)
  - `00000008` - POW_W: This attack is considered to be "weak" (affects blockstun and hitstun)
  - `00000010` - POW_M: This attack is considered to be "medium" (affects blockstun and hitstun)
  - `00000020` - POW_S: This attack is considered to be "strong" (affects blockstun and hitstun)
  - `00000040` - LOW: This attack hits Low (will not hit moves that currently have SMALL flag active)
  - `00000080` - MIDDLE: This attack hits Mid (will still hit moves that currently have either SIT and SMALL flag active, but not FUSE)
  - `00000100` - HIGH: This attack hits High (will not hit moves that currently have SIT flag active)
  - `00000200` - PUNCH: This attack is considered a punch (enables Y-Cancels for the attack)
  - `00000400` - KICK: This attack is considered a kick (enables Y-Cancels for the attack)
  - `00000800` - THROW: Attack is classified as a throw
  - `00001000` - OIUCHI: This attack can bypass a tech roll's invincibility (unused)
  - `00002000` - SPECIAL: This attack will not build any meter (most commonly seen on supers)
  - `00004000` - NOGUARD: This attack is unblockable
  - `00008000` - TDOWN: Makes a move grabbable while active
  - `00010000` - SPTATA: This attack causes a large groundbounce on hit (cannot be Y-Canceled)
  - `00020000` - BREAK: This attack pushes the opponent on block (the direction of the push depends on the attack's inherent angle value)
  - `00040000` - COMBO: This action is considered a part of a string
  - `00080000` - DOWN: This attack causes a spinning launch on hit (launches higher than Uki flag)
  - `00100000` - YORO: This attack staggers the opponent on hit
  - `00200000` - BUTT: This attack causes heavy knockback (when combined with BREAK flag, triggers flying screen)
  - `00400000` - UKI: This attack launches the opponent on hit
  - `00800000` - FURI: On hit, this attack causes opponents to forcefully turn their back towards the attacker (unused)
  - `01000000` - KORO: This attack trips the opponent on hit (cannot be Y-Canceled)
  - `02000000` - REACH_L: The projectile's hitboxes will refresh as it travels
  - `04000000` - TATA: This attack causes a small groundbounce on hit (cannot be Y-Canceled)
  - `08000000` - NOSPEEP: ??
  - `10000000` - BEAST: This attack deals chip damage
  - `20000000` - FREEZE: This attack does not have pushback on hit or block (Kimi multihit moves)
  - `40000000` - CANCEL: Cancel the move when you press Y (combine with RF for feint)
  - `80000000` - ATKCAN: This attack can be canceled into supers

Note: 0x30000000 causes counter hits. Used in `counter_hit_check()`

</details>

### 0x13c: **K2F Flags**

More attack flags.

<details>
  <summary>K2F Flag Values</summary>

  - `00000001` - YORO2: Body trapped (Kido 5A)
  - `00000002` - HIKI: Swamp hole sink (jiraiya 2A)
  - `00000004` - HIKI2: Fall into ground and appear above (shikamaru 2X)
  - `00000008` - MISSION: In mission mode this pops up when you achieve the objective and is on incoming Zsubs
  - `00000010` - NATEMI: Used on Ino 5X
  - `00000020` - SUPERARMOR: Gives the move super armor
  - `00000040` - MOTO2: Feet trapped (Kido 2A)
  - `00000080` - ATKALLCAN: Can follow up with any other attack
  - `00000100` - TOJI: Jirobo 2X drain
  - `00000200` - HASA: Jirobo stone clap crumple (air and ground grabbable crumple)
  - `00000400` - SHAVE: For Kisame
  - `00000800` - NEMU: Sleep (Kabuto 2X)
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

### 0x140: **DF Flags**

<details>
  <summary>DF Flag Values</summary>

  - `00000001` - F: Front
  - `00000002` - B: Back
  - `00000004` - R: Right
  - `00000008` - L: Left
  - `00000010` - W
  - `00000020` - M
  - `00000040` - S
  - `00000080` - SPECIAL
  - `00000100` - DOWN
  - `00000200` - YORO: Stagger (Naruto first charge of 5A or OTK 5AA)
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

### 0x144: **D2F Flags**

Eighting ran out of DF flags, and so added the rest to D2F flags.

<details>
  <summary>D2F Flag Values</summary>

  - `00000001` - MATO: Body trapped (Kido 5A)
  - `00000002` - HIKI: Suck into ground (Jiraiya 2A)
  - `00000004` - HIKI2: Drop into ground (Shikamaru 2X)
  - `00000008` - MISSION
  - `00000010` - BDGUARD
  - `00000020` - MOTO2: Feet trapped (Kido 2A)
  - `00000040` - TOJI
  - `00000080` - HASA
  - `00000100` - NEMU: Sleep (Kabuto 2X)
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

### 0x148: **EF Flags**

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
  - `00008000` - OFFBEAST: Screen flash
  - `00010000` - HOPUP: Screen blur
  - `00020000` - WARP: Warp this character in front of the opponent
  - `00040000` - FIX: Pushes this character in front of the opponent
  - `00080000` - TAKEON
  - `00100000` - RINGOUT
  - `00200000` - TFAIL: Whiffing a throw, set at 0x800637f4 in `throw_logic()`
  - `00400000` - THROW
  - `00800000` - TDOWN
  - `01000000` - COMBO0
  - `02000000` - COMBO1
  - `04000000` - TESCAPE: Set to the attacker and defender when a throw break occurs
  - `08000000` - BDRIVE
  - `10000000` - FLAG0
  - `20000000` - FLAG1
  - `40000000` - FLAG2: SCON4 hijacks this value for a poison effect
  - `80000000` - 31

</details>

### 0x14c: **RF Flags**

<details>
  <summary>RF Flag Values</summary>

  - `00000001` - COLOR
  - `00000002` - TYAKURASUB: This attack subtracts chakra from the opponent
  - `00000004` - HAZIKI: This attack can repel projectiles (Neji 2X)
  - `00000008` - HAZIKIR
  - `00000010` - ALLGUARD: Guards all sides when DEF is active
  - `00000020` - EFTREV: Removes GFX
  - `00000040` - TARGETDIRA
  - `00000080` - GCANCELCHK: This move is Hyuuga-cancellable and will be checking for a Hyuuga-cancel input before active frames.
  - `00000100` - GCANCELOK: A Hyuuga-cancel animation can initiate as soon as the frame after this flag appears.
  - `00000200` - GCANCEL: The game puts this flag down if a Hyuuga-cancel has been input while GCANCELCHK is active. Initiates a Hyuuga-cancel when paired with flag GCANCELOK.
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
  - `10000000` - KAWARIMI: This character is currently performing a "Kawarimi-no-Jutsu"
  - `20000000` - ACTCAN: Canceling an attack with Y
  - `40000000` - 30: Affects the camera?
  - `80000000` - 31: Affects the camera?

</details>

### 0x150: **CF Flags**

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

### 0x154: **Character Modifier Flag**

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

### 0x15c: **Active Hitbox Check**

  - FFFFFFFF when no hitbox is active
  - 00000000 when hitbox is active

### 0x164: **Combo Count 1**

  - Normal tally.
  - Added to Combo Count 2 to get combo count

### 0x166: **Combo Count 2**

  - Capture state tally, for attacks that add to combo counter inside of capture state, e.g. supers, or anko 4B(B) second hit
  - Added to Combo Count 1 to get combo count

### 0x168: **Hitbox Struct**

  - A struct where one of the fields stores active hitboxes and other stuff.
  - Modified in `create_hitbox`
  - Offset 0x3c: Pointer to hitboxes, where each hitbox is 0x40 bytes. Appears to be a maximum of 0x14 hitboxes allowed so 0x500 bytes total.

### 0x19c: **X Position**

### 0x1a0: **Y Position**

### 0x1a4: **Z Position**

### 0x1bc: **Facing Opponent**

  - A signed short representing the degree to which you are facing the opponent. 0 is directly facing the opponent, −32,767 is directly facing away from your opponent.

### 0x1cc: Movement Flags

  - Set to 0x1 if being pushed horizontally or vertically (fields 0x1d4 and 0x1dc). Sometimes set to 0x2 when doing other things like walking.

### 0x1d4: **Horizontal Push Speed**

  - A float value representing a push or pull horizontally on the character. Normally 0. Positive pushes the character forward, negative pulls them backwards. Kinda looks like a [Raging Demon](https://streetfighter.fandom.com/wiki/Shun_Goku_Satsu).

### 0x1d8: **Horizontal Push Acceleration**

  - A float value representing the amount to decrease Horizontal Push Speed (field 0x1d4) per frame. Positive increases it, negative decreases it.

### 0x1dc: **Vertical Push Speed**

  - A float value representing how fast you are moving up or down. Normally 0. When jumping starts at 1.42, peaks at 0, and ends at -1.56. Positive is moving up, negative is moving down.

### 0x1e0: **Vertical Push Acceleration**

- Also known as gravity.

### 0x1e8: **Horizontal Air Speed**

### 0x1f4: **Knockback Speed**

### 0x1f8: **Knockback Acceleration**

### 0x230: **chr_tbl**

  - Pointer to memory address for characters chr\_tbl

### 0x234: **chr_cam**

  - Offset to characters chr_cam in seq file

### 0x238: **Act Counter Difference**

  - The amount to add to the **Act Counter** every frame.

### 0x23c: **Act ID**

  - Current Action ID

### 0x240: **Last Act ID**

  - The last Action ID executed, updated at 0xA74 in the chr seq files. When Act ID and Last Act ID are not equal, the game knows that the action has changed and will re-initialize many values at instruction 0x800178ec.

### 0x24c: **Something about jumping and attacking**

- Start round at FFFFFFFF
- Set to 1D when jumping
- Set to E4 at start of dive kick
- Set to FFFFFFFF at end of dive kick or start of air throw

### 0x250: **Changes on start of actions that moves character**

  - Getting thrown
  - Doing any attack

### 0x254: **Unknown**

  - Start round at FFFFFFFF
  - Set to 0 first jump

### 0x258: **Act Counter**

  - Resets to 0 at the end of your last action. Can be displayed in the debug menu under the ACT mess, labeled on the right side as ACT.

### 0x25c: **Current Recoverable Damage**

  - Current recoverable health. Counts up from 0.
  - REMAIN in debug mode (LIFE)

### 0x260: **Current Damage**

  - Current health. Counts up from 0.
  - TOTAL in debug mode (LIFE)

### 0x264: **Current REC**

  - REC in debug mode (LIFE)

### 0x26c: **Health Frame Counter**

  - Used to count frames for damage/healing over time. e.g. Tsunade heal.

### 0x270: **Transform Drain Counter**

  - Used for every character but transformed Kakashi, Naruto, and Lee.
    If current recoverable damage is less than current damage, heal 1 health.
    The counter counts up by 1 until it reaches 0x18.

### 0x278: **Health Recovery Drain Counter**

  - Every frame counts up by 1 until it reaches 0x14, and either adds and subtracts 1 health.
    Used with the Health Recovery and Drain handicaps.

### 0x27c: **Max Damage**

  - The total health of your character. You die when **Current Damage** >= **Max Damage**

### 0x280: **New Damage**

  - This gets added to **Current Damage**. Can be negative, which results in healing.

### 0x288: **Last Damage**

  - The **New Damage** of the previous attack.

### 0x28c: **Current Chakra**

### 0x290: **New Chakra**

  - Signed integer, this gets added to **Current Chakra**. Can be negative, which results in drain.

### 0x294: **Current Block Guard**

### 0x298: **Max Block Guard**

### 0x29c: **GRD**

  - GRD value current attack

### 0x2a0: **Confusion Flag**

  - The flag for which Tsunade confusion effect you are afflicted with. `0` is reverse directions. `1` is reverse buttons (A with B, Y with X).
  Set at dol address 0x8003bad0.

### 0x2a4: **Confusion Timer**

  - The timer for how long you are affected by Tsunade's confusion effect. Initialized to 300 frames (5 seconds) at dol address 0x8003bad4.

### 0x2a8: **Idle Counter 2**

  - Appears to be a duplicate of **Idle Counter**

### 0x2ac: **Hitbox Removal Timer**

  - Count down 100 each frame, hitbox disappear when timer reach 0.

### 0x2b0: **Hitbox Appearance Timer**

  - Count down 100 each frame, hitbox appear when timer reach 0.

### 0x2b4: **Synchronous timer after hitbox**

Neutral in this case means idling and is represented by END in ATK debug menu.

  - FFFFFFFF in neutral
  - 00000000 at start of action
  - Count up 100 from 0 each frame after hitbox disappear (at instruction 0x80017200)

### 0x2b8: **DIR**

  - What angle the attacking character was turned away from the opponent when the attack connected

### 0x2bc: **POW**

  - Current attack POW value

### 0x2c0: **ANG**

  - Current attack ANG value

### 0x2c4: **Attack Multiplier**

  - A multiplier that is applied to the damage you do. Defaults to 1. Choji chips can raise it up to a max of 1.5.

### 0x2c8: **DMG**

  - Current attack DMG value

### 0x2d0: **REV**

### 0x2d4: **REV2**

### 0x2d8: **Block Stun**

  - Shows how many frames blockstun last received attack gave

### 0x2dc: **Stand up timer**

  - Timer idling on the ground before standing up

### 0x2ec: **Inactionable timer**

  - No inputs possible before timer reach 0
  - Used at round start or after reset

### 0x2f0: **Intangible timer**

  - Reset when moving
  - Set when standing up
  - Count down 100 each frame

### 0x2f4: **Anti Super timer?**

  - Count down 100 each frame
  - If super connect when not 0, character freeze

### 0x2f8: **Grab Break Counter**

  - A counter that while it is not zero, you can break a grab. Seems to always be set to 0x300 at instruction 0x800b5144. Every frame subtracts 0x100 at instruction 0x8001aaec.

### 0x3be: **Current Buttons Held**

  - Half-word bitflag of buttons pressed. Some of the bitflags are for "states" more than buttons pressed, e.g. Facing Left.
<details>
  <summary>Button mapping</summary>
  
  | Button      | Bitflag |
  |-------------|---------|
  | Forward     | 0x1     | 
  | Back        | 0x2     |
  | Up          | 0x4     |
  | Down        | 0x8     |
  | B           | 0x10    |
  | A           | 0x20    |
  | ???         | 0x40    |
  | ???         | 0x80    |
  | Facing Left | 0x100   |
  | Y           | 0x200   |
  | ???         | 0x400   |
  | L           | 0x800   |
  | R           | 0x1000  |
  | X           | 0x2000  |
  | Z           | 0x4000  |
  | ???         | 0x8000  |
  
</details>

### 0x54c: **Active Attacks**

  - Pointer to where in memory the available throws, supers and jump attacks are defined
  - Each active attack consists of two parts
    - Header tells which attack is to be activated and where extra data is located
    - Extra data contains requirements for the attack to activate

<details>
  <summary>Header</summary>
  
  - Byte 1-2 seems to be dependant on what attack it is
    - `0000` air throw (naruto transform)
    - `0001` air attack
    - `0003` jump squat attack
    - `0008` super
    - `0020` grounded throw
    - `0040` z swap
    - `0080` unknown
  - Byte 3 seems to only matter for throws
    - `00` not a throw
    - `56` throw from the front
    - `66` throw from the back
    - `79` air throw
  - Byte 4
    - `00` air moves
    - `03` unknown
    - `23` supers (including transformation)
    - `80` ground throw
  - Byte 5-6 is ATK ID
  - Byte 7-8 
    - `0004` any throw
    - `0008` jump and jump squat
    - `000D` anything that drains chakra
  - Byte 9-10
    - `0014` throws, jump attack and jump squat attacks
    - `001E` anything else
  - Byte 11-12 0 all
  - Byte 13-14
    - `0000` anything else
    - `42E0` grounded throw
    - `4316` air throw
    - `C248` jump attack
    - `C32A` jump squat attack
  - Byte 15-16 0 all
  - Byte 17-20 offset in file to extra data
  
</details>

<details>
<summary>Extra data</summary>
  
- `0001000A` incoming command
- Command types
  - `0001` directional input
    - Byte 1-2 probably a mask for what inputs to read among
    - Byte 3-4 the sought after input, can be directional by setting two cardinal directions as input
  - `0002` button input
    - `2270`
      - Button input
    - `227F`
      - Button input and chakra cost, can be extended with more unknown commands. Terminated with 8 bytes of 0
  
</details>

### 0x7d8: **Start String Offset**

- Where the offsets for all the characters strings start
- Header is a list with an offset to each active string, terminated by 4 bytes of 0
<details>
<summary>String structure</summary>
  
- `0001`
- 2 bytes atk id that this string combo from
 - if start with `40`, the second byte is how many atk id's this instruction is for
 - follow with a list of 2 byte atk id
- `0004`
- 2 bytes input leeway after hitbox ends, default `FFFF`
- 2 bytes earliest frame delay after hitbox disappear
- 2 bytes condition continue, default `0002`, other behaviour unknown
- 2 bytes number of inputs required for activation, default `0001`
- `00062270`
- 2 bytes button input, direction ignored
- `0000` seems to be padding
- 2 bytes whiffable or not
  - `0003` allow follow up on whiff
  - `0007` don't allow follow up on whiff
- 2 bytes attack id to combo into
- 4 bytes unknown normal values include
  - `00000028` most common
  - `00000090`
  - `00000096`
  - `00000098`
  - `0000009A`
- 2 bytes tells if it terminates or not
  - `0000` final part of this string
  - `0004` start over with the input leeway after hitbox after this one, and continue
  - Other values unknown
  
</details>
  

### 0x7e0: **Something with Strings**

  - 2 Bytes
  - Set upon controller input
  - POW is added to it
  - If early, can be overwritten at a later frame
  - Set to 0 if **PF FLAG** combo is not set and the value in 0x7f8 is < 0

### 0x7e2: **String Next ATK ID**

  - 2 Bytes
  - Set upon controller input

### 0x7e4: **Something with Strings**

  - 2 Bytes
  - Set to 0 if **PF FLAG** combo is not set and the value in 0x7f8 is < 0

### 0x7e6: **Something with Strings**

  - 2 Bytes
  - Set sometimes in strings
  - Set to 0 if **PF FLAG** combo is not set and the value in 0x7f8 is < 0

### 0x7ec: **Something with Strings**

  - 4 Bytes
  - Set sometimes in strings

### 0x7f4: **Something with Strings**

  - 2 Bytes
  - Compared with 0x7f6

### 0x7f6: **Something with Strings**
  
  - 2 Bytes
  - Seem to oscillate between 0 and 1

### 0x7f8: **0x7f6 previous value**

  - 2 Bytes
  - Value in 0x7f6 backed up here before being manipulated

### 0x7fc: **Capture Range**
  
  - If small, the opponent will not get captured. The `throw_logic()` expects this to be 0x8000 to initiate capture
    at 0x80063448.

### 0x800: **capture\_state\_attack**

  - Signed short
  - Normally -1
  - Set to attack id of the capture state move
  - Opponent act forced to 0xF0 + value set here

### 0x804 **Throw Qualifying Distance**

The distance between the two players to qualify a throw. Usually 11.2.

### 0x854: **Transformation Flag**

  - 0 is Naruto, 2 is ZTK.
  - 0 is Sasuke, 2 is Sharingan Sasuke.
  - 0 is Kakashi, 2 is Sharingan Kakashi.
  - 0 is Lee, 2 is First Gate, 6 is Second Gate.
  - 0 is Gai, 2 is First Gate.
  - 0 is Sakon, 0x2002 is Ukon.
  - 0 is Tsunade, 2 is Tsunade Healing from 2X
  - 8 is unknown but used in some places like 0x8003e470
  - 0x20 prevents web trap (YORO2) at 0x8005e580

### 0x87c: **SF Flags**

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

### 0x894: **Air Fall Combo Counter**

The current combo count against this character, used to slowly increase gravity as the combo continues. Written to at 0x8003a884 and sometimes 0x8003bb04 in `damage_stuff`. Read from functions `calculate_air_fall_1` and `calculate_air_fall_2`.

### 0x8C8: **Synchronous timer**

Set by opcode 2011263F.

### 0x954 **Throw Target**

Pointer to the character struct of the target of a throw or projectile

### 0x960 **Opponent Target**

Pointer to potentially the target of an attack. Set at dol address 0x8003ba78

### 0x964 **Capture Target**

Pointer to the target of capture, such as Kidomaru 6A.

### 0x968 **Captured By**

Pointer to the person capturing the current player, such as Kidomaru 6A.

### 0x974: **Opponent Character Struct**

Pointer to potentially one or more enemy character structs.
