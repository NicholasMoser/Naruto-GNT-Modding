# Useful Memory Locations
The following memory locations can be used to modify game values while the game is running. This is useful for writing Gecko codes to change game logic. They can be modified by using Dolphin's built-in debug mode. Please note that these values may be used for other things in the game (many are used while the intro cutscene is playing), so side effects can occur.

| Hex Location |  Bytes |  Type  |  Description                                                                               | 
|--------------|--------|--------|--------------------------------------------------------------------------------------------| 
| 8024A594     |  4     |  Int   |  Very fast universal timer                                                                 | 
| 8106C37C     |  4     |  Int   |  Set to 0x00000001 if in character select and 0x00000000 if not.                           | 
| 802FD704     |  4     |  Int   |  Title screen demo trigger timer (0x00000258 triggers demo which correlates to 10 seconds) | 
| 8031B7AC     |  4     |  Int   |  Training Mode: P1 Chakra Count (Max is 0x00003C00)                                        | 
| 8031B6FC     |  4     |  Float |  Training Mode: P1 Vertical Speed                                                          | 
| 8031B700     |  4     |  Float |  Training Mode: P1 Gravitational Constant (-0.083008)                                      | 
| 802D5D17     |  4     |  Int   |  Training Mode: P1 Character Select (Visual)                                               | 
| 802DB4E3     |  4     |  Int   |  Training Mode: P1 Character Select (Actual)                                               | 
| 802D5D47     |  4     |  Int   |  Training Mode: P2 Character Select (Visual)                                               | 
| 802DB4E7     |  4     |  Int   |  Training Mode: P2 Character Select (Actual)                                               | 
| 802D5CF7     |  4     |  Int   |  Versus Mode: P1 Character Select (Visual)                                                 | 
| 802DB4C3     |  4     |  Int   |  Versus Mode: P1 Character Select (Actual)                                                 | 
| 802D5D27     |  4     |  Int   |  Versus Mode: P2 Character Select (Visual)                                                 | 
| 802DB4C7     |  4     |  Int   |  Versus Mode: P2 Character Select (Actual)                                                 | 
| 802DAA57     |  4     |  Int   |  4-Player Mode: P1 Character Select (Visual)                                               | 
| 802DF5E3     |  4     |  Int   |  4-Player Mode: P1 Character Select (Actual)                                               | 
| 802DAA77     |  4     |  Int   |  4-Player Mode: P2 Character Select (Visual)                                               | 
| 802DF5E7     |  4     |  Int   |  4-Player Mode: P2 Character Select (Actual)                                               | 
| 802DAA97     |  4     |  Int   |  4-Player Mode: P3 Character Select (Visual)                                               | 
| 802DF5EB     |  4     |  Int   |  4-Player Mode: P3 Character Select (Actual)                                               | 
| 802DAAB7     |  4     |  Int   |  4-Player Mode: P4 Character Select (Visual)                                               | 
| 802DF5EF     |  4     |  Int   |  4-Player Mode: P4 Character Select (Actual)                                               | 
| 80222D40     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 80222D74     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 80222DA8     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 80222DDC     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 80222E10     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 80222E96     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 80222ECE     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 80222ED6     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 8024A630     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 8024C7F6     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 8024C7FA     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 8024C906     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 8024C90A     |  2     |  Int   |  Player 1 Controller Input (Buttons)                                                       | 
| 80222D4C     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 80222D80     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 80222DB4     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 80222DE8     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 80222E1C     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 80222E92     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 80222F0E     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 80222F12     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 80222F16     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 8024A638     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 8024C83A     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 8024C83E     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 8024C846     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 8024C94A     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 8024C94E     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
| 8024C956     |  2     |  Int   |  Player 2 Controller Input (Buttons)                                                       | 
