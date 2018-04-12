# Sequence Files
Files ending with .seq dictate just about everything about the UI and characters that aren't art assets. This includes damage, speed, which animation to play, hitboxes, etc.

### KF Flags
These are for value *24 1A 12 00*

| Value       |  Name    |  Description                                    | 
|-------------|----------|-------------------------------------------------| 
| 00          |  None    |                                                 | 
| 01          |  Replay  |                                                 | 
| 02          |  Bdrive  |  No sub or roll for the rest of the combo       | 
| 04          |  Shot    |  Projectile                                     | 
| 08          |  Pow_W   |  Weak Hit                                       | 
| 10          |  Pow_M   |  Medium Hit                                     | 
| 20          |  Pow_S   |  Strong Hit                                     | 
| 40          |  Low     |                                                 | 
| 80          |  Medium  |                                                 | 
| 01 00       |  High    |                                                 | 
| 02 00       |  Punch   |                                                 | 
| 04 00       |  Kick    |                                                 | 
| 08 00       |  Throw   |                                                 | 
| 10 00       |  Oiuchi  |                                                 | 
| 20 00       |  Special |  Builds no chakra when it connects              | 
| 40 00       |  NoGuard |  Unblockable attack                             | 
| 80 00       |  Tdown   |                                                 | 
| 1 00 00     |  SPTata  |  Large bounce                                   | 
| 2 00 00     |  Break   |  Lift opponents guard                           | 
| 4 00 00     |  Combo   |  Attacks that can be followed into on whiff     | 
| 8 00 00     |  Down    |  Spinout launcher                               | 
| 10 00 00    |  Yoro    |  Stagger                                        | 
| 20 00 00    |  Butt    |  Flying screen                                  | 
| 40 00 00    |  Uki     |  Launch                                         | 
| 80 00 00    |  Furi    |  Turns opponent around                          | 
| 1 00 00 00  |  Koro    |  Sweep                                          | 
| 2 00 00 00  |  Reach_L |  Makes the projectile appear when it is removed | 
| 4 00 00 00  |  Tata    |  Bounce                                         | 
| 8 00 00 00  |  NoSpeEp |                                                 | 
| 10 00 00 00 |  Beast   |  Causes a slash effect and chip damage          | 
| 20 00 00 00 |  Freeze  |                                                 | 
| 40 00 00 00 |  Cancel  |  Hyuuga cancel                                  | 
| 80 00 00 00 |  AtkCan  |  Super Cancel                                   | 

### K2F Flags
These are for value *24 1A 48 00*

| Value   |  Name       |  Description                 | 
|---------|-------------|------------------------------| 
| 01      |  yoro2      |  Feet trapped                | 
| 02      |  hiki       |  Jiraya 2A                   | 
| 04      |  hiki2      |  Shika 2X                    | 
| 08      |  mission    |                              | 
| 10      |  natemi     |                              | 
| 20      |  superarmor |                              | 
| 40      |  mato2      |  Feet trapped                | 
| 80      |  atkallcan  |  Can cancel in to any attack | 
| 1 00    |  toji       |                              | 
| 2 00    |  hasa       |  Jirobo crumple              | 
| 4 00    |  shave      |  Kisame sword                | 
| 8 00    |  nemu       |  Sleep                       | 
| 10 00   |  wing       |                              | 
| 20 00   |  null       |                              | 
| 40 00   |  null       |                              | 
| 80 00   |  null       |                              | 
| 1 00 00 |  null       |                              | 
