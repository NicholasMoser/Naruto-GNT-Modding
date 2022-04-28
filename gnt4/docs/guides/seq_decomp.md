# SEQ Decompilation

This page includes information regarding the decompilation of the SEQ format and how it is parsed.

## SEQ Header

The file begins with a 16 byte header. Only the first three four-byte words are used. The last four bytes are always zero. The values of each word used by SEQ files in the game are:

<details>
  <summary>First word</summary>

Appears to be used to determine the number of register groups needed. For more info see [Opcode Method Parameters](#opcode-method-parameters)

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

Opcodes are read from the seq file in the seq_parse method. Each full opcode is four bytes long. The first byte defines the opcode group and the second byte defines the opcode within that opcode group to use. The third and fourth byte may be used to additionally configure the full opcode.

Each opcode will jump to code in the game to execute. It uses the following function to find the code to execute:

```c
// Find the opcode group method
0x802103a0 + (opcode >> 0x16 & 0x3fc)
```

By bit shifting by 0x16, it multiplies the top byte by four. This is because each pointer is four bytes long, so we need the opcode group index multiplied by four. It is &'d with 0x3fc (`001111111100` in binary) in order to force it to be a multiple of four.

So for example:

1. Read opcode, e.g. `0x01320000` (`00000001001100100000000000000000` in binary)
2. Use bit shifting to get the top 10 bits, the binary `0000000100` in this case.
3. & it with `0x3fc` (`001111111100` in binary)
4. For this example, that doesn't change the value and it stays as `100` in binary, or 4 in hex.
5. This value is added as an offset to `0x802103a0`, which is a location to a pointer table in memory.
6. For this example, we get the final value `0x800a5698`, which is the second pointer in the opcode pointer table.

The highest value that can come from this math is `0x3fc`, so the opcode pointer table is between `0x802103a0` and `0x8021079C`

<details>
  <summary>Opcode Pointer Table</summary>

| Opcode | Offset | Code Pointer | Purpose                                          |
|--------|--------|--------------|--------------------------------------------------|
| 0x0    | 0x0    | 800A6068     | SEQ_CmdSEQ1                                      |
| 0x1    | 0x4    | 800A5698     | SEQ_CmdSEQ2                                      |
| 0x2    | 0x8    | 800A52F8     | SEQ_CmdTSK                                       |
| 0x3    | 0xc    | 800A51B0     | SEQ_CmdREG                                       |
| 0x4    | 0x10   | 800A4B40     | SEQ_CmdI                                         |
| 0x5    | 0x14   | 800A44C4     | SEQ_CmdIC                                        |
| 0x6    | 0x18   | 800A3ED4     | SEQ_CmdIS                                        |
| 0x7    | 0x1c   | 800A3888     | SEQ_CmdIL                                        |
| 0x8    | 0x20   | 800A32C0     | SEQ_CmdF                                         |
| 0x9    | 0x24   | 800A2A8C     | SEQ_CmdP                                         |
| 0xa    | 0x28   | 800A274C     | SEQ_CmdIV                                        |
| 0xb    | 0x2c   | 800A1C5C     | SEQ_CmdFV                                        |
| 0xc    | 0x30   | 800A1894     | SEQ_CmdFM                                        |
| 0xd    | 0x34   | 800A188C     | SEQ_CmdRGB                                       |
| 0xe    | 0x38   | 800AA9B8     | SEQ_CmdMEM                                       |
| 0xf    | 0x3c   | 800AA430     | SEQ_CmdFILE                                      |
| 0x10   | 0x40   | 800A9C1C     | SEQ_CmdGOBJ                                      |
| 0x11   | 0x44   | 800A99F0     | SEQ_CmdOBJ                                       |
| 0x12   | 0x48   | 800A8E68     |                                                  |
| 0x13   | 0x4c   | 800A8594     |                                                  |
| 0x14   | 0x50   | 800A76EC     |                                                  |
| 0x15   | 0x54   | 800A75C0     | SEQ_CmdPAUSE                                     |
| 0x16   | 0x58   | 800A7204     | Sounds                                           |
| 0x17   | 0x5c   | 800A713C     |                                                  |
| 0x18   | 0x60   | 800A7054     |                                                  |
| 0x19   | 0x64   | 800A6B1C     | SEQ_CmdPRT                                       |
| 0x1a   | 0x68   | 800A6458     | Call HSD functions                               |
| 0x1b   | 0x6c   | 800A6324     |                                                  |
| 0x1c   | 0x70   | 800A6228     |                                                  |
| 0x1d   | 0x74   | 800BB7A0     |                                                  |
| 0x1e   | 0x78   | 800BB5F8     |                                                  |
| 0x1f   | 0x7c   | 800BB338     |                                                  |
| 0x20   | 0x80   | 800BA19C     |                                                  |
| 0x21   | 0x84   | 800B9458     |                                                  |
| 0x22   | 0x88   | 800B832C     |                                                  |
| 0x23   | 0x8c   | 800B7D98     |                                                  |
| 0x24   | 0x90   | 800B3EC4     | Battle related                                   |
| 0x25   | 0x94   | 800B3CE4     |                                                  |
| 0x26   | 0x98   | 800C0288     |                                                  |
| 0x27   | 0x9c   | 800B097C     |                                                  |
| 0x28   | 0xa0   | 800B0320     |                                                  |
| 0x29   | 0xa4   | 800B214C     |                                                  |
| 0x2a   | 0xa8   | 800B1750     |                                                  |
| 0x2b   | 0xac   | 800B1590     | Particles                                        |
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
| 0x3c   | 0xf0   | 80091B8C     | Menu logic                                       |
| 0x3d   | 0xf4   | 800C6228     |                                                  |
| 0x3e   | 0xf8   | 80090EF8     |                                                  |
| 0x3f   | 0xfc   | 800C5EDC     |                                                  |
| 0x40   | 0x100  | 800C57BC     |                                                  |
| 0x41   | 0x104  | 800C531C     |                                                  |
| 0x42   | 0x108  | 800C5124     |                                                  |
| 0x43   | 0x10c  | 800C4FCC     |                                                  |
| 0x44   | 0x110  | 800C4688     | Save data                                        |
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

</details>

It will then jump to the code found in the opcode pointer table. When we jump to `0x800a5698`, it then checks the second byte of the opcode. This second byte further breaks down the action to be performed.

## Opcode Groups

There are 82 total opcode groups. 6 of the groups are empty (resulting in a no-op), leaving 76 with actual instructions in them. The number of instructions in each group varies. Each instruction for each opcode group can be found in the respective pages below for each opcode group.

<details>
  <summary>Opcode Group Pages</summary>

- [Group 00: SEQ_CmdSEQ1](opcode_group/00.md)
- [Group 01: SEQ_CmdSEQ2](opcode_group/01.md)
- [Group 02: SEQ_CmdTSK](opcode_group/02.md)
- [Group 03: SEQ_CmdREG](opcode_group/03.md)
- [Group 04: SEQ_CmdI](opcode_group/04.md)
- [Group 05: SEQ_CmdIC](opcode_group/05.md)
- [Group 06: SEQ_CmdIS](opcode_group/06.md)
- [Group 07: SEQ_CmdIL](opcode_group/07.md)
- [Group 08: SEQ_CmdF](opcode_group/08.md)
- [Group 09: SEQ_CmdP](opcode_group/09.md)
- [Group 0A: SEQ_CmdIV](opcode_group/0A.md)
- [Group 0B: SEQ_CmdFV](opcode_group/0B.md)
- [Group 0C: SEQ_CmdFM](opcode_group/0C.md)
- [Group 0D: SEQ_CmdRGB](opcode_group/0D.md)
- [Group 0E: SEQ_CmdMEM](opcode_group/0E.md)
- [Group 0F: SEQ_CmdFILE](opcode_group/0F.md)
- [Group 10](opcode_group/10.md)
- [Group 11: SEQ_CmdOBJ](opcode_group/11.md)
- [Group 12](opcode_group/12.md)
- [Group 13](opcode_group/13.md)
- [Group 14: SEQ_CmdHIT](opcode_group/14.md)
- [Group 15: SEQ_CmdPAUSE](opcode_group/15.md)
- [Group 16](opcode_group/16.md)
- [Group 17](opcode_group/17.md)
- [Group 18](opcode_group/18.md)
- [Group 19](opcode_group/19.md)
- [Group 1A](opcode_group/1A.md)
- [Group 1B](opcode_group/1B.md)
- [Group 1C](opcode_group/1C.md)
- [Group 1E](opcode_group/1E.md)
- [Group 1F](opcode_group/1F.md)
- [Group 20](opcode_group/20.md)
- [Group 21](opcode_group/21.md)
- [Group 22](opcode_group/22.md)
- [Group 23](opcode_group/23.md)
- [Group 24](opcode_group/24.md)
- [Group 25](opcode_group/25.md)
- [Group 26](opcode_group/26.md)
- [Group 27](opcode_group/27.md)
- [Group 28](opcode_group/28.md)
- [Group 29](opcode_group/29.md)
- [Group 2A](opcode_group/2A.md)
- [Group 2B](opcode_group/2B.md)
- [Group 31](opcode_group/31.md)
- [Group 32](opcode_group/32.md)
- [Group 33](opcode_group/33.md)
- [Group 34](opcode_group/34.md)
- [Group 36](opcode_group/36.md)
- [Group 37](opcode_group/37.md)
- [Group 38](opcode_group/38.md)
- [Group 39](opcode_group/39.md)
- [Group 3A](opcode_group/3A.md)
- [Group 3B](opcode_group/3B.md)
- [Group 3C](opcode_group/3C.md)
- [Group 3D](opcode_group/3D.md)
- [Group 3E](opcode_group/3E.md)
- [Group 3F](opcode_group/3F.md)
- [Group 40](opcode_group/40.md)
- [Group 41](opcode_group/41.md)
- [Group 42](opcode_group/42.md)
- [Group 43](opcode_group/43.md)
- [Group 44](opcode_group/44.md)
- [Group 46](opcode_group/46.md)
- [Group 47](opcode_group/47.md)
- [Group 48](opcode_group/48.md)
- [Group 49](opcode_group/49.md)
- [Group 4A](opcode_group/4A.md)
- [Group 4B](opcode_group/4B.md)
- [Group 4C](opcode_group/4C.md)
- [Group 4D](opcode_group/4D.md)
- [Group 50](opcode_group/50.md)
- [Group 55](opcode_group/55.md)
- [Group 56](opcode_group/56.md)
- [Group 5B](opcode_group/5B.md)
- [Group 5C](opcode_group/5C.md)
- [Group 61](opcode_group/61.md)

</details>

## Opcode Method Parameters

Each opcode group method takes in three parameters, `seq_p`, `reg_p`, and `pc`. We know this is the case because opcode `02` in group `00` prints them out:

```c
sprintf("sys_bp(): seq_p%08x reg_p%08x pc%08x\n", seq_p, reg_p, pc);
```

### seq_p

The first parameter `seq_p` is a pointer to a variety of information related to the seq files being executed. One such example is the offset in memory to the start of the current seq file being executed.

seq_p->seq_p_sp is field 0x20 on seq_p, and seems to have lots of interesting data in it.

seq_p->seq_p_sp->field_0x1c = Battle frame count. Number of frames since the battle started.
seq_p->seq_p_sp->field_0x2c = Used in synchronous timers. How much to subtract from the timer per frame, seems to default to 0x100.
seq_p->seq_p_sp->field_0x38 = Pointer to this character's chr_p.
seq_p->seq_p_sp->field_0x3c = Pointer to the opposing character's chr_p.
seq_p->seq_p_sp->field_0x98->field_0x18 = Character index (player 1, player 2, player 3, player 4)?

### reg_p

The second parameter `reg_p` holds pointers to the registers used. There are 18 registers. Despite this, the size of it in appears to be the first four-byte word of the seq file plus 1 times 0x60.

```c
reg_p_size = (first_word + 1) * 0x60
```

So for example, `game00.seq` starts with `0x00000006`, so it will initialize a `reg_p` of size `0x2A0`.

### pc

The third parameter `pc` is a pointer to the current opcode being executed in the seq file. It will move from opcode to opcode and branch when told to. When set to 0 it will cease executing opcodes.

## Operand Names

- `op1` - The operand from `SEQ_RegCMD1` or the first operand from `SEQ_RegCMD2`.
- `op2` - The second operand from `SEQ_RegCMD2`.
- `varX` - An operand that follows after the opcode word, where X is the index (starting at 1).

## Known Values

The structs for `reg_p` seem to all be next to each other in memory.

- seq_p[5][0x17]: Memory address of the start of the current SEQ file.
- reg_p[0x00]: Possibly a general purpose register (`gpr0`).
- reg_p[0x01]: Possibly a general purpose register (`gpr1`).
- reg_p[0x02]: Possibly a general purpose register (`gpr2`).
- reg_p[0x03]: Possibly a general purpose register (`gpr3`).
- reg_p[0x04]: Possibly a general purpose register (`gpr4`).
- reg_p[0x05]: Possibly a general purpose register (`gpr5`).
- reg_p[0x06]: Possibly a general purpose register (`gpr6`).
- reg_p[0x07]: Possibly a general purpose register (`gpr7`).
- reg_p[0x08]: Possibly a general purpose register (`gpr8`).
- reg_p[0x09]: Possibly a general purpose register (`gpr9`).
- reg_p[0x0A]: Possibly a general purpose register (`gpr10`).
- reg_p[0x0B]: Possibly a general purpose register (`gpr11`).
- reg_p[0x0C]: Possibly a general purpose register (`gpr12`).
- reg_p[0x0D]: Possibly a general purpose register (`gpr13`).
- reg_p[0x0E]: Possibly a general purpose register (`gpr14`).
- reg_p[0x0F]: Possibly a general purpose register (`gpr15`).
- reg_p[0x10]: Possibly a general purpose register (`gpr16`).
- reg_p[0x11]: Possibly a general purpose register (`gpr17`).
- reg_p[0x12]: Possibly a general purpose register (`gpr18`).
- reg_p[0x13]: Currently unknown, appears to be used alongside the Condition Register (`cr`).
- reg_p[0x14]: Count Register (`ctr`). Holds a counter. Set by opcode 0402 (reg_p[0x15] also is set to this counter) and read/decremented by opcode 013B.
- reg_p[0x15]: Condition Register (`cr`). Holds values to be compared for branching. Set by opcode group 04 and compared in opcode group 01.
- reg_p[0x16]: Stored PC (`stored_pc`). Holds a program counter while the program counter is reset to zero. Set by opcode 0100 and 0101 and used in the function `seq_parse(...)`. Reset by opcode 0001.
- reg_p[0x17]: Stack Pointer (`sp`). The stack pointer to push and pop values from, such as return addresses for subroutine calls.

Any of the above registers can be read from by certain opcodes. You will know this can be done if the opcode calls `seq_read_params`. If the last byte is under 0x18, it will return the value in the registers associated with that value. For example, the opcode `01500013` will read from register 0x13.

If the last byte is between 0x18 and 0x30, it will access from stored registers at seq_p[5].
