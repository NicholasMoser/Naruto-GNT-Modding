# File Formats

## Table of Contents

1. **[FPK Files](#fpk-files)**
2. **[SEQ Files](#seq-files)**
3. **[DAT Files](#dat-files)**
4. **[JCV Files](#jcv-files)**
5. **[TXG Files](#txg-files)**
6. **[MOT Files](#mot-files)**
7. **[PTL Files](#ptl-files)**
8. **[REF Files](#ref-files)**
9. **[POO, PRO, SAM and SDI Files](#poo-pro-sam-and-sdi-files)**
10. **[TRK Files](#trk-files)**
11. **[H4M Files](#h4m-files)**

## DOL File

The Dol file format is the main executable file format for both the GameCube and the Wii. The name presumably refers to "Dolphin", which was the GameCube's codename. 
It is a simple file format consisting of a header and up to 7 loadable code sections (Text0..Text6) and up to 11 data sections (Data0..Data10). 
All values in the header are unsigned big-endian 32-bit values. 
For more information see the following page: [DOL File](/gnt4/docs/file_formats/dol.md)

## FPK Files

These files are archives that contain related character data files. For more information see the following page: [FPK Files](/gnt4/docs/file_formats/fpk.md)

## SEQ Files

Contains much of the logic of the game itself. Think character health, attacks, etc.

## DAT Files

HAL Labs HSD Model format. The same model format used in Melee.

## JCV Files

These files are responsible for bones/armature for associated DAT files.

## TXG Files

These files contain textures. ThatTrueStruggle has written a program that will allow you to convert them to TPL called [TXG2TPL](https://github.com/ThatTrueStruggle/TXG2TPL).

TPL files can be opened with [BrawlBox](https://github.com/libertyernie/brawltools).

## MOT Files

The file that contains animations.

## PTL Files

???

## REF Files

???

## POO, PRO, SAM and SDI Files

These files are for sound and voice. The main files that contain sound data are the SAM/SDI files. You can unpack and pack SAM and SDI files with [MusyX-Extract](https://github.com/Nisto/musyx-extract)

## TRK Files

TRK files are music files (does not include sound effects). are simply renamed ADP Files. A list of what each audio file represents and can be found here: [Background Music](/gnt4/docs/audio/bgm.md)

## H4M Files

Movie files. Includes the opening, ending, Tomy and 8ing videos.

You can find the patent on Google under [Patent US6714687B2](https://www.google.com/patents/US6714687)

To decode the audio you can use [h4m_audio_decode](https://github.com/hcs64/vgm_ripping/tree/master/demux/h4m_audio_decode)
