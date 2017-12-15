# Naruto-GNT4-Hacking
Naruto Gekitō Ninja Taisen! 4 (GNT4) Hacking White Paper

## Table of Contents
1. **[Basics](#basics)**
2. **[FPK Files](#fpk-files)**
3. **[TXG Files](#txg-files)**
4. **[DAT Files](#dat-files)**
5. **[JCV Files](#jcv-files)**
6. **[PTL Files](#ptl-files)**
7. **[REF Files](#ref-files)**
8. **[POO Files](#poo-files)**
9. **[PRO Files](#pro-files)**
10. **[SAM Files](#sam-files)**
11. **[SDI Files](#jcv-files)**
12. **[TRK Files](#trk-files)**
13. **[H4M Files](#h4m-files)**

# Basics
Before you begin reading, if you are only interested in modifying textures for an emulated copy of GNT4 you are in luck. The [Dolphin Emulator](https://dolphin-emu.org/) drastically simplifies this process with the **Dump Textures** and **Load Textures** tools. This will allow you to skip straight to the texture design process. As of version 5.0 you will find these two options under the Advanced tab of Graphics Configuration. However, modifying anything else in the game will require understanding more about the game data files. You can both import and export these files by using the [GCRebuilder](https://www.google.com/search?q=gcrebuilder) with your copy of the game.

# FPK Files
Naruto character data is stored in FPK files. These files are archives that contain related character data files. Naruto GNT3 seems to do the same, so it's likely all GNT games conform to this. For more information on game data archives, see http://wiki.xentax.com/index.php/DGTEFF

I have written a script to unpack these files using Python (version 3.2+). [You can find it here](utils/fpk_unpack.py)

### FPK Headers
The first 16 bytes in an FPK file represent the header for the file. In particular, this header describes information regarding the archive such as how many files are being stored in this single FPK file. The byte order is **Big-Endian**. 

| Bytes | Value                                                 |
| :---- | :---------------------------------------------------- |
|   4   | Unknown (Seems to always be null)                     |
|   4   | Number of Files                                       |
|   4   | Could be String/Entry size                            |
|   4   | File/asset size (could be EoF if this wasn't split)   |

After the first 16 bytes, will be 32 byte headers for each archived file.

| Bytes | Value                                                 |
| :---- | :---------------------------------------------------- |
|   16  | Resource file name string (null terminated)           |
|   4   | Unknown (Seems to always be null)                     |
|   4   | Offset                                                |
|   4   | Size                                                  |
|   4   | Unknown                                               |

The rest of the information in the FPK file will be the data contained in each archived file. You can use the file sizes and offsets to find where each one starts and ends. 

### Character File Abbreviations
| Abbreviation | Character                  |
| :----------- | :------------------------- |
|   ank        | Anko                       |
|   bou        | Jirōbō                     |
|   cho        | Chōji                      |
|   cmn        | ???                        |
|   dog        | Akamaru                    |
|   gai        | Might Guy                  |
|   gar        | Gaara                      |
|   hak        | Haku	                      |
|   hi         | Awakened Hinata            |
|   hin        | Hinata                     |
|   ino        | Ino                        |
|   iru        | Iruka                      |
|   ita        | Itachi                     |
|   jir        | Jiraiya                    |
|   kab        | Kabuto                     |
|   kak        | Kakashi                    |
|   kan        | Kankurō                    |
|   kar        | Karasu (Puppet)            |
|   kib        | Kiba                       |
|   kid        | Kidōmaru                   |
|   kim        | Kimimaro                   |
|   kis        | Kisame                     |
|   loc        | Rock Lee                   |
|   miz        | Mizuki                     |
|   na         | Kyūbi Naruto               |
|   nar        | Naruto                     |
|   nej        | Neji                       |
|   obo        | Oboro                      |
|   oro        | Orochimaru                 |
|   sa         | Sasuke CS2                 |
|   sak        | Sakura                     |
|   sar        | Sarutobi (Third Hokage)    |
|   sas        | Sasuke                     |
|   scmn       | ???                        |
|   sik        | Shikamaru                  |
|   sin        | Shino                      |
|   sko        | Sakon                      |
|   ta         | ???                        |
|   tay        | Tayuya                     |
|   tem        | Temari                     |
|   ten        | Tenten                     |
|   tsu        | Tsunade                    |
|   zab        | Zabuza                     |
  
### FPK File Contents
When you unpack an FPK file, you will find a handful of different files types that have been extracted. Different characters will have different amounts of these files.

| File Type | Purpose                                                                                        |
| :-------- | :--------------------------------------------------------------------------------------------- |
|   .dat    | Likely general character data                                                                  |
|   .jcv    | Unknown (seems to be paired with a .dat file)                                                  |
|   .txg    | Texture file                                                                                   |
|   .mot    | [Likely motion](https://simtk-confluence.stanford.edu/display/OpenSim/Motion+%28.mot%29+Files) |
|   .ptl    | Unknown                                                                                        |
|   .ref    | Unknown                                                                                        |
|   .poo    | Unknown                                                                                        |
|   .pro    | Unknown                                                                                        |
|   .sam    | Unknown                                                                                        |
|   .sdi    | Unknown                                                                                        |

# TXG Files
These files contain textures. For more information, see ThatTrueStruggle's [TXG2TPL code](https://github.com/ThatTrueStruggle/TXG2TPL).

# DAT Files
???

# JCV Files
???

# PTL Files
???

# REF Files
???

# POO Files
???

# PRO Files
???

# SAM Files
???

# SDI Files
???

# TRK Files
TRK files are simply renamed ADP Files. A list of what each audio file represents and can be found here: [Audio](docs/music.md)

# H4M Files
???
