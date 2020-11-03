# MOT Files

Credit to [Sifo](https://twitter.com/Zameen_Jinya) and Icylittlething for their investigation of the mot and gnta files.

MOT files contain one or more animations. They can be unpacked using QuickBMS and [naruto_mot.bms](/utils/naruto_mot.bms). Each character has a **0000.mot**, **0001.mot**, and potentially others. 0001.mot contains only a single animation, the idle animation used for the character select screen. 0000.mot contains battle animations, as well as the same idle animation in 0001.mot. You can replace animations with each other using the QuickBMS reimport option.

## GNTA Files

Gnta files are specific animations extracted using **naruto_mot.bms**. Gnta is an unofficial name given to these files since we do not know the original file type name. It stands for GNT Animation.

Gnta files are a series of keyframes. The game will automatically fill animations in-between each keyframe. A keyframe consists of an x, y, z, and w for all applicable joints. The joint values are the same as those used in the jcv and seq files. It is theorized that these were originally created using the auto key feature of soft image, a now-defunct 3D modeling program. You would give it a series of poses and it would fill in animations between them for you. 3dsmax has the same feature today.

It is believed that Eighting made the animations in soft image and converted them to gnta. Reason being, that they wanted their animations to be recyclable across many characters. The gnta format works across jcv files. It can store bone movement data for bones, and can even do so for bones a character potentially doesn't have. This allows them to reuse the same animation across many characters with different bones.

The universal throw for example defines movements for bones 16, 17, 18, and 19, which most characters don't have. So in this case the animation would ignore those movements for characters it does not match against. For a breakdown of bone ids see the [Bone IDs section](#Bone-IDs).

### Header info

| Offset | Size | Description                                                                                        |
|--------|------|----------------------------------------------------------------------------------------------------|
| 0x00   | 4    | Number of entries                                                                                  |
| 0x04   | 4    | Always 00000010                                                                                    |
| 0x08   | 4    | Float. Smoothness/Bounciness of the animation, lower is bouncier. Usually is between .03 and .25   |
| 0x0C   | 4    | Float. Animation repeat delay, lower is quicker. Usually is between .03 and 5.0                    |
| 0x10   | 4    | Playback speed of the animations. Eighting has always used 00000040                                |
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

## Bone IDs

- -1 - root?
- 0 - Y
- 1 - X
- 2 - Z
- 3 - hip
- 4 - waist
- 5 - breast
- 6 - head
- 7 - right collar
- 8 - right high arm
- 9 - right lower arm
- 10 - right hand
- 11 - left collar
- 12 - left high arm
- 13 - left lower arm
- 14 - left hand
- 15 - right high leg
- 16 - right lower leg
- 17 - right foot
- 18 - left high leg
- 19 - left lower leg
- 20 - left foot
- 21 - neck
- 22 - ?
- 23 - ?
- 24 - ?
- 25 - ?
- 26 - ?
- 27 - ?
- 28 - ?
- 29 - ?
- 30 - right high arm ex
- 31 - right high arm ex eff
- 32 - ?
- 33 - ?
- 34 - ?
- 35 - left high arm ex
- 36 - left high arm ex eff
- 37 - ?
- 38 - ?
- 39 - ?
- 40 - right high leg EX
- 41 - right high leg EX eff
- 42 - ?
- 43 - ?
- 44 - ?
- 45 - right toe
- 46 - left high leg EX
- 47 - left high leg EX eff
- 48 - ?
- 49 - ?
- 50 - ?
- 51 - left toe
- 52 - ?
- 53 - ?
- 54 - ?
- 55 - ?
- 56 - ?
- 57 - ?
- 58 - ?
- 59 - ?
- 60 - right thumb 1
- 61 - right thumb 2
- 62 - right thumb 3
- 63 - right index finger 1
- 64 - right index finger 2
- 65 - right index finger 3
- 66 - right middle finger 1
- 67 - right middle finger 2
- 68 - right middle finger 3
- 69 - right ring finger 1
- 70 - right ring finger 2
- 71 - right ring finger 3
- 72 - right pinky 1
- 73 - right pinky 2
- 74 - right pinky 3
- 75 - left thumb 1
- 76 - left thumb 2
- 77 - left thumb 3
- 78 - left index finger 1
- 79 - left index finger 2
- 80 - left index finger 3
- 81 - left middle finger 1
- 82 - left middle finger 2
- 83 - left middle finger 3
- 84 - left ring finger 1
- 85 - left ring finger 2
- 86 - left ring finger 3
- 87 - left pinky 1
- 88 - left pinky 2
- 89 - left pinky 3
- 90 - ?
- 91 - ?
- 92 - mouth top lip
- 93 - jaw
- 94 - mouth right side
- 95 - mouth left side
- 96 - ?
- 97 - ?
- 98 - ?
- 99 - ?
- 100 - ?
- 101 - ?
- 102 - mouth bottom lip
- 103 - ?
- 104 - ?
- 105 - ?
- 106 - ?
- 107 - ?
- 108 - ?
- 109 - ?
- 110 - pelvic bone?
- 111 - hair base
- 112 - hair right 1
- 113 - hair right 2
- 114 - hair right 3
- 115 - ?
- 116 - hair left 1
- 117 - hair left 2
- 118 - hair left 3
- 119 - upper breast
- 120 - lower breast
- 121 - ?
- 122 - ?
- 123 - ?
- 124 - ?
- 125 - ?
- 126 - ?
- 127 - ?
- 128 - ?
- 129 - ?
- 130 - ?
- 131 - ?
- 132 - ?
- 133 - ?
- 134 - ?
- 135 - ?
- 136 - ?
- 137 - ?
- 138 - ?
- 139 - ?
- 140 - ?
- 141 - ?

## Full List of MOT Files

- files\chr\ank\0000.mot
- files\chr\ank\0001.mot
- files\chr\bou\0000.mot
- files\chr\bou\0001.mot
- files\chr\bou\1002.mot
- files\chr\cho\0000.mot
- files\chr\cho\0001.mot
- files\chr\cho\1002.mot
- files\chr\cmn\0000.mot
- files\chr\dog\0000.mot
- files\chr\dog\0001.mot
- files\chr\gai\0000.mot
- files\chr\gai\0001.mot
- files\chr\gar\0000.mot
- files\chr\gar\0001.mot
- files\chr\hak\0000.mot
- files\chr\hak\0001.mot
- files\chr\hi2\0000.mot
- files\chr\hi2\0001.mot
- files\chr\hin\0000.mot
- files\chr\hin\0001.mot
- files\chr\ino\0000.mot
- files\chr\ino\0001.mot
- files\chr\ino\1000.mot
- files\chr\iru\0000.mot
- files\chr\iru\0001.mot
- files\chr\ita\0000.mot
- files\chr\ita\0001.mot
- files\chr\jir\0000.mot
- files\chr\jir\0001.mot
- files\chr\jir\1001.mot
- files\chr\jir\1153.mot
- files\chr\kab\0000.mot
- files\chr\kab\0001.mot
- files\chr\kak\0000.mot
- files\chr\kak\0001.mot
- files\chr\kan\0000.mot
- files\chr\kan\0001.mot
- files\chr\kar\0000.mot
- files\chr\kar\0001.mot
- files\chr\kib\0000.mot
- files\chr\kib\0001.mot
- files\chr\kid\0000.mot
- files\chr\kid\0001.mot
- files\chr\kim\0000.mot
- files\chr\kim\0001.mot
- files\chr\kis\0000.mot
- files\chr\kis\0001.mot
- files\chr\loc\0000.mot
- files\chr\loc\0001.mot
- files\chr\miz\0000.mot
- files\chr\miz\0001.mot
- files\chr\na9\0000.mot
- files\chr\na9\0001.mot
- files\chr\nar\0000.mot
- files\chr\nar\0001.mot
- files\chr\nej\0000.mot
- files\chr\nej\0001.mot
- files\chr\obo\0000.mot
- files\chr\obo\0001.mot
- files\chr\oro\0000.mot
- files\chr\oro\0001.mot
- files\chr\sa2\0000.mot
- files\chr\sa2\0001.mot
- files\chr\sak\0000.mot
- files\chr\sak\0001.mot
- files\chr\sar\0000.mot
- files\chr\sar\0001.mot
- files\chr\sar\1003.mot
- files\chr\sas\0000.mot
- files\chr\sas\0001.mot
- files\chr\sik\0000.mot
- files\chr\sik\0001.mot
- files\chr\sin\0000.mot
- files\chr\sin\0001.mot
- files\chr\sko\0000.mot
- files\chr\sko\0001.mot
- files\chr\ta2\0000.mot
- files\chr\tay\0000.mot
- files\chr\tay\0001.mot
- files\chr\tem\0000.mot
- files\chr\tem\0001.mot
- files\chr\ten\0000.mot
- files\chr\ten\0001.mot
- files\chr\tsu\0000.mot
- files\chr\tsu\0001.mot
- files\chr\zab\0000.mot
- files\chr\zab\0001.mot
- files\shop\0000.mot
- files\title\0000.mot
- files\unite\000\0000.mot
- files\unite\001\0000.mot
- files\unite\002\0000.mot
- files\unite\003\0000.mot
- files\unite\004\0000.mot
- files\unite\005\0000.mot
- files\unite\006\0000.mot
- files\unite\007\0000.mot
- files\unite\008\0000.mot
- files\unite\009\0000.mot
- files\unite\010\0000.mot
- files\unite\011\0000.mot
- files\unite\012\0000.mot
- files\unite\013\0000.mot
- files\unite\014\0000.mot
