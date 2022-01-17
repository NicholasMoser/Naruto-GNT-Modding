# MOT Files

Credit to [Sifo](https://twitter.com/Zameen_Jinya) and Icylittlething for their investigation of the mot and gnta files.

MOT files contain one or more animations. They can be unpacked using QuickBMS and [naruto_mot.bms](/utils/naruto_mot.bms). Each character has a **0000.mot**, **0001.mot**, and potentially others. 0001.mot contains only a single animation, the idle animation used for the character select screen. 0000.mot contains battle animations, as well as the same idle animation in 0001.mot. You can replace animations with each other using the QuickBMS reimport option.

### Header info

| Offset | Size | Description                                                                                        |
|--------|------|----------------------------------------------------------------------------------------------------|
| 0x00   | 4    | Null bytes                                                                                         |
| 0x04   | 4    | Total number of animations                                                                         |
| 0x08   | 4    | Header size                                                                                        |
| 0x0C   | 4    | File size                                                                                          |

The header is followed by an integer for every animation, where that integer is the offset to it.

## GNTA Files

.gnta is an unofficial file name extension given to individual animations of a .mot file. It's unofficial since we don't know the actual name that Eighting used.

Gnta files are a series of keyframes. Keyframes are snapshots of movement at specific moments. The game will automatically fill animations in-between each keyframe. A keyframe consists of an x, y, z, and w for all applicable joints. The joint values are the same as those used in the jcv and seq files. These were originally created using the auto key feature of soft image, a now-defunct 3D modeling program. You would give it a series of poses and it would fill in animations between them for you. 3dsmax has the same feature today.

Eighting made the animations in soft image and converted them to gnta. Reason being, they wanted their animations to be recyclable across many characters. The gnta format works across jcv files. It can store bone movement data for bones, and can even do so for bones a character potentially doesn't have. This allows them to reuse the same animation across many characters with different bones.

The universal throw for example defines movements for bones 118, 119, and 120, which most characters don't have. So in this case the animation would ignore those movements for characters it does not match against. For a breakdown of bone ids see the [Bone IDs section](#Bone-IDs).

Gnta files were also designed to be able to combine, in that you can ask the game to play two at once. If the joints do not conflict, the game will do so. This is how hand animations in done in the GNT games. For example, Naruto's clone summoning animation is completely separate from the hand sign animation he does to call it.

### MOT Header

The MOT header defines a number of animation IDs. The header is followed by 4-byte words for each animation ID. Each 4-byte word
is the optional offset to that animation. If there is no animation, the offset will be 0. The animation at the given offset is
a GNTA file.

| Offset | Size | Description                                                                                        |
|--------|------|----------------------------------------------------------------------------------------------------|
| 0x00   | 4    | Padding (zeros)                                                                                    |
| 0x04   | 4    | Number of animation IDs                                                                            |
| 0x08   | 4    | Header size (always 0x10)                                                                          |
| 0x0C   | 4    | MOT file size                                                                                      |

### GNTA Header

A GNTA file defines a number of bone animations.

| Offset | Size | Description                                                                                        |
|--------|------|----------------------------------------------------------------------------------------------------|
| 0x00   | 4    | Number of bone animations                                                                          |
| 0x04   | 4    | Always 0x00000010                                                                                  |
| 0x08   | 4    | Float. Smoothness/Bounciness of the animation, lower is bouncier. Usually is between .03 and .25   |
| 0x0C   | 4    | Float. Animation repeat delay, lower is quicker. Usually is between .03 and 5.0                    |
| 0x10   | 4    | Playback speed of the animations. Eighting has always used 00000040                                |
| 0x14   | 2    | Unknown, always 0xFFFF                                                                             |
| 0x16   | 2    | Number of function curve values                                                                    |
| 0x18   | 4    | Unknown, but you can find it in the frame data entries in 0x08                                     |
| 0x1C   | 4    | Padding (zeros)                                                                                    |
| 0x20   | 4    | Offset to the function curve values                                                                |

### Bone Animation Header

A bone animation defines a number of key frames for a specific bone.

| Offset | Size | Description                                                         |
|--------|------|---------------------------------------------------------------------|
| 0x00   | 4    | Flags. Always begins with 02 02. Ends with 21 or 28.                |
| 0x04   | 2    | Bone id maybe                                                       |
| 0x06   | 2    | Number of key frames                                                |
| 0x08   | 4    | That float doesn't repeat itself twice for a specific value in 0x02 |
| 0x0C   | 4    | Padding (zeros)                                                     |
| 0x10   | 4    | Offset to the function curve for each key frame                     |
| 0x14   | 4    | Offset to the coordinates for each key frame                        |
| 0x18   | 4    | Padding (zeros)                                                     |

## Character Animation IDs to Purpose

- 0000: Idle
- 0001: Walk Forward
- 0002: Walk Backward
- 0003: Dash
- 0004: Dash End
- 0005: Run
- 0006: Run End
- 0007: Back Dash
- 0008: Turn Around
- 000A: 5Z out

- 0010: Rolling across the ground after being killed with butt
- 0013: Turn around while getting up

- 0020: Block
- 0021: Standing blocking slide
- 0022: Block
- 0023: Block
- 0024: Block low
- 0026: Crouching pushing sliding block
- 0028: Hit by butt
- 0029: Hit by butt back turned
- 002A: Landing from butt on back
- 002B: Landing from butt on face
- 002C: Sinking in Jiraiya swamp
- 002D: Hit by Shika 2X
- 002E: Coming to a stop from tata on face
- 002F: Trapped (Kido 5A2C / Shino 2A)

- 0030: Jump Startup
- 0031: Jump Land
- 0032: Jump
- 0033: Falling in the air
- 0034: Breaking a grab
- 0035: Having a grab broken
- 0036: grab break in the air
- 0037: Guard break in the air / grab broken in the air
- 0038: Feet trapped (Kido 2A)
- 0039: Launching block
- 003E: Landing after air guard break

- 0041: Hit while standing (during stagger?)
- 0042: Hit while standing and head bucks back
- 0043: Hit by 5B
- 0044: Hit by 5B(B)B
- 0045: Hit by 5BB(B)
- 0046: Hit by Kakashi/Kabuto 2A (low throw?)
- 0047: Hit by 2B
- 0048: Hit by a strong low

- 004F: Stagger

- 0050: Hit in the back
- 0051: Hit in the back
- 0052: Hit low in the back
- 0053: Reverse stagger
- 0054: Hit towards ground with tata or sptata
- 0056: Koro onto back
- 0058: Hit by down
- 0059: Hit by down
- 005A: About to hit the ground in hitstun (likely tech roll)
- 005B: Flying through the air from a throw
- 005D: Crumple (OTK 2X)
- 005E: Hit by Furi

- 0061: Hit by Hasa
- 0064: Hit by Kabuto sleep
- 0066: Hitting the ground in hitstun
- 0067: Coming to a stop in hitstun on back
- 0068: Coming to a stop in hitstun on face
- 0069: Hit OTG on back
- 006A: Hit OTG on face
- 006B: Standing guard break
- 006C: Death crumple with arms out
- 006D: Death crumple slow
- 006E: Rising in hitstun
- 006F: Falling in hitstun

- 0071: Getting up after being knocked down on back
- 0077: Getting up after being knocked down on face
- 007E: Sptata bounce on back
- 00F7: Sptata bounce on face

- 008E: Landing on back from air throw
- 008F: Tata bounce on face

- 0090: 5B
- 0091: 6B
- 0092: 4B
- 0093: 2B
- 0097: RB

- 00A0: 5A
- 00A1: 6A
- 00A2: 4A / Y cancel
- 00A3: 2A
- 00A7: RA

- 00B0: 2A reappear
- 00B1: A4A
- 00B3: Pulled into the ground by Kakashi 2A/ Stunned by Kabuto 2A

- 00D6: Sidestep to foreground
- 00D7: Sidestep to background
- 00D8: Running sidestep to background
- 00D9: Running sidestep to foreground

- 00F0: Generic Match beginning
- 00F1: Match opening
- 00F2: 3MC match beginning
- 00F6: Match Loss
- 00FB: Super Freeze for 5X

- 0100: 8B
- 0109: 8A

- 0110: JB (0111 and 0112 with dive kicks)

- 0121: Air RKnJ
- 012A: JA (12B and 12C for dive kicks like Sakon)

- 0130: Charge 5A
- 0131: Release 5A

- 0140: Throw
- 0141: Activated 8A going up
- 0142: Activated 8A going down
- 0143: Activated 8A landing
- 0146: Air Throw

- 0150: Entering a match

- 0160: Being grabbed
- 0166: Being air thrown
- 0167: Released from air throw
- 0168: Head buried in the ground

- 0180: Missed throw
- 0181: Missed air throw

- 01B0: 5X
- 01B3: 2X
- 01B4: 2X hit

- 01E0: 5BB(B)
- 01E1: 5BBB(B)
- 01E2: 5BBBA(A)
- 01E3: 5B(B)
- 01E4: 8B(B)
- 01E5: 5BBBA(B)
- 01E6: 2B(B)

- 01F0: Main person for 6X start
- 01F1: Second person for 6X
- 01F2: Third person for 6X
- 01F4: Main person finishing 6X

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
