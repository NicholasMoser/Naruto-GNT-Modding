# Game Struct

Used in game00.seq, currently is labeled as *chr_p.

## Values

### 0x08: **Round State**

Something involving round state. Is set to 0x4 during battle and changes as battle starts and ends.

- 4 normal battle state
- 5 the moment your opponent dies
- 6 
- 7 
- 8 end of round

8 then goes to 1 on round start

- 1 when round start
- 2
- 3
- 4 when fighting can start

Or, 8 goes to 9 on game end

- 9 when game end
