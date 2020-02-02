# MOT Files

MOT files contain one or more animations. They can be unpacked using QuickBMS and [naruto_mot.bms](/utils/naruto_mot.bms). Each character has a **0000.mot**, **0001.mot**, and potentially others. 0001.mot contains only a single animation, the idle animation used for the character select screen. 0000.mot contains battle animations, as well as the same idle animation in 0001.mot. You can replace animations with each other using the QuickBMS reimport option.

## GNTA Files

GNTA files are specific animations extracted using **naruto_mot.bms**. GNTA is an unofficial name given to these files since we do not know the original file type name. It stands for GNT Animation.

### Header info

| Offset | Size | Description                                                                                        |
|--------|------|----------------------------------------------------------------------------------------------------|
| 0x00   | 4    | Number of entries                                                                                  |
| 0x04   | 4    | Always 00000010                                                                                    |
| 0x08   | 4    | Float. Smoothness/Bounciness of the animation, lower is bouncier. Usually is between .03 and .25   |
| 0x0C   | 4    | Float. Animation repeat delay, lower is quicker. Usually is between .03 and 5.0                    |
| 0x10   | 4    | Always 00000040                                                                                    |
| 0x14   | 4    | idk what this is, but always starts with FF FF                                                     |
| 0x18   | 4    | idk the purpose of this float, but you can find it in the frame data entries in 0x08               |
| 0x1C   | 4    | 0 padding                                                                                          |
| 0x20   | 4    | Pointer to the beginning of the animation values                                                   |

### Frame data entries

| Offset | Size | Description                                                         |
|--------|------|---------------------------------------------------------------------|
| 0x00   | 2    | Always begins with 02 02                                            |
| 0x02   | 2    | Always 21 or 28, other values don't seem to be allowed              |
| 0x04   | 2    | Bone id maybe                                                       |
| 0x06   | 2    | Number of floats                                                    |
| 0x08   | 4    | That float doesn't repeat itself twice for a specific value in 0x02 |
| 0x0C   | 4    | 0 padding                                                           |
| 0x10   | 4    | Offset to the first part of the animation values                    |
| 0x14   | 4    | Offset to the second part of the animation values                   |
| 0x18   | 4    | 0 padding                                                           |

## Full List of MOT Files

* files\chr\ank\0000.mot
* files\chr\ank\0001.mot
* files\chr\bou\0000.mot
* files\chr\bou\0001.mot
* files\chr\bou\1002.mot
* files\chr\cho\0000.mot
* files\chr\cho\0001.mot
* files\chr\cho\1002.mot
* files\chr\cmn\0000.mot
* files\chr\dog\0000.mot
* files\chr\dog\0001.mot
* files\chr\gai\0000.mot
* files\chr\gai\0001.mot
* files\chr\gar\0000.mot
* files\chr\gar\0001.mot
* files\chr\hak\0000.mot
* files\chr\hak\0001.mot
* files\chr\hi2\0000.mot
* files\chr\hi2\0001.mot
* files\chr\hin\0000.mot
* files\chr\hin\0001.mot
* files\chr\ino\0000.mot
* files\chr\ino\0001.mot
* files\chr\ino\1000.mot
* files\chr\iru\0000.mot
* files\chr\iru\0001.mot
* files\chr\ita\0000.mot
* files\chr\ita\0001.mot
* files\chr\jir\0000.mot
* files\chr\jir\0001.mot
* files\chr\jir\1001.mot
* files\chr\jir\1153.mot
* files\chr\kab\0000.mot
* files\chr\kab\0001.mot
* files\chr\kak\0000.mot
* files\chr\kak\0001.mot
* files\chr\kan\0000.mot
* files\chr\kan\0001.mot
* files\chr\kar\0000.mot
* files\chr\kar\0001.mot
* files\chr\kib\0000.mot
* files\chr\kib\0001.mot
* files\chr\kid\0000.mot
* files\chr\kid\0001.mot
* files\chr\kim\0000.mot
* files\chr\kim\0001.mot
* files\chr\kis\0000.mot
* files\chr\kis\0001.mot
* files\chr\loc\0000.mot
* files\chr\loc\0001.mot
* files\chr\miz\0000.mot
* files\chr\miz\0001.mot
* files\chr\na9\0000.mot
* files\chr\na9\0001.mot
* files\chr\nar\0000.mot
* files\chr\nar\0001.mot
* files\chr\nej\0000.mot
* files\chr\nej\0001.mot
* files\chr\obo\0000.mot
* files\chr\obo\0001.mot
* files\chr\oro\0000.mot
* files\chr\oro\0001.mot
* files\chr\sa2\0000.mot
* files\chr\sa2\0001.mot
* files\chr\sak\0000.mot
* files\chr\sak\0001.mot
* files\chr\sar\0000.mot
* files\chr\sar\0001.mot
* files\chr\sar\1003.mot
* files\chr\sas\0000.mot
* files\chr\sas\0001.mot
* files\chr\sik\0000.mot
* files\chr\sik\0001.mot
* files\chr\sin\0000.mot
* files\chr\sin\0001.mot
* files\chr\sko\0000.mot
* files\chr\sko\0001.mot
* files\chr\ta2\0000.mot
* files\chr\tay\0000.mot
* files\chr\tay\0001.mot
* files\chr\tem\0000.mot
* files\chr\tem\0001.mot
* files\chr\ten\0000.mot
* files\chr\ten\0001.mot
* files\chr\tsu\0000.mot
* files\chr\tsu\0001.mot
* files\chr\zab\0000.mot
* files\chr\zab\0001.mot
* files\shop\0000.mot
* files\title\0000.mot
* files\unite\000\0000.mot
* files\unite\001\0000.mot
* files\unite\002\0000.mot
* files\unite\003\0000.mot
* files\unite\004\0000.mot
* files\unite\005\0000.mot
* files\unite\006\0000.mot
* files\unite\007\0000.mot
* files\unite\008\0000.mot
* files\unite\009\0000.mot
* files\unite\010\0000.mot
* files\unite\011\0000.mot
* files\unite\012\0000.mot
* files\unite\013\0000.mot
* files\unite\014\0000.mot
