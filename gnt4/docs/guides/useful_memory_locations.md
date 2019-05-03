# GNT4 Useful Memory Locations

The following memory locations can be used to modify game values while the game is running. This is useful for writing Gecko codes to change game logic. They can be modified by using Dolphin's built-in debug mode. Please note that these values may be used for other things in the game (many are used while the intro cutscene is playing), so side effects can occur.

## Difference Between Absolute and Relative Values

There are two types of hex locations that you may come across, absolute and relative. Absolute hex locations will always be in the same location, for example the title screen demo trigger at 0x802FD704. This hex location is used for other things in other parts of the game, but the title screen demo trigger can always be found there. Relative values are dependent upon certain variables. For example, modifying character health values depends on which controller number you are and which character is selected. In these cases, an absolute hex location will hold a pointer to the relative hex location. Then, the values we wish to modify will be offsets of the resulting relative hex location. Gecko's pointer address operations are used to interact with these relative hex locations.

### Example

The absolute hex location 0x80226358 contains the relative hex location for player 1. If we pick Naruto in training, this is set to relative hex location 0x8031B520 (and will be different if we chose a different character). Now, if we go to this location we will be at the list of player values for player 1. Adding any of the offsets from the relative table will give us the specific location of our desired variable. Chakra values have an offset of 0x28E, so if we add that to 0x8031B520 we get 0x8031B7AE. This value holds player 1's chakra value and can be modified.

## Absolute Values

| Hex Location |  Bytes |   Type  |  Description                                                                               |
|--------------|--------|---------|--------------------------------------------------------------------------------------------|
| 8024A594     |  4     |  uint   |  Very fast universal timer                                                                 |
| 8106C37C     |  4     |  uint   |  Set to 0x00000001 if in character select and 0x00000000 if not.                           |
| 802FD704     |  4     |  uint   |  Title screen demo trigger timer[1]                                                        |
| 802D5D17     |  4     |  uint   |  Training Mode: P1 Character Select (Visual)                                               |
| 802DB4E3     |  4     |  uint   |  Training Mode: P1 Character Select (Actual)                                               |
| 802D5D47     |  4     |  uint   |  Training Mode: P2 Character Select (Visual)                                               |
| 802DB4E7     |  4     |  uint   |  Training Mode: P2 Character Select (Actual)                                               |
| 802D5CF7     |  4     |  uint   |  Versus Mode: P1 Character Select (Visual)                                                 |
| 802DB4C3     |  4     |  uint   |  Versus Mode: P1 Character Select (Actual)                                                 |
| 802D5D27     |  4     |  uint   |  Versus Mode: P2 Character Select (Visual)                                                 |
| 802DB4C7     |  4     |  uint   |  Versus Mode: P2 Character Select (Actual)                                                 |
| 802DAA57     |  4     |  uint   |  4-Player Mode: P1 Character Select (Visual)                                               |
| 802DF5E3     |  4     |  uint   |  4-Player Mode: P1 Character Select (Actual)                                               |
| 802DAA77     |  4     |  uint   |  4-Player Mode: P2 Character Select (Visual)                                               |
| 802DF5E7     |  4     |  uint   |  4-Player Mode: P2 Character Select (Actual)                                               |
| 802DAA97     |  4     |  uint   |  4-Player Mode: P3 Character Select (Visual)                                               |
| 802DF5EB     |  4     |  uint   |  4-Player Mode: P3 Character Select (Actual)                                               |
| 802DAAB7     |  4     |  uint   |  4-Player Mode: P4 Character Select (Visual)                                               |
| 802DF5EF     |  4     |  uint   |  4-Player Mode: P4 Character Select (Actual)                                               |
| 80222D40     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 80222D74     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 80222DA8     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 80222DDC     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 80222E10     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 80222E96     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 80222ECE     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 80222ED6     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 8024A630     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 8024C7F6     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 8024C7FA     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 8024C906     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 8024C90A     |  2     |  uint   |  Player 1 Controller Input (Buttons)                                                       |
| 80222D4C     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 80222D80     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 80222DB4     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 80222DE8     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 80222E1C     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 80222E92     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 80222F0E     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 80222F12     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 80222F16     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 8024A638     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 8024C83A     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 8024C83E     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 8024C846     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 8024C94A     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 8024C94E     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |
| 8024C956     |  2     |  uint   |  Player 2 Controller Input (Buttons)                                                       |

[1] Demo triggers after 10 seconds (0x00000258)

## Relative Values

| Absolute Location |  Offset |  Bytes |  Type  |  Description                                    |
|-------------------|---------|--------|--------|-------------------------------------------------|
| 80226358          |  1DC    |  4     |  float |  P1 Vertical Speed                              |
| 80226358          |  1E0    |  4     |  float |  P1 Gravitational Constant[1]                   |
| 80226358          |  262    |  4     |  uint  |  P1 Health Value                                |
| 80226358          |  28E    |  4     |  uint  |  P1 Chakra Value[2]                             |
| 80226614          |  1DC    |  4     |  float |  P2 Vertical Speed                              |
| 80226614          |  1E0    |  4     |  float |  P2 Gravitational Constant[1]                   |
| 80226614          |  262    |  4     |  uint  |  P2 Health Value                                |
| 80226614          |  28E    |  4     |  uint  |  P2 Chakra Value[2]                             |
| 802268D0          |  1DC    |  4     |  float |  P3 Vertical Speed                              |
| 802268D0          |  1E0    |  4     |  float |  P3 Gravitational Constant[1]                   |
| 802268D0          |  262    |  4     |  uint  |  P3 Health Value                                |
| 802268D0          |  28E    |  4     |  uint  |  P3 Chakra Value[2]                             |
| 80226B8C          |  1DC    |  4     |  float |  P4 Vertical Speed                              |
| 80226B8C          |  1E0    |  4     |  float |  P4 Gravitational Constant[1]                   |
| 80226B8C          |  262    |  4     |  uint  |  P4 Health Value                                |
| 80226B8C          |  28E    |  4     |  uint  |  P4 Chakra Value[2]                             |

[1] Default: -0.083008  
[2] Max: 15360 (0x00003C00)
