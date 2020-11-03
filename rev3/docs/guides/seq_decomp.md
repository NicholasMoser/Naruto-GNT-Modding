## Reading Opcodes

The opcode is read from the seq file in the seq_parse method. It uses the following function to find the pointer to code associated with it:

```c
0x802103a0 + (opcode >> 0x16 & 0x3fc)
```

1. Read opcode, e.g. `0x01320000` (`0001001100100000000000000000` in binary)
2. Use bit shifting to get the top 6 bits, `000100` in this case.
3. & it with `0x3fc` (`001111111100` in binary)
4. For this example, that doesn't change the value and it stays as `000100` in binary, or 4 in hex.
5. This value is added as an offset to `0x802103a0`, which is a location to a pointer table in memory.
6. For this example, we get the final value `0x800a5698`, which is the second pointer in the opcode pointer table.

The highest value that can come from this math is `0x3fc`, so the opcode pointer table is between `0x802103a0` and `0x8021079C`

<details>
  <summary>Opcode Pointer Table</summary>

| Opcode | Offset | Code Pointer |  Purpose  |
|--------|--------|--------------|-----------|
| 0x0    | 0x0    | 80139894     |           |
| 0x1    | 0x4    | 80139B2C     | Branching |
| 0x2    | 0x8    | 8013A728     |           |
| 0x3    | 0xc    | 8013ADFC     |           |
| 0x4    | 0x10   | 8013AFF8     |           |
| 0x5    | 0x14   | 8013B94C     |           |
| 0x6    | 0x18   | 8013C3C4     |           |
| 0x7    | 0x1c   | 8013CD6C     |           |
| 0x8    | 0x20   | 8013D36C     |           |
| 0x9    | 0x24   | 8013D790     |           |
| 0xa    | 0x28   | 8013DC60     |           |
| 0xb    | 0x2c   | 8013DF80     |           |
| 0xc    | 0x30   | 8013E554     |           |
| 0xd    | 0x34   | 80150AFC     |           |
| 0xe    | 0x38   | 80150C88     |           |
| 0xf    | 0x3c   | 801518C4     |           |
| 0x10   | 0x40   | 80152030     |           |
| 0x11   | 0x44   | 801525DC     |           |
| 0x12   | 0x48   | 8015317C     |           |
| 0x13   | 0x4c   | 00000000     | Invalid   |
| 0x14   | 0x50   | 00000000     | Invalid   |
| 0x15   | 0x54   | 00000000     | Invalid   |
| 0x16   | 0x58   | 00000000     | Invalid   |
| 0x17   | 0x5c   | 00000000     | Invalid   |
| 0x18   | 0x60   | 00000000     | Invalid   |
| 0x19   | 0x64   | 80162A90     |           |
| 0x1a   | 0x68   | 80162B50     |           |
| 0x1b   | 0x6c   | 00000000     | Invalid   |
| 0x1c   | 0x70   | 00000000     | Invalid   |
| 0x1d   | 0x74   | 00000000     | Invalid   |
| 0x1e   | 0x78   | 8015DFB4     |           |
| 0x1f   | 0x7c   | 8015E424     |           |
| 0x20   | 0x80   | 8015E8AC     |           |
| 0x21   | 0x84   | 00000000     | Invalid   |
| 0x22   | 0x88   | 00000000     | Invalid   |
| 0x23   | 0x8c   | 801626F0     |           |
| 0x24   | 0x90   | 00000000     | Invalid   |
| 0x25   | 0x94   | 00000000     | Invalid   |
| 0x26   | 0x98   | 00000000     | Invalid   |
| 0x27   | 0x9c   | 00000000     | Invalid   |
| 0x28   | 0xa0   | 8015EDB4     |           |
| 0x29   | 0xa4   | 00000000     | Invalid   |
| 0x2a   | 0xa8   | 00000000     | Invalid   |
| 0x2b   | 0xac   | 80148C18     |           |
| 0x2c   | 0xb0   | 8014983C     |           |
| 0x2d   | 0xb4   | 80149C60     |           |
| 0x2e   | 0xb8   | 80149FEC     |           |
| 0x2f   | 0xbc   | 8014B0CC     |           |
| 0x30   | 0xc0   | 8014B39C     |           |
| 0x31   | 0xc4   | 8014B514     |           |
| 0x32   | 0xc8   | 8014B794     |           |
| 0x33   | 0xcc   | 8014BBE4     |           |
| 0x34   | 0xd0   | 8014D12C     |           |
| 0x35   | 0xd4   | 8014EF50     |           |
| 0x36   | 0xd8   | 8014F82C     |           |
| 0x37   | 0xdc   | 80150244     |           |
| 0x38   | 0xe0   | 00000000     | Invalid   |
| 0x39   | 0xe4   | 00000000     | Invalid   |
| 0x3a   | 0xe8   | 00000000     | Invalid   |
| 0x3b   | 0xec   | 00000000     | Invalid   |
| 0x3c   | 0xf0   | 8013E778     |           |
| 0x3d   | 0xf4   | 8013F334     |           |
| 0x3e   | 0xf8   | 8013FA84     |           |
| 0x3f   | 0xfc   | 8013FBC8     |           |
| 0x40   | 0x100  | 80140920     |           |
| 0x41   | 0x104  | 80140AF8     |           |
| 0x42   | 0x108  | 00000000     | Invalid   |
| 0x43   | 0x10c  | 00000000     | Invalid   |
| 0x44   | 0x110  | 00000000     | Invalid   |
| 0x45   | 0x114  | 00000000     | Invalid   |
| 0x46   | 0x118  | 80153E5C     |           |
| 0x47   | 0x11c  | 80155AD0     |           |
| 0x48   | 0x120  | 80155D50     |           |
| 0x49   | 0x124  | 801563C8     |           |
| 0x4a   | 0x128  | 80156738     |           |
| 0x4b   | 0x12c  | 8015788C     |           |
| 0x4c   | 0x130  | 8015831C     |           |
| 0x4d   | 0x134  | 801587F4     |           |
| 0x4e   | 0x138  | 80158EA0     |           |
| 0x4f   | 0x13c  | 8015949C     |           |
| 0x50   | 0x140  | 801597AC     |           |
| 0x51   | 0x144  | 8015B3C0     |           |
| 0x52   | 0x148  | 8015C058     |           |
| 0x53   | 0x14c  | 8015C060     |           |
| 0x54   | 0x150  | 8015C464     |           |
| 0x55   | 0x154  | 8015C868     |           |
| 0x56   | 0x158  | 8015D5B4     |           |
| 0x57   | 0x15c  | 801467D4     |           |
| 0x58   | 0x160  | 801475D0     |           |
| 0x59   | 0x164  | 80163178     |           |
| 0x5a   | 0x168  | 00000000     | Invalid   |
| 0x5b   | 0x16c  | 801646D4     |           |
| 0x5c   | 0x170  | 801646E4     |           |
| 0x5d   | 0x174  | 801646F4     |           |
| 0x5e   | 0x178  | 80164704     |           |
| 0x5f   | 0x17c  | 8016474C     |           |
| 0x60   | 0x180  | 8016474C     |           |
| 0x61   | 0x184  | 80164724     |           |
| 0x62   | 0x188  | 80164714     |           |
| 0x63   | 0x18c  | 80164734     |           |
| 0x64   | 0x190  | 8016474C     |           |
| 0x65   | 0x194  | 8016474C     |           |
| 0x66   | 0x198  | 8016474C     |           |
| 0x67   | 0x19c  | 8016474C     |           |
| 0x68   | 0x1a0  | 8016474C     |           |
| 0x69   | 0x1a4  | 8016474C     |           |
| 0x6a   | 0x1a8  | 80164744     |           |
| 0x6b   | 0x1ac  | 00000000     | Invalid   |

</details>
