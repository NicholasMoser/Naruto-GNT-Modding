# SEQ Decompilation

This page includes information regarding the decompilation of the SEQ format and how it is parsed.

## SEQ Header

The file begins with a 16 byte header. Only the first three four-byte words are used. The last four bytes are always zero. The values of each word used by SEQ files in the game are:

<details>
  <summary>First word</summary>

- 0x01
- 0x02
- 0x04
- 0x05
- 0x06
- 0x07
- 0x08
- 0x09
- 0x0C
- 0x0E
- 0x10
- 0x11
- 0x16
- 0x1F

</details>

<details>
  <summary>Second Word</summary>

- 0x0010
- 0x0020
- 0x0025
- 0x0026
- 0x0027
- 0x0028
- 0x0029
- 0x002A
- 0x002B
- 0x002C
- 0x002D
- 0x002E
- 0x0035
- 0x0040
- 0x004E
- 0x006C
- 0x01A0
- 0x01B0
- 0x0A48

</details>

<details>
  <summary>Third Word</summary>

- 0x10
- 0x20
- 0x40

</details>

Here are the headers of each SEQ file in the game:

<details>
  <summary>Headers</summary>

```output
00000011 00000a48 00000040 00000000 /files/chr/ank/0000.seq
00000007 00000028 00000040 00000000 /files/chr/ank/0010.seq
00000001 00000027 00000040 00000000 /files/chr/ank/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/bou/0000.seq
00000007 00000028 00000040 00000000 /files/chr/bou/0010.seq
00000001 0000002c 00000040 00000000 /files/chr/bou/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/cho/0000.seq
00000007 00000028 00000040 00000000 /files/chr/cho/0010.seq
00000001 00000026 00000040 00000000 /files/chr/cho/1000.seq
00000001 0000004e 00000040 00000000 /files/chr/cmn/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/dog/0000.seq
00000007 00000028 00000040 00000000 /files/chr/dog/0010.seq
00000001 00000025 00000040 00000000 /files/chr/dog/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/gai/0000.seq
00000007 00000028 00000040 00000000 /files/chr/gai/0010.seq
00000001 0000002c 00000040 00000000 /files/chr/gai/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/gar/0000.seq
00000007 00000028 00000040 00000000 /files/chr/gar/0010.seq
00000001 0000002c 00000040 00000000 /files/chr/gar/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/hak/0000.seq
00000007 00000028 00000040 00000000 /files/chr/hak/0010.seq
00000001 00000025 00000040 00000000 /files/chr/hak/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/hi2/0000.seq
00000007 00000028 00000040 00000000 /files/chr/hi2/0010.seq
00000001 0000002c 00000040 00000000 /files/chr/hi2/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/hin/0000.seq
00000007 00000028 00000040 00000000 /files/chr/hin/0010.seq
00000001 00000025 00000040 00000000 /files/chr/hin/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/ino/0000.seq
00000007 00000028 00000040 00000000 /files/chr/ino/0010.seq
00000001 00000029 00000040 00000000 /files/chr/ino/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/iru/0000.seq
00000007 00000028 00000040 00000000 /files/chr/iru/0010.seq
00000001 00000025 00000040 00000000 /files/chr/iru/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/ita/0000.seq
00000007 00000028 00000040 00000000 /files/chr/ita/0010.seq
00000001 00000028 00000040 00000000 /files/chr/ita/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/jir/0000.seq
00000007 00000028 00000040 00000000 /files/chr/jir/0010.seq
00000001 00000025 00000040 00000000 /files/chr/jir/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/kab/0000.seq
00000007 00000028 00000040 00000000 /files/chr/kab/0010.seq
00000001 00000026 00000040 00000000 /files/chr/kab/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/kak/0000.seq
00000007 00000028 00000040 00000000 /files/chr/kak/0010.seq
00000001 0000002c 00000040 00000000 /files/chr/kak/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/kan/0000.seq
00000007 00000028 00000040 00000000 /files/chr/kan/0010.seq
00000001 00000025 00000040 00000000 /files/chr/kan/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/kar/0000.seq
00000007 00000028 00000040 00000000 /files/chr/kar/0010.seq
00000001 00000026 00000040 00000000 /files/chr/kar/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/kib/0000.seq
00000007 00000028 00000040 00000000 /files/chr/kib/0010.seq
00000001 00000025 00000040 00000000 /files/chr/kib/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/kid/0000.seq
00000007 00000028 00000040 00000000 /files/chr/kid/0010.seq
00000001 00000035 00000040 00000000 /files/chr/kid/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/kim/0000.seq
00000007 00000028 00000040 00000000 /files/chr/kim/0010.seq
00000001 0000002d 00000040 00000000 /files/chr/kim/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/kis/0000.seq
00000007 00000028 00000040 00000000 /files/chr/kis/0010.seq
00000001 00000026 00000040 00000000 /files/chr/kis/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/loc/0000.seq
00000007 00000028 00000040 00000000 /files/chr/loc/0010.seq
00000001 00000029 00000040 00000000 /files/chr/loc/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/miz/0000.seq
00000007 00000028 00000040 00000000 /files/chr/miz/0010.seq
00000001 00000025 00000040 00000000 /files/chr/miz/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/na9/0000.seq
00000007 00000028 00000040 00000000 /files/chr/na9/0010.seq
00000001 0000002d 00000040 00000000 /files/chr/na9/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/nar/0000.seq
00000007 00000028 00000040 00000000 /files/chr/nar/0010.seq
00000001 0000002e 00000040 00000000 /files/chr/nar/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/nej/0000.seq
00000007 00000028 00000040 00000000 /files/chr/nej/0010.seq
00000001 0000002b 00000040 00000000 /files/chr/nej/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/obo/0000.seq
00000007 00000028 00000040 00000000 /files/chr/obo/0010.seq
00000001 00000025 00000040 00000000 /files/chr/obo/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/oro/0000.seq
00000007 00000028 00000040 00000000 /files/chr/oro/0010.seq
00000001 00000029 00000040 00000000 /files/chr/oro/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/sa2/0000.seq
00000007 00000028 00000040 00000000 /files/chr/sa2/0010.seq
00000001 00000029 00000040 00000000 /files/chr/sa2/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/sak/0000.seq
00000007 00000028 00000040 00000000 /files/chr/sak/0010.seq
00000001 00000027 00000040 00000000 /files/chr/sak/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/sar/0000.seq
00000007 00000028 00000040 00000000 /files/chr/sar/0010.seq
00000001 00000028 00000040 00000000 /files/chr/sar/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/sas/0000.seq
00000007 00000028 00000040 00000000 /files/chr/sas/0010.seq
00000001 0000002b 00000040 00000000 /files/chr/sas/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/sik/0000.seq
00000007 00000028 00000040 00000000 /files/chr/sik/0010.seq
00000001 00000025 00000040 00000000 /files/chr/sik/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/sin/0000.seq
00000007 00000028 00000040 00000000 /files/chr/sin/0010.seq
00000001 00000026 00000040 00000000 /files/chr/sin/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/sko/0000.seq
00000007 00000028 00000040 00000000 /files/chr/sko/0010.seq
00000001 0000002a 00000040 00000000 /files/chr/sko/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/ta2/0000.seq
00000007 00000028 00000040 00000000 /files/chr/ta2/0010.seq
00000001 00000025 00000040 00000000 /files/chr/ta2/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/tay/0000.seq
00000007 00000028 00000040 00000000 /files/chr/tay/0010.seq
00000001 00000028 00000040 00000000 /files/chr/tay/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/tem/0000.seq
00000007 00000028 00000040 00000000 /files/chr/tem/0010.seq
00000001 00000028 00000040 00000000 /files/chr/tem/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/ten/0000.seq
00000007 00000028 00000040 00000000 /files/chr/ten/0010.seq
00000001 00000026 00000040 00000000 /files/chr/ten/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/tsu/0000.seq
00000007 00000028 00000040 00000000 /files/chr/tsu/0010.seq
00000001 0000002d 00000040 00000000 /files/chr/tsu/1000.seq
00000011 00000a48 00000040 00000000 /files/chr/zab/0000.seq
00000007 00000028 00000040 00000000 /files/chr/zab/0010.seq
00000001 00000025 00000040 00000000 /files/chr/zab/1000.seq
00000002 000001b0 00000040 00000000 /files/furu/f_camera.seq
00000002 000001a0 00000040 00000000 /files/game/camera00.seq
00000002 000001a0 00000040 00000000 /files/game/camera01.seq
00000006 0000006c 00000040 00000000 /files/game/game00.seq
00000010 00000020 00000020 00000000 /files/game/m_entry.seq
0000000c 00000040 00000040 00000000 /files/game/m_vs.seq
00000001 00000010 00000010 00000000 /files/game/player00.seq
00000006 00000040 00000040 00000000 /files/kuro/button.seq
0000000e 00000040 00000040 00000000 /files/kuro/loading.seq
00000001 00000010 00000010 00000000 /files/kuro/tmode.seq
0000000c 00000040 00000040 00000000 /files/maki/charsel4.seq
00000008 00000040 00000040 00000000 /files/maki/char_sel.seq
00000008 00000040 00000040 00000000 /files/maki/m_gal.seq
00000005 00000040 00000040 00000000 /files/maki/m_nfile.seq
00000006 00000040 00000040 00000000 /files/maki/m_nsiki.seq
00000007 00000040 00000040 00000000 /files/maki/m_sndplr.seq
0000001f 00000040 00000040 00000000 /files/maki/m_title.seq
00000008 00000040 00000040 00000000 /files/maki/m_viewer.seq
00000008 0000006c 00000020 00000000 /files/stg/001/0000.seq
00000004 00000040 00000020 00000000 /files/stg/001/0100.seq
00000009 0000006c 00000020 00000000 /files/stg/002/0000.seq
00000004 00000040 00000020 00000000 /files/stg/002/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/003/0000.seq
00000004 00000040 00000020 00000000 /files/stg/003/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/004/0000.seq
00000004 00000040 00000020 00000000 /files/stg/004/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/005/0000.seq
00000004 00000040 00000020 00000000 /files/stg/005/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/006/0000.seq
00000004 00000040 00000020 00000000 /files/stg/006/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/007/0000.seq
00000004 00000040 00000020 00000000 /files/stg/007/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/008/0000.seq
00000004 00000040 00000020 00000000 /files/stg/008/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/009/0000.seq
00000004 00000040 00000020 00000000 /files/stg/009/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/010/0000.seq
00000004 00000040 00000020 00000000 /files/stg/010/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/011/0000.seq
00000004 00000040 00000020 00000000 /files/stg/011/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/012/0000.seq
00000004 00000040 00000020 00000000 /files/stg/012/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/013/0000.seq
00000004 00000040 00000020 00000000 /files/stg/013/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/014/0000.seq
00000004 00000040 00000020 00000000 /files/stg/014/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/015/0000.seq
00000004 00000040 00000020 00000000 /files/stg/015/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/016/0000.seq
00000004 00000040 00000020 00000000 /files/stg/016/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/017/0000.seq
00000004 00000040 00000020 00000000 /files/stg/017/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/019/0000.seq
00000005 00000040 00000020 00000000 /files/stg/019/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/020/0000.seq
00000004 00000040 00000020 00000000 /files/stg/020/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/021/0000.seq
00000004 00000040 00000020 00000000 /files/stg/021/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/022/0000.seq
00000004 00000040 00000020 00000000 /files/stg/022/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/023/0000.seq
00000004 00000040 00000020 00000000 /files/stg/023/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/024/0000.seq
00000004 00000040 00000020 00000000 /files/stg/024/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/025/0000.seq
00000004 00000040 00000020 00000000 /files/stg/025/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/026/0000.seq
00000004 00000040 00000020 00000000 /files/stg/026/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/027/0000.seq
00000004 00000040 00000020 00000000 /files/stg/027/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/028/0000.seq
00000004 00000040 00000020 00000000 /files/stg/028/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/029/0000.seq
00000004 00000040 00000020 00000000 /files/stg/029/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/030/0000.seq
00000004 00000040 00000020 00000000 /files/stg/030/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/031/0000.seq
00000004 00000040 00000020 00000000 /files/stg/031/0100.seq
00000008 0000006c 00000020 00000000 /files/stg/032/0000.seq
00000004 00000040 00000020 00000000 /files/stg/032/0100.seq
00000016 00000040 00000040 00000000 /files/story/s00.seq
00000016 00000040 00000040 00000000 /files/story/s01.seq
00000016 00000040 00000040 00000000 /files/story/s02.seq
00000016 00000040 00000040 00000000 /files/story/s03.seq
00000016 00000040 00000040 00000000 /files/story/s04.seq
00000016 00000040 00000040 00000000 /files/story/s05.seq
00000016 00000040 00000040 00000000 /files/story/s06.seq
00000016 00000040 00000040 00000000 /files/story/s07.seq
00000016 00000040 00000040 00000000 /files/story/s08.seq
00000016 00000040 00000040 00000000 /files/story/s09.seq
00000016 00000040 00000040 00000000 /files/story/s0e.seq
00000016 00000040 00000040 00000000 /files/story/s10.seq
00000016 00000040 00000040 00000000 /files/story/s11.seq
00000016 00000040 00000040 00000000 /files/story/s12.seq
00000016 00000040 00000040 00000000 /files/story/s13.seq
00000016 00000040 00000040 00000000 /files/story/s14.seq
00000016 00000040 00000040 00000000 /files/story/s15.seq
00000016 00000040 00000040 00000000 /files/story/s16.seq
00000016 00000040 00000040 00000000 /files/story/s17.seq
00000016 00000040 00000040 00000000 /files/story/s18.seq
00000016 00000040 00000040 00000000 /files/story/s19.seq
00000016 00000040 00000040 00000000 /files/story/s1e.seq
00000016 00000040 00000040 00000000 /files/story/s20.seq
00000016 00000040 00000040 00000000 /files/story/s21.seq
00000016 00000040 00000040 00000000 /files/story/s22.seq
00000016 00000040 00000040 00000000 /files/story/s23.seq
00000016 00000040 00000040 00000000 /files/story/s24.seq
```

</details>

## SEQ Initialization

Before it is used, a SEQ file will first be initialized. This calls the function at 0x80099388 I call `seq_init()`. It takes three arguments.

1. The String of the SEQ file to be read, without the .seq extension. e.g. `"maki/charsel4"`
2. An unknown integer used during initialization of the seq initialization struct.
3. An unused value. Likely used during development.

This function will read the header and initialize a struct based on it.

<details>
  <summary>seq_init_struct</summary>

```psuedocode
seq_init_struct[0x0] = 0
seq_init_struct[0x1] = 0 (appears to have originally been used for something is no longer used)
seq_init_struct[0x2] = (SEQ Header Word 2) + (((SEQ Header Word 1 + 1) * 0x60) >> 2) + SEQ Header Word 1
seq_init_struct[0x3] = 0
seq_init_struct[0x4] = SEQ Header Word 1 + 1;
seq_init_struct[0x5] = SEQ Header Word 2
seq_init_struct[0x6] = SEQ Header Word 3
seq_init_struct[0x7] = Pointer made using 80222ba8 and seq_init_struct[0x2]
seq_init_struct[0x8] = seq_init_struct[7] + seq_init_struct[4] * 0x60
seq_init_struct[0x9] = seq_init_struct[8] + seq_init_struct[5] * 4
seq_init_struct[0xA] = pointer to something related to the file extension
seq_init_struct[0xb] = pointer to beginning of seq file data
seq_init_struct[0xc] = 0
seq_init_struct[0xd] = 0
seq_init_struct[0xe] = 0
seq_init_struct[0xf] = 0
seq_init_struct[0x10] = 0
Many pointers appear to be set after this based on the number of SEQ Header Word 1 using numbers derived from SEQ Header Word 2 and 3
```

</details>

## Reading Opcodes

The opcode is read from the seq file at 0x800c9120. It uses the following function to find the pointer to code associated with it:

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

| Opcode | Offset | Code Pointer | Purpose                                          |
|--------|--------|--------------|--------------------------------------------------|
| 0x0    | 0x0    | 800A6068     |                                                  |
| 0x1    | 0x4    | 800A5698     | Branching                                        |
| 0x2    | 0x8    | 800A52F8     |                                                  |
| 0x3    | 0xc    | 800A51B0     |                                                  |
| 0x4    | 0x10   | 800A4B40     |                                                  |
| 0x5    | 0x14   | 800A44C4     |                                                  |
| 0x6    | 0x18   | 800A3ED4     |                                                  |
| 0x7    | 0x1c   | 800A3888     |                                                  |
| 0x8    | 0x20   | 800A32C0     |                                                  |
| 0x9    | 0x24   | 800A2A8C     |                                                  |
| 0xa    | 0x28   | 800A274C     |                                                  |
| 0xb    | 0x2c   | 800A1C5C     |                                                  |
| 0xc    | 0x30   | 800A1894     |                                                  |
| 0xd    | 0x34   | 800A188C     | Empty and unused                                 |
| 0xe    | 0x38   | 800AA9B8     |                                                  |
| 0xf    | 0x3c   | 800AA430     |                                                  |
| 0x10   | 0x40   | 800A9C1C     |                                                  |
| 0x11   | 0x44   | 800A99F0     |                                                  |
| 0x12   | 0x48   | 800A8E68     |                                                  |
| 0x13   | 0x4c   | 800A8594     |                                                  |
| 0x14   | 0x50   | 800A76EC     |                                                  |
| 0x15   | 0x54   | 800A75C0     |                                                  |
| 0x16   | 0x58   | 800A7204     |                                                  |
| 0x17   | 0x5c   | 800A713C     |                                                  |
| 0x18   | 0x60   | 800A7054     |                                                  |
| 0x19   | 0x64   | 800A6B1C     |                                                  |
| 0x1a   | 0x68   | 800A6458     |                                                  |
| 0x1b   | 0x6c   | 800A6324     |                                                  |
| 0x1c   | 0x70   | 800A6228     |                                                  |
| 0x1d   | 0x74   | 800BB7A0     |                                                  |
| 0x1e   | 0x78   | 800BB5F8     |                                                  |
| 0x1f   | 0x7c   | 800BB338     |                                                  |
| 0x20   | 0x80   | 800BA19C     |                                                  |
| 0x21   | 0x84   | 800B9458     |                                                  |
| 0x22   | 0x88   | 800B832C     |                                                  |
| 0x23   | 0x8c   | 800B7D98     |                                                  |
| 0x24   | 0x90   | 800B3EC4     |                                                  |
| 0x25   | 0x94   | 800B3CE4     |                                                  |
| 0x26   | 0x98   | 800C0288     |                                                  |
| 0x27   | 0x9c   | 800B097C     |                                                  |
| 0x28   | 0xa0   | 800B0320     |                                                  |
| 0x29   | 0xa4   | 800B214C     |                                                  |
| 0x2a   | 0xa8   | 800B1750     |                                                  |
| 0x2b   | 0xac   | 800B1590     |                                                  |
| 0x2c   | 0xb0   | 800B24B8     | Empty and unused                                 |
| 0x2d   | 0xb4   | 800B24B0     | Empty and unused                                 |
| 0x2e   | 0xb8   | 800B24A8     | Empty and unused                                 |
| 0x2f   | 0xbc   | 800B24A0     | Empty and unused                                 |
| 0x30   | 0xc0   | 800B2498     | Empty and unused                                 |
| 0x31   | 0xc4   | 800B3580     |                                                  |
| 0x32   | 0xc8   | 800B3020     |                                                  |
| 0x33   | 0xcc   | 800B25D0     |                                                  |
| 0x34   | 0xd0   | 800B24C0     |                                                  |
| 0x35   | 0xd4   | 00000000     | Invalid                                          |
| 0x36   | 0xd8   | 800960B4     |                                                  |
| 0x37   | 0xdc   | 800952F4     |                                                  |
| 0x38   | 0xe0   | 80094324     |                                                  |
| 0x39   | 0xe4   | 800924F0     |                                                  |
| 0x3a   | 0xe8   | 80091248     |                                                  |
| 0x3b   | 0xec   | 8009228C     |                                                  |
| 0x3c   | 0xf0   | 80091B8C     |                                                  |
| 0x3d   | 0xf4   | 800C6228     |                                                  |
| 0x3e   | 0xf8   | 80090EF8     |                                                  |
| 0x3f   | 0xfc   | 800C5EDC     |                                                  |
| 0x40   | 0x100  | 800C57BC     |                                                  |
| 0x41   | 0x104  | 800C531C     |                                                  |
| 0x42   | 0x108  | 800C5124     |                                                  |
| 0x43   | 0x10c  | 800C4FCC     |                                                  |
| 0x44   | 0x110  | 800C4688     |                                                  |
| 0x45   | 0x114  | 00000000     | Invalid                                          |
| 0x46   | 0x118  | 800C88A8     |                                                  |
| 0x47   | 0x11c  | 800C8404     |                                                  |
| 0x48   | 0x120  | 800C8108     |                                                  |
| 0x49   | 0x124  | 800C7D20     |                                                  |
| 0x4a   | 0x128  | 800C7C5C     |                                                  |
| 0x4b   | 0x12c  | 800C7424     |                                                  |
| 0x4c   | 0x130  | 800C6900     |                                                  |
| 0x4d   | 0x134  | 800C676C     |                                                  |
| 0x4e   | 0x138  | 00000000     | Invalid                                          |
| 0x4f   | 0x13c  | 00000000     | Invalid                                          |
| 0x50   | 0x140  | 800C6534     |                                                  |
| 0x51   | 0x144  | 00000000     | Invalid                                          |
| 0x52   | 0x148  | 00000000     | Invalid                                          |
| 0x53   | 0x14c  | 00000000     | Invalid                                          |
| 0x54   | 0x150  | 00000000     | Invalid                                          |
| 0x55   | 0x154  | 800AAD24     |                                                  |
| 0x56   | 0x158  | 800AAC68     |                                                  |
| 0x57   | 0x15c  | 00000000     | Invalid                                          |
| 0x58   | 0x160  | 00000000     | Invalid                                          |
| 0x59   | 0x164  | 00000000     | Invalid                                          |
| 0x5a   | 0x168  | 00000000     | Invalid                                          |
| 0x5b   | 0x16c  | 800BFBB0     |                                                  |
| 0x5c   | 0x170  | 800BE9EC     |                                                  |
| 0x5d   | 0x174  | 00000000     | Invalid                                          |
| 0x5e   | 0x178  | 00000000     | Invalid                                          |
| 0x5f   | 0x17c  | 00000000     | Invalid                                          |
| 0x60   | 0x180  | 00000000     | Invalid                                          |
| 0x61   | 0x184  | 800AB754     |                                                  |
| 0x62   | 0x188  | 00000000     | Invalid                                          |
| 0x63   | 0x18c  | 00000000     | Invalid                                          |
| 0x64   | 0x190  | 00000000     | Invalid                                          |
| 0x65   | 0x194  | 800C97B0     | None of the opcodes from here on are valid       |
| 0x66   | 0x198  | 800C9858     | Invalid                                          |
| 0x67   | 0x19c  | 800C97C0     | Invalid                                          |
| 0x68   | 0x1a0  | 800C97D0     | Invalid                                          |
| 0x69   | 0x1a4  | 800C97E0     | Invalid                                          |
| 0x6a   | 0x1a8  | 800C9858     | Invalid                                          |
| 0x6b   | 0x1ac  | 800C9858     | Invalid                                          |
| 0x6c   | 0x1b0  | 800C9858     | Invalid                                          |
| 0x6d   | 0x1b4  | 800C9858     | Invalid                                          |
| 0x6e   | 0x1b8  | 800C97F0     | Invalid                                          |
| 0x6f   | 0x1bc  | 800C9800     | Invalid                                          |
| 0x70   | 0x1c0  | 800C9810     | Invalid                                          |
| 0x71   | 0x1c4  | 800C9820     | Invalid                                          |
| 0x72   | 0x1c8  | 800C9830     | Invalid                                          |
| 0x73   | 0x1cc  | 800C9840     | Invalid                                          |
| 0x74   | 0x1d0  | 800C9850     | Invalid                                          |
| 0x75   | 0x1d4  | 00000000     | Invalid                                          |
| 0x76   | 0x1d8  | 80201EC8     | Invalid                                          |
| 0x77   | 0x1dc  | 80201ED8     | Invalid                                          |
| 0x78   | 0x1e0  | 80201EEC     | Invalid                                          |
| 0x79   | 0x1e4  | 80201F00     | Invalid                                          |
| 0x7a   | 0x1e8  | 800CE908     | Invalid                                          |
| 0x7b   | 0x1ec  | 800CE808     | Invalid                                          |
| 0x7c   | 0x1f0  | 800CE810     | Invalid                                          |
| 0x7d   | 0x1f4  | 800CE818     | Invalid                                          |
| 0x7e   | 0x1f8  | 800CE820     | Invalid                                          |
| 0x7f   | 0x1fc  | 800CE828     | Invalid                                          |
| 0x80   | 0x200  | 800CE830     | Invalid                                          |
| 0x81   | 0x204  | 800CE838     | Invalid                                          |
| 0x82   | 0x208  | 800CE840     | Invalid                                          |
| 0x83   | 0x20c  | 800CE848     | Invalid                                          |
| 0x84   | 0x210  | 800CE850     | Invalid                                          |
| 0x85   | 0x214  | 800CE858     | Invalid                                          |
| 0x86   | 0x218  | 800CE860     | Invalid                                          |
| 0x87   | 0x21c  | 800CE868     | Invalid                                          |
| 0x88   | 0x220  | 800CE870     | Invalid                                          |
| 0x89   | 0x224  | 800CE878     | Invalid                                          |
| 0x8a   | 0x228  | 800CE880     | Invalid                                          |
| 0x8b   | 0x22c  | 800CE888     | Invalid                                          |
| 0x8c   | 0x230  | 800CE890     | Invalid                                          |
| 0x8d   | 0x234  | 800CE898     | Invalid                                          |
| 0x8e   | 0x238  | 800CE8A0     | Invalid                                          |
| 0x8f   | 0x23c  | 800CE8A8     | Invalid                                          |
| 0x90   | 0x240  | 800CE8B0     | Invalid                                          |
| 0x91   | 0x244  | 800CE8B8     | Invalid                                          |
| 0x92   | 0x248  | 800CE8C0     | Invalid                                          |
| 0x93   | 0x24c  | 800CE8C8     | Invalid                                          |
| 0x94   | 0x250  | 800CE8D0     | Invalid                                          |
| 0x95   | 0x254  | 800CE8D8     | Invalid                                          |
| 0x96   | 0x258  | 800CE8E0     | Invalid                                          |
| 0x97   | 0x25c  | 800CE8E8     | Invalid                                          |
| 0x98   | 0x260  | 800CE8F0     | Invalid                                          |
| 0x99   | 0x264  | 800CE8F8     | Invalid                                          |
| 0x9a   | 0x268  | 800CE900     | Invalid                                          |
| 0x9b   | 0x26c  | 800CE980     | Invalid                                          |
| 0x9c   | 0x270  | 800CEB08     | Invalid                                          |
| 0x9d   | 0x274  | 800CEB08     | Invalid                                          |
| 0x9e   | 0x278  | 800CE9DC     | Invalid                                          |
| 0x9f   | 0x27c  | 800CEB08     | Invalid                                          |
| 0xa0   | 0x280  | 800CEB08     | Invalid                                          |
| 0xa1   | 0x284  | 800CEB08     | Invalid                                          |
| 0xa2   | 0x288  | 800CEB08     | Invalid                                          |
| 0xa3   | 0x28c  | 800CE9F8     | Invalid                                          |
| 0xa4   | 0x290  | 800CEA54     | Invalid                                          |
| 0xa5   | 0x294  | 800CEAB0     | Invalid                                          |
| 0xa6   | 0x298  | 800CEEF8     | Invalid                                          |
| 0xa7   | 0x29c  | 800CEF08     | Invalid                                          |
| 0xa8   | 0x2a0  | 800CEF18     | Invalid                                          |
| 0xa9   | 0x2a4  | 800CEF24     | Invalid                                          |
| 0xaa   | 0x2a8  | 800CEF30     | Invalid                                          |
| 0xab   | 0x2ac  | 800CEF3C     | Invalid                                          |
| 0xac   | 0x2b0  | 800CEF4C     | Invalid                                          |
| 0xad   | 0x2b4  | 800CEF58     | Invalid                                          |
| 0xae   | 0x2b8  | 800CEF64     | Invalid                                          |
| 0xaf   | 0x2bc  | 800CEF70     | Invalid                                          |
| 0xb0   | 0x2c0  | 800CEF80     | Invalid                                          |
| 0xb1   | 0x2c4  | 800CEF90     | Invalid                                          |
| 0xb2   | 0x2c8  | 800CEFA0     | Invalid                                          |
| 0xb3   | 0x2cc  | 800CEFB0     | Invalid                                          |
| 0xb4   | 0x2d0  | 800CEFC0     | Invalid                                          |
| 0xb5   | 0x2d4  | 800CEFD0     | Invalid                                          |
| 0xb6   | 0x2d8  | 800CEFE0     | Invalid                                          |
| 0xb7   | 0x2dc  | 800CEFF0     | Invalid                                          |
| 0xb8   | 0x2e0  | 800CF000     | Invalid                                          |
| 0xb9   | 0x2e4  | 800CF010     | Invalid                                          |
| 0xba   | 0x2e8  | 800CF020     | Invalid                                          |
| 0xbb   | 0x2ec  | 800CF02C     | Invalid                                          |
| 0xbc   | 0x2f0  | 800CF25C     | Invalid                                          |
| 0xbd   | 0x2f4  | 800CF25C     | Invalid                                          |
| 0xbe   | 0x2f8  | 800CF25C     | Invalid                                          |
| 0xbf   | 0x2fc  | 800CF25C     | Invalid                                          |
| 0xc0   | 0x300  | 800CF25C     | Invalid                                          |
| 0xc1   | 0x304  | 800CF25C     | Invalid                                          |
| 0xc2   | 0x308  | 800CF25C     | Invalid                                          |
| 0xc3   | 0x30c  | 800CF25C     | Invalid                                          |
| 0xc4   | 0x310  | 800CF25C     | Invalid                                          |
| 0xc5   | 0x314  | 800CF25C     | Invalid                                          |
| 0xc6   | 0x318  | 800CF25C     | Invalid                                          |
| 0xc7   | 0x31c  | 800CF25C     | Invalid                                          |
| 0xc8   | 0x320  | 800CF25C     | Invalid                                          |
| 0xc9   | 0x324  | 800CF25C     | Invalid                                          |
| 0xca   | 0x328  | 800CF25C     | Invalid                                          |
| 0xcb   | 0x32c  | 800CF25C     | Invalid                                          |
| 0xcc   | 0x330  | 800CF25C     | Invalid                                          |
| 0xcd   | 0x334  | 800CF25C     | Invalid                                          |
| 0xce   | 0x338  | 800CF038     | Invalid                                          |
| 0xcf   | 0x33c  | 800CF048     | Invalid                                          |
| 0xd0   | 0x340  | 800CF058     | Invalid                                          |
| 0xd1   | 0x344  | 800CF068     | Invalid                                          |
| 0xd2   | 0x348  | 800CF078     | Invalid                                          |
| 0xd3   | 0x34c  | 800CF088     | Invalid                                          |
| 0xd4   | 0x350  | 800CF098     | Invalid                                          |
| 0xd5   | 0x354  | 800CF0A8     | Invalid                                          |
| 0xd6   | 0x358  | 800CF0B8     | Invalid                                          |
| 0xd7   | 0x35c  | 800CF0C8     | Invalid                                          |
| 0xd8   | 0x360  | 800CF0D8     | Invalid                                          |
| 0xd9   | 0x364  | 800CF0E8     | Invalid                                          |
| 0xda   | 0x368  | 800CF0F8     | Invalid                                          |
| 0xdb   | 0x36c  | 800CF108     | Invalid                                          |
| 0xdc   | 0x370  | 800CF118     | Invalid                                          |
| 0xdd   | 0x374  | 800CF128     | Invalid                                          |
| 0xde   | 0x378  | 800CF138     | Invalid                                          |
| 0xdf   | 0x37c  | 800CF148     | Invalid                                          |
| 0xe0   | 0x380  | 800CF158     | Invalid                                          |
| 0xe1   | 0x384  | 800CF168     | Invalid                                          |
| 0xe2   | 0x388  | 800CF178     | Invalid                                          |
| 0xe3   | 0x38c  | 800CF188     | Invalid                                          |
| 0xe4   | 0x390  | 800CF198     | Invalid                                          |
| 0xe5   | 0x394  | 800CF1A8     | Invalid                                          |
| 0xe6   | 0x398  | 800CF1B8     | Invalid                                          |
| 0xe7   | 0x39c  | 800CF1C8     | Invalid                                          |
| 0xe8   | 0x3a0  | 800CF1D8     | Invalid                                          |
| 0xe9   | 0x3a4  | 800CF1E8     | Invalid                                          |
| 0xea   | 0x3a8  | 800CF1F8     | Invalid                                          |
| 0xeb   | 0x3ac  | 800CF208     | Invalid                                          |
| 0xec   | 0x3b0  | 800CF218     | Invalid                                          |
| 0xed   | 0x3b4  | 800CF228     | Invalid                                          |
| 0xee   | 0x3b8  | 800CF25C     | Invalid                                          |
| 0xef   | 0x3bc  | 800CF25C     | Invalid                                          |
| 0xf0   | 0x3c0  | 800CF25C     | Invalid                                          |
| 0xf1   | 0x3c4  | 800CF25C     | Invalid                                          |
| 0xf2   | 0x3c8  | 800CF25C     | Invalid                                          |
| 0xf3   | 0x3cc  | 800CF25C     | Invalid                                          |
| 0xf4   | 0x3d0  | 800CF25C     | Invalid                                          |
| 0xf5   | 0x3d4  | 800CF25C     | Invalid                                          |
| 0xf6   | 0x3d8  | 800CF238     | Invalid                                          |
| 0xf7   | 0x3dc  | 800CF244     | Invalid                                          |
| 0xf8   | 0x3e0  | 800CF250     | Invalid                                          |
| 0xf9   | 0x3e4  | 800CFDA4     | Invalid                                          |
| 0xfa   | 0x3e8  | 800CFA84     | Invalid                                          |
| 0xfb   | 0x3ec  | 800CFA98     | Invalid                                          |
| 0xfc   | 0x3f0  | 800CFAAC     | Invalid                                          |
| 0xfd   | 0x3f4  | 800CFAC0     | Invalid                                          |
| 0xfe   | 0x3f8  | 800CFAD4     | Invalid                                          |
| 0xff   | 0x3fc  | 800CFAE8     | Invalid                                          |

</details>

It will then jump to the code found in the opcode pointer table. When we jump to `0x800a5698`, it then checks the second byte of the opcode. This second byte further breaks down the action to be performed.

## Branching Opcodes

- X = param_2[0x15]
- Y = param_2[0x14]
- Z = param_2[0x17] (is a pointer)

In the below table, Params is the number of bytes after the opcode used for parameters.

<details>
  <summary>Branching Opcodes</summary>

| Opcode | Params | Description                                                                                                                        |
|--------|--------|------------------------------------------------------------------------------------------------------------------------------------|
| 0100   | 4      | ???                                                                                                                                |
| 0101   | ?      | ???                                                                                                                                |
| 0102   | 4      | ???                                                                                                                                |
| 0103   | ?      | ???                                                                                                                                |
| 0104   | 0      | ???                                                                                                                                |
| 0105   | ?      | ???                                                                                                                                |
| 0106   | 0      | ???                                                                                                                                |
| 0107   | ?      | ???                                                                                                                                |
| 0108   | 0      | ???                                                                                                                                |
| 0132   | 4      | Unconditional branch.                                                                                                              |
| 0133   | 4      | Branch if X is 0.                                                                                                                  |
| 0134   | 4      | Branch if X is not 0.                                                                                                              |
| 0135   | 4      | Branch is X is 1 or greater.                                                                                                       |
| 0136   | 4      | Branch if X is 0 or greater.                                                                                                       |
| 0137   | 4      | Branch if X is less than 0.                                                                                                        |
| 0138   | 4      | Branch if X is less than 1.                                                                                                        |
| 0139   | 4      | Branch if X is less than 0 (Duplicate of 0137).                                                                                    |
| 013A   | 4      | Branch if X is 0 or greater (Duplicate of 0136).                                                                                   |
| 013B   | 4      | Branch if Y is less than 0. Otherwise, decrement Y and if Y is then not 0, branch.                                                 |
| 013C   | 4      | Subtract 4 from Z. Using the pointer Z is holding, set it to the offset of the opcode after the current one. Unconditional branch. |
| 013D   | 4      | Execute opcode 013C if X is 0.                                                                                                     |
| 013E   | 4      | Execute opcode 013C if X is not 0.                                                                                                 |
| 013F   | 4      | Execute opcode 013C if X is 1 or greater.                                                                                          |
| 0140   | 4      | Execute opcode 013C if X is 0 or greater.                                                                                          |
| 0141   | 4      | Execute opcode 013C if X is less than 0.                                                                                           |
| 0142   | 4      | Execute opcode 013C if X is less than 1.                                                                                           |
| 0143   | 4      | Execute opcode 013C if X is less than 0 (Duplicate of 0141).                                                                       |
| 0144   | 4      | Execute opcode 013C if X is 0 or greater (Duplicate of 0140).                                                                      |
| 0145   | 0      | Unconditional branch to the deferenced pointer of Z. Increment Z by 4.                                                             |
| 0146   | 0      | Execute opcode 0145 if X is 0.                                                                                                     |
| 0147   | 0      | Execute opcode 0145 if X is not 0.                                                                                                 |
| 0148   | 0      | Execute opcode 0145 if X is 1 or greater.                                                                                          |
| 0149   | 0      | Execute opcode 0145 if X is 0 or greater.                                                                                          |
| 014A   | 0      | Execute opcode 0145 if X is less than 0.                                                                                           |
| 014B   | 0      | Execute opcode 0145 if X is less than 1.                                                                                           |
| 014C   | 0      | Execute opcode 0145 if X is less than 0 (Duplicate of 014A).                                                                       |
| 014D   | 0      | Execute opcode 0145 if X is 0 or greater (Duplicate of 0149).                                                                      |
| 014E   | ?      | ???                                                                                                                                |
| 014F   | 0      | Execute opcode 0145 if Y is less than 0. Otherwise, decrement Y and if Y is then not 0, execute opcode 0145.                       |
| 0150   | varies | ???                                                                                                                                |
| 0151   | varies | ???                                                                                                                                |

</details>
