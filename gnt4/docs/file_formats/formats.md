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

MOT files contain one or more animations. They can be unpacked using QuickBMS and [naruto_mot.bms](/utils/naruto_mot.bms). Each character has a **0000.mot**, **0001.mot**, and potentially others. 0001.mot contains only a single animation, the idle animation used for the character select screen. 0000.mot contains battle animations, as well as the same idle animation in 0001.mot. You can replace animations with each other using the QuickBMS reimport option.

### GNTA Files

GNTA files are specific animations extracted using **naruto_mot.bms**. Their header info as as follows:

0x00(4): Number of entries  
0x04(4): Always 00000010  
0x08(4): Float. Smoothness/Bounciness of the animation, lower is bouncier, Usually is between .03 and .25  
0x0C(4): Float. Animation repeat delay, lower is quicker. Usually is between .03 and 5.0  
0x10(4): Always 00000040  
0x14(4): idk what this is, but always starts with FF FF  
0x18(4): idk the purpose of this float, but you can find it in the frame data entries in 0x08  
0x1C(4): 0 padding  
0x20(4): Pointer to the beginning of the animation values  

Frame data entries:  
0x00(2): Always begins with 02 02  
0x02(2): Always 21 or 28, other values don't seem to be allowed  
0x04(2): Bone id maybe  
0x06(2): Number of floats  
0x08(4): That float doesn't repeat itself twice for a specific value in 0x02  
0x0C(4): 0 padding  
0x10(4): Offset to the first part of the animation values  
0x14(4): Offset to the second part of the animation values  
0x18(4): 0 padding  

### Full List of MOT Files

* fpack\chr\hr\ank\0000.mot
* fpack\chr\hr\ank\0001.mot
* fpack\chr\hr\bou\0000.mot
* fpack\chr\hr\bou\0001.mot
* fpack\chr\hr\bou\1002.mot
* fpack\chr\hr\cho\0000.mot
* fpack\chr\hr\cho\0001.mot
* fpack\chr\hr\cho\1002.mot
* fpack\chr\hr\cmn\0000.mot
* fpack\chr\hr\dog\0000.mot
* fpack\chr\hr\dog\0001.mot
* fpack\chr\hr\gai\0000.mot
* fpack\chr\hr\gai\0001.mot
* fpack\chr\hr\gar\0000.mot
* fpack\chr\hr\gar\0001.mot
* fpack\chr\hr\hak\0000.mot
* fpack\chr\hr\hak\0001.mot
* fpack\chr\hr\hi2\0000.mot
* fpack\chr\hr\hi2\0001.mot
* fpack\chr\hr\hin\0000.mot
* fpack\chr\hr\hin\0001.mot
* fpack\chr\hr\ino\0000.mot
* fpack\chr\hr\ino\0001.mot
* fpack\chr\hr\ino\1000.mot
* fpack\chr\hr\iru\0000.mot
* fpack\chr\hr\iru\0001.mot
* fpack\chr\hr\ita\0000.mot
* fpack\chr\hr\ita\0001.mot
* fpack\chr\hr\jir\0000.mot
* fpack\chr\hr\jir\0001.mot
* fpack\chr\hr\jir\1001.mot
* fpack\chr\hr\jir\1153.mot
* fpack\chr\hr\kab\0000.mot
* fpack\chr\hr\kab\0001.mot
* fpack\chr\hr\kak\0000.mot
* fpack\chr\hr\kak\0001.mot
* fpack\chr\hr\kan\0000.mot
* fpack\chr\hr\kan\0001.mot
* fpack\chr\hr\kar\0000.mot
* fpack\chr\hr\kar\0001.mot
* fpack\chr\hr\kib\0000.mot
* fpack\chr\hr\kib\0001.mot
* fpack\chr\hr\kid\0000.mot
* fpack\chr\hr\kid\0001.mot
* fpack\chr\hr\kim\0000.mot
* fpack\chr\hr\kim\0001.mot
* fpack\chr\hr\kis\0000.mot
* fpack\chr\hr\kis\0001.mot
* fpack\chr\hr\loc\0000.mot
* fpack\chr\hr\loc\0001.mot
* fpack\chr\hr\miz\0000.mot
* fpack\chr\hr\miz\0001.mot
* fpack\chr\hr\na9\0000.mot
* fpack\chr\hr\na9\0001.mot
* fpack\chr\hr\nar\0000.mot
* fpack\chr\hr\nar\0001.mot
* fpack\chr\hr\nej\0000.mot
* fpack\chr\hr\nej\0001.mot
* fpack\chr\hr\obo\0000.mot
* fpack\chr\hr\obo\0001.mot
* fpack\chr\hr\oro\0000.mot
* fpack\chr\hr\oro\0001.mot
* fpack\chr\hr\sa2\0000.mot
* fpack\chr\hr\sa2\0001.mot
* fpack\chr\hr\sak\0000.mot
* fpack\chr\hr\sak\0001.mot
* fpack\chr\hr\sar\0000.mot
* fpack\chr\hr\sar\0001.mot
* fpack\chr\hr\sar\1003.mot
* fpack\chr\hr\sas\0000.mot
* fpack\chr\hr\sas\0001.mot
* fpack\chr\hr\sik\0000.mot
* fpack\chr\hr\sik\0001.mot
* fpack\chr\hr\sin\0000.mot
* fpack\chr\hr\sin\0001.mot
* fpack\chr\hr\sko\0000.mot
* fpack\chr\hr\sko\0001.mot
* fpack\chr\hr\ta2\0000.mot
* fpack\chr\hr\tay\0000.mot
* fpack\chr\hr\tay\0001.mot
* fpack\chr\hr\tem\0000.mot
* fpack\chr\hr\tem\0001.mot
* fpack\chr\hr\ten\0000.mot
* fpack\chr\hr\ten\0001.mot
* fpack\chr\hr\tsu\0000.mot
* fpack\chr\hr\tsu\0001.mot
* fpack\chr\hr\zab\0000.mot
* fpack\chr\hr\zab\0001.mot
* fpack\shop\0000.mot
* fpack\title\0000.mot
* fpack\unite\te\000\0000.mot
* fpack\unite\te\001\0000.mot
* fpack\unite\te\002\0000.mot
* fpack\unite\te\003\0000.mot
* fpack\unite\te\004\0000.mot
* fpack\unite\te\005\0000.mot
* fpack\unite\te\006\0000.mot
* fpack\unite\te\007\0000.mot
* fpack\unite\te\008\0000.mot
* fpack\unite\te\009\0000.mot
* fpack\unite\te\010\0000.mot
* fpack\unite\te\011\0000.mot
* fpack\unite\te\012\0000.mot
* fpack\unite\te\013\0000.mot
* fpack\unite\te\014\0000.mot

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
