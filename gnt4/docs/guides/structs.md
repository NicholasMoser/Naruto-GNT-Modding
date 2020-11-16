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

- 0x07: Character ID. See [INTERNAL_CHAR_ORDER](https://github.com/NicholasMoser/GNTool/blob/3.7/src/main/java/com/github/nicholasmoser/gnt4/GNT4Characters.java#L105)
- 0x44: **Movement Stuff**
  - Pointer to some movement related stuff.
- 0x4C: Flags
  - `0x810000` is invincibility; all damage becomes 0. See `damage_handler(uint* chr_p)`.
- 0x67: **X Position**
- 0x68: **Y Position**
- 0x69: **Z Position**
- 0x6F: **Facing Opponent**
  - A signed short representing the degree to which you are facing the opponent. 0 is directly facing the opponent, −32,767 is directly facing away from your opponent.
- 0x77: **Vertical Speed**
- 0x7a: **Horizontal Air Speed**
- 0x8E: **Idle Counter Difference**
  - The amount to add to the **Idle Counter** every frame.
- 0x78: **Gravitational Constant**
- 0x96: **Idle Counter**
  - Resets to 0 when any button is pressed.
- 0x98: **Current Damage**
  - Current health. Counts up from 0.
- 0x9B: **Health Frame Counter**
  - Used to count frames for damage/healing over time. e.g. Tsunade heal.
- 0x9F: **Max Damage**
  - The total health of your character. You die when **Current Damage** >= **Max Damage**
- 0xA0: **New Damage**
  - This gets added to **Current Damage**. Can be negative, which results in healing.
- 0xA2: **Last Damage**
  - The **New Damage** of the previous attack.
- 0xA3: **Current Chakra**
- 0xA5: **Current Block Guard**
- 0xA6: **New Block Guard**
  - This gets set to **Current Block Guard**
- 0xAA: **Idle Counter 2**
  - Appears to be a duplicate of **Idle Counter**
