# DOL File

## Table of Contents

1. **[Description](#Description)**
2. **[DOL Header](#DOL-Header)**
3. **[DOL Breakdown](#DOL-Breakdown)**
4. **[Assembly](#Assembly)**
5. **[Modifying the DOL](#Modifying-the-DOL)**
6. **[Decompilation](#Decompilation)**
6. **[Resources](#Resources)**

## Description

The DOL file format is the main executable format for the GameCube/Wii and contains all of the code for a game. The name presumably refers to "Dolphin", which was the GameCube's codename.

The DOL itself is similar to the [ELF file format](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format). So much so, that you can convert between the two formats using scripts both [open source](https://github.com/devkitPro/gamecube-tools/blob/master/elftool/elf2dol.c) and in the GameCube SDK. 

The DOL file format consists of a header and up to 7 loadable code sections (Text0..Text6) and up to 11 data sections (Data0..Data10). All values in the header are unsigned big-endian 32-bit values. **Text** is executable PowerPC assembly code and **data** are numbers and text used by the code. The header also allows for a [zero initialized (BSS)](https://en.wikipedia.org/wiki/.bss) range. This range can overlap the 18 sections, with the sections taking priority. The BSS section is for uninitialized variables.

## DOL Header

Here are the header entries for the Naruto GNT4 DOL file along with their respective values.

| Start |  End  |  Length |  Description                    |  Value              |
|-------|-------|---------|---------------------------------|---------------------|
| 0x0   |  0x3  |  4      |  File offset to start of Text0  |  0x100 (256)        |
| 0x4   |  0x7  |  4      |  File offset to start of Text1  |  0x26C0 (9920)      |
| 0x8   |  0xB  |  4      |  File offset to start of Text2  |  0x0 **NOT USED**   |
| 0xC   |  0xF  |  4      |  File offset to start of Text3  |  0x0 **NOT USED**   |
| 0x10  |  0x13 |  4      |  File offset to start of Text4  |  0x0 **NOT USED**   |
| 0x14  |  0x17 |  4      |  File offset to start of Text5  |  0x0 **NOT USED**   |
| 0x18  |  0x1B |  4      |  File offset to start of Text6  |  0x0 **NOT USED**   |
| 0x1C  |  0x1F |  4      |  File offset to start of Data0  |  0x1FA800 (2074624) |
| 0x20  |  0x23 |  4      |  File offset to start of Data1  |  0x1FA820 (2074656) |
| 0x24  |  0x27 |  4      |  File offset to start of Data2  |  0x1FA840 (2074688) |
| 0x28  |  0x2B |  4      |  File offset to start of Data3  |  0x202C40 (2108480) |
| 0x2C  |  0x2F |  4      |  File offset to start of Data4  |  0x21F9E0 (2226656) |
| 0x30  |  0x33 |  4      |  File offset to start of Data5  |  0x2200A0 (2228384) |
| 0x34  |  0x37 |  4      |  File offset to start of Data6  |  0x0 **NOT USED**   |
| 0x38  |  0x3B |  4      |  File offset to start of Data7  |  0x0 **NOT USED**   |
| 0x3C  |  0x3F |  4      |  File offset to start of Data8  |  0x0 **NOT USED**   |
| 0x40  |  0x43 |  4      |  File offset to start of Data9  |  0x0 **NOT USED**   |
| 0x44  |  0x47 |  4      |  File offset to start of Data10 |  0x0 **NOT USED**   |
| 0x48  |  0x4B |  4      |  Loading address for Text0      |  0x80003100         |
| 0x4C  |  0x4F |  4      |  Loading address for Text1      |  0x800056C0         |
| 0x50  |  0x53 |  4      |  Loading address for Text2      |  0x0 **NOT USED**   |
| 0x54  |  0x57 |  4      |  Loading address for Text3      |  0x0 **NOT USED**   |
| 0x58  |  0x5B |  4      |  Loading address for Text4      |  0x0 **NOT USED**   |
| 0x5C  |  0x5F |  4      |  Loading address for Text5      |  0x0 **NOT USED**   |
| 0x60  |  0x63 |  4      |  Loading address for Text6      |  0x0 **NOT USED**   |
| 0x64  |  0x67 |  4      |  Loading address for Data0      |  0x801FD800         |
| 0x68  |  0x6B |  4      |  Loading address for Data1      |  0x801FD820         |
| 0x6C  |  0x6F |  4      |  Loading address for Data2      |  0x801FD840         |
| 0x70  |  0x73 |  4      |  Loading address for Data3      |  0x80205C40         |
| 0x74  |  0x77 |  4      |  Loading address for Data4      |  0x80276920         |
| 0x78  |  0x7B |  4      |  Loading address for Data5      |  0x80277CA0         |
| 0x7C  |  0x7F |  4      |  Loading address for Data6      |  0x0 **NOT USED**   |
| 0x80  |  0x83 |  4      |  Loading address for Data7      |  0x0 **NOT USED**   |
| 0x84  |  0x87 |  4      |  Loading address for Data8      |  0x0 **NOT USED**   |
| 0x88  |  0x8B |  4      |  Loading address for Data9      |  0x0 **NOT USED**   |
| 0x8C  |  0x8F |  4      |  Loading address for Data10     |  0x0 **NOT USED**   |
| 0x90  |  0x93 |  4      |  Section sizes for Text0        |  0x25C0 (9664)      |
| 0x94  |  0x97 |  4      |  Section sizes for Text1        |  0x1F8140 (2064704) |
| 0x98  |  0x9B |  4      |  Section sizes for Text2        |  0x0 **NOT USED**   |
| 0x9C  |  0x9F |  4      |  Section sizes for Text3        |  0x0 **NOT USED**   |
| 0xA0  |  0xA3 |  4      |  Section sizes for Text4        |  0x0 **NOT USED**   |
| 0xA4  |  0xA7 |  4      |  Section sizes for Text5        |  0x0 **NOT USED**   |
| 0xA8  |  0xAB |  4      |  Section sizes for Text6        |  0x0 **NOT USED**   |
| 0xAC  |  0xAF |  4      |  Section sizes for Data0        |  0x20 (32)          |
| 0xB0  |  0xB3 |  4      |  Section sizes for Data1        |  0x20 (32)          |
| 0xB4  |  0xB7 |  4      |  Section sizes for Data2        |  0x8400 (33792)     |
| 0xB8  |  0xBB |  4      |  Section sizes for Data3        |  0x1CDA0 (118176)   |
| 0xBC  |  0xBF |  4      |  Section sizes for Data4        |  0x6C0 (1728)       |
| 0xC0  |  0xC3 |  4      |  Section sizes for Data5        |  0x48C0 (18624)     |
| 0xC4  |  0xC7 |  4      |  Section sizes for Data6        |  0x0 **NOT USED**   |
| 0xC8  |  0xCB |  4      |  Section sizes for Data7        |  0x0 **NOT USED**   |
| 0xCC  |  0xCF |  4      |  Section sizes for Data8        |  0x0 **NOT USED**   |
| 0xD0  |  0xD3 |  4      |  Section sizes for Data9        |  0x0 **NOT USED**   |
| 0xD4  |  0xD7 |  4      |  Section sizes for Data10       |  0x0 **NOT USED**   |
| 0xD8  |  0xDB |  4      |  BSS address                    |  0x802229E0         |
| 0xDC  |  0xDF |  4      |  BSS size                       |  0x59B98 (367512)   |
| 0xE0  |  0xE3 |  4      |  Entry point                    |  0x80003154         |
| 0xE4  |  0xFF |  28     |  padding                        |  0x0                |

## DOL Breakdown

GNT4 has two sections of code, Text0 and Text1, known as **init** and **text** respectively. The **init** section starts at file offset 0x100, which is loaded into address 0x80003100 when the game starts. The **text** section starts at file offset 0x26c0, which is loaded into address 0x800056c0 when the game starts.

The **init** section is all of the code that runs when the game starts up. All of this code runs before any of the intro videos play. The **text** section is all of the rest of the code of the game.

## Assembly

The code in the DOL is PowerPC assembly. IBM designed a custom processor called the [Gekko](https://en.wikipedia.org/wiki/Gekko_(microprocessor)) for the GameCube and the [Broadway](https://en.wikipedia.org/wiki/Broadway_(microprocessor)) for the Wii. These use the PowerPC instruction set, but with additional features for better performance with video games.

## Modifying the DOL

Modifying the DOL may be very easy or very hard depending on what you wish to do. For example, assuming you just wish to replace a single instruction. All this requires is finding the instruction in the DOL and replace the four bytes with the four bytes of your desired new instruction. This type of modification is similar to the Gecko code for a [32 bits Write](https://github.com/NicholasMoser/Naruto-GNT-Modding/blob/master/general/docs/guides/gecko_codetype_documentation.md#32-bits-write).

However, assume you wish to replace a single instruction with multiple instructions. This will require either making the DOL larger or overwriting other existing instructions. The DOL cannot simply be made larger to due all of the code inside of it using offsets to jump around. Inserting new code would break these offsets. Overwriting existing code and branching to and from it is much simpler to implement but riskier since code is removed from the game. This type of modification is similar to the Gecko code for [Insert ASM](https://github.com/NicholasMoser/Naruto-GNT-Modding/blob/master/general/docs/guides/gecko_codetype_documentation.md#insert-asm).

Both Gecko codes for 32 bits Write and Insert ASM can be inserted into a DOL using GNTool. This functionality was added as part of [this issue](https://github.com/NicholasMoser/GNTool/issues/14). Insert ASM codes in particular overwrite the unused recording functionality in GNT4, therefore no functionality in the game is lost. For more information on how this works, see the README for GNTool.

## Decompilation

Through [decompilation](https://en.wikipedia.org/wiki/Decompiler), we can slowly recreate the original C/C++ code of the game from the assembly in the DOL. This is currently being done at [doldecomp/gnt4](https://github.com/doldecomp/gnt4). Eventually, it may be possible to compile the game with entirely new C/C++ for easier modding.

## Resources

[DOL File Format](http://wiki.tockdom.com/wiki/DOL_(File_Format))

[Gamecube Optical Disc Drive Guidelines](https://archive.org/stream/GCN_SDK_Documentation/Nintendo%20GameCube%20Optical%20Disc%20Drive%20Guidelines%20Version%201.41_djvu.txt)

[Sham Rock ASM Injection Guide](https://smashboards.com/threads/the-dol-mod-topic.326347/page-5#post-16623011)
