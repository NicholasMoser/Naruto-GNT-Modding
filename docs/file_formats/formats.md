# File Formats

## Table of Contents
1. **[FPK Files](#fpk-files)**
2. **[SEQ Files](#dat-files)**
3. **[DAT Files](#dat-files)**
4. **[JCV Files](#jcv-files)**
5. **[TXG Files](#txg-files)**
6. **[MOT Files](#mot-files)**
7. **[PTL Files](#ptl-files)**
8. **[REF Files](#ref-files)**
9. **[POO, PRO, SAM and SDI Files](#poo-pro-sam-and-sdi-files)**
10. **[TRK Files](#trk-files)**
11. **[H4M Files](#h4m-files)**

# FPK Files
These files are archives that contain related character data files. For more information see the following page: [FPK Files](/docs/file_formats/fpk.md)

# SEQ Files
Contains much of the logic of the game itself. Think character health, attacks, etc.

# DAT Files
HAL Labs HSD Model format. The same model format used in Melee.

# JCV Files
These files are **believed** to be bones/armature for associated DAT files.

# TXG Files
These files contain textures. ThatTrueStruggle has written a program that will allow you to convert them to TPL here: [TXG2TPL code](https://github.com/ThatTrueStruggle/TXG2TPL).
TPL files can be opened with [BrawlBox](https://github.com/libertyernie/brawltools)

# MOT Files
The file that contains animations.

# PTL Files
???

# REF Files
???

# POO, PRO, SAM and SDI Files
These files are for sound and voice. The main files that contain sound data are the SAM/SDI files. You can unpack and pack SAM and SDI files with [MusyX-Extract](https://github.com/Nisto/musyx-extract)

# TRK Files
TRK files are music files (does not include sound effects). are simply renamed ADP Files. A list of what each audio file represents and can be found here: [Background Music](/docs/audio/bgm.md)

# H4M Files
Movie files. Includes the opening, ending, Tomy and 8ing videos.
You can find the patent for this format here: https://www.google.com/patents/US6714687
You can find a tool to decode the audio from it here: https://github.com/hcs64/vgm_ripping/tree/master/demux/h4m_audio_decode
