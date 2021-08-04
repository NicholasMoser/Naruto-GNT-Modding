# Structs

## Character Struct

Holds values related to a player character in battle. Named `chr_p` in the decompilation. They appear to have a size of `0xA08` bytes.

### Where to Find

The absolute positions of these structs can be found at the locations listed below. Additional locations can be found in `chr_init_dummy_team`, `chr_init_player`, `chr_init_static`, or `chr_init_team` after the call to `TRK_memset`.

- Player 1: `80226358`
- Player 2: `80226614`
- Player 3: `802268D0`
- Player 4: `80226B8C`
- Training Mode Single CPU: `802283FC`

### Values

- 0x00: Flags
  - 0x00000001: If set to 0, the character is removed. Probably used to remove clones and such.
  - 0x8: Invincibility; all damage becomes 0. Used in `damage_handler()`.
- 0x10: **CPU Flags**
  - 0 if a player, other values if non-player controlled.
- 0x1c: **Character ID**
  - See [INTERNAL_CHAR_ORDER](https://github.com/NicholasMoser/GNTool/blob/3.7/src/main/java/com/github/nicholasmoser/gnt4/GNT4Characters.java#L105)
- 0x110: **Movement Stuff**
  - Pointer to some movement related stuff.
- 0x128: Flags
  - 0x00001000: Jumping
  - 0x00002000: Falling from a jump.
  - 0x80000000: Causes counter hits. Used in `counter_hit_check()`.
- 0x130: Flags
  - 0x00000008: If the player has double jumped. Set to 0x8 when you double jump. When set to 0x8 prevents a double jump.
  - 0x00810000: Invincibility; all damage becomes 0. Used in `damage_handler()`.
- 0x138: Flags
  - Used in `counter_hit_check()`.
- 0x140: Flags
  - 0x02000000: Set on counter hit. Used in `counter_hit_check()`.
  - 0x30000000: Causes counter hits. Used in `counter_hit_check()`.
- 0x164: **Combo Count 1**
  - Added to Combo Count 2 to get combo count
- 0x166: **Combo Count 2**
  - Added to Combo Count 1 to get combo count
- 0x19c: **X Position**
- 0x1a0: **Y Position**
- 0x1a4: **Z Position**
- 0x1bc: **Facing Opponent**
  - A signed short representing the degree to which you are facing the opponent. 0 is directly facing the opponent, −32,767 is directly facing away from your opponent.
- 0x1dc: **Vertical Speed**
- 0x1e0: **Gravitational Constant**
- 0x1e8: **Horizontal Air Speed**
- 0x1f4: **Knockback Velocity**
- 0x1f8: **Knockback Acceleration**
- 0x238: **Act Counter Difference**
  - The amount to add to the **Act Counter** every frame.
- 0x258: **Act Counter**
  - Resets to 0 at the end of your last action. Can be displayed in the debug menu under the ACT mess, labeled on the right side as ACT.
- 0x260: **Current Damage**
  - Current health. Counts up from 0.
- 0x26c: **Health Frame Counter**
  - Used to count frames for damage/healing over time. e.g. Tsunade heal.
- 0x27c: **Max Damage**
  - The total health of your character. You die when **Current Damage** >= **Max Damage**
- 0x280: **New Damage**
  - This gets added to **Current Damage**. Can be negative, which results in healing.
- 0x288: **Last Damage**
  - The **New Damage** of the previous attack.
- 0x28c: **Current Chakra**
- 0x294: **Current Block Guard**
- 0x298: **Max Block Guard**
- 0x2a8: **Idle Counter 2**
  - Appears to be a duplicate of **Idle Counter**
- 0x2c4: **Attack Multiplier**
  - A multiplier that is applied to the damage you do. Defaults to 1. Choji chips can raise it up to a max of 1.5.
- 0x854: **Transformation Flag**
  - 0 is Naruto, 2 is ZTK.
  - 0 is Sasuke, 2 is Sharingan Sasuke.
  - 0 is Kakashi, 2 is Sharingan Kakashi.
  - 0 is Lee, 2 is First Gate, 6 is Second Gate.
  - 0 is Gai, 2 is First Gate.
  - 0 is Sakon, 0x2002 is Ukon.
  - 0 is Tsunade, 2 is Tsunade Healing from 2X
