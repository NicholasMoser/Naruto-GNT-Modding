# DOL File

## Table of Contents
1. **[Description](#description)**
2. **[DOL Header](#dol-header)**
3. **[DOL Breakdown](#dol-breakdown)**
4. **[DOL Code Empty Space](#dol-code-empty-space)**
5. **[How to Inject ASM](#how-to-inject-asm)**
6. **[Resources](#resources)**

## Description

The Dol file format is for GameCube and Wii disc partitions. The name presumably refers to "Dolphin", which was the GameCube's codename. It is a simple file format consisting of a header and up to 7 loadable code sections (Text0..Text6) and up to 11 data sections (Data0..Data10). All values in the header are unsigned big-endian 32-bit values. Text is executable code and data is just data for the game. The header also allows for a zero initialized (BSS) range. This range can overlap the 18 sections, with the sections taking priority. The BSS section is for uninitialized variables.

More information can be found here: http://wiki.tockdom.com/wiki/DOL_(File_Format)

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

GNT4 has two sections of code, Text0 and Text1. Text0 starts at file offset 0x100, which is loaded into address 0x80003100 when the game is playing. Text1 starts at file offset 0x26c0, which is loaded into address 0x800056c0 when the game is playing.

Text0 is all of the code up until you hit Start at the title screen. This includes initialization of things needed to run the game such as registers. After you hit Start at the title screen it will begin Text1 code. This explains why Text0 is 9,664 bytes and Text1 is 2,064,704 bytes. This also means that if you go back to the title screen and hit Start again, it will begin from the start of Text1 code again.

* Data0: 32 bytes of zeros.
* Data1: The four byte word 0x8018E10C followed by 28 bytes of zeros. 0x8018E10C is a location to the ASM code for __destroy_global_chain.
* Data2: Contains lots of text (e.g. file names, error messages, debug messages)
* Data3: ???
* Data4: Contains names of c code files (e.g. dvd.c, audio.c, pobj.c, hash.c)
* Data5: Contains names of in-game battle properties (e.g. UKEMI, DAMAGE, THROW, SPECIAL).

## DOL Code Empty Space

One way of injection ASM is to insert into empty space in the code. There is only a single gap in Text1 for inserting new code. It exists at Start.dol offset 0x18a424, which is loaded into address 0x8018d424. It has room for 3 instructions, however this actually would only be 2 instructions since one instruction needs to be a return to the calling code.

## How to Inject ASM

*Note: This was taken from [Sham Rock's smashboards post](https://smashboards.com/threads/the-dol-mod-topic.326347/page-5#post-16623011) on how to do it*

### Requirements

* A working ASM code
* The DOL file
* Debug version of Dolphin that can execute memory breakpoints
* Tool to extract/replace the dol (gc-rebuilder or gc-tool)
* Hex editor
* ASM <> WiiRd converter

### Guide

Injecting ASM into the game involves inserting ASM codes (C2xx xxxx) directly into the ISO (particularly the DOL). First you will need to find free space in the DOL. Extract the DOL, then load it up in your hex editor and look for some free space (a lot of 00´s). Insert the code and add a little something to make it easy to find it later on (0xFEDCBA98 for example since it´s normally not found in the game's memory, so you can find it easily with a single memory search). Save and insert the DOL into the ISO.

Next you will need to check if the memory space is safe to inject. Load up the ISO in dolphin and search for the identifier you added (0xFEDCBA98 in this case). It should only give you 1 result. From there you can find where you inserted the code into the game permanently. To check if it's safe to use that space load up the development version of dolphin and simply put 1 big memory-breakpoint for all the memory addresses we just modified and just play a bit. If the game never breaks, it never uses those memory addresses and it's safe to use them.

Now that we know the memory is not used by the game, we can add 2 simple branches to and from the custom code. One way to do this is with the ASM<>WiiRd converter:

**Branching backwards**  
b 0x (FFFF FFFF - (start memory address - end memory address) )+1 in this case  
(FFFF FFFF - (801a415c - 80004420) )+ 1 = FFE602C4  
--> enter "b 0xFFE602C4" into converter  
--> 4BE602C4 assembler instruction that has to be inserted into the dol where the code would normally be injected

**Branching forward**  
b 0x end address - start address  
801a4160 - 8000448c = 19FCD4  
--> enter "b 0x19FCD4" into converter  
--> 4819FCD4 assembler instruction that has to be inserted where we wrote "FEDCBA98"

Now you can find the injection point (0x801A415C in this example) in the DOL. You can find it with a simple hex search by looking at the surrounding instructions:

```
address code line hex instructions
801a415c subi r0, r3, 1 3803ffff
801a4160 stb r0, 0x0003 (r31) 981f0003
801a4164 li r0, 0 38000000
801a4168 stb r0, 0x0005 (r31) 981f0005
```

search for "3803ffff981f000338000000981f0005" in the DOL
1 result @1A0D3C, meaning that's the point the branch backwards has to be inserted

## Resources

[DOL File Format](http://wiki.tockdom.com/wiki/DOL_(File_Format))

[Gamecube Optical Disc Drive Guidelines](https://archive.org/stream/GCN_SDK_Documentation/Nintendo%20GameCube%20Optical%20Disc%20Drive%20Guidelines%20Version%201.41_djvu.txt)

[Sham Rock ASM Injection Guide](https://smashboards.com/threads/the-dol-mod-topic.326347/page-5#post-16623011)
