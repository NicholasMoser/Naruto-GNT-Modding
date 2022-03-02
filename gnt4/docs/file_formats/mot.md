# MOT Files

Credit to [Sifo](https://twitter.com/Zameen_Jinya) and Icylittlething for their investigation of the mot and gnta files.

MOT files contain one or more animations. They can be unpacked using QuickBMS and [naruto_mot.bms](/utils/naruto_mot.bms). Each character has a **0000.mot**, **0001.mot**, and potentially others. 0001.mot contains only a single animation, the idle animation used for the character select screen. 0000.mot contains battle animations, as well as the same idle animation in 0001.mot. You can replace animations with each other using the QuickBMS reimport option.

## GNTA Files

.gnta is an unofficial file name extension given to individual animations of a .mot file. It's unofficial since we don't know the actual name that Eighting used.

Gnta files are a series of keyframes. Keyframes are snapshots of movement at specific moments. The game will automatically fill animations in-between each keyframe. A keyframe consists of an x, y, z, and w for all applicable joints. The joint values are the same as those used in the jcv and seq files. These were originally created using the auto key feature of soft image, a now-defunct 3D modeling program. You would give it a series of poses and it would fill in animations between them for you. 3dsmax has the same feature today.

Eighting made the animations in soft image and converted them to gnta. Reason being, they wanted their animations to be recyclable across many characters. The gnta format works across jcv files. It can store bone movement data for bones, and can even do so for bones a character potentially doesn't have. This allows them to reuse the same animation across many characters with different bones.

The universal throw for example defines movements for bones 118, 119, and 120, which most characters don't have. So in this case the animation would ignore those movements for characters it does not match against. For a breakdown of bone ids see the [Bone IDs section](#Bone-IDs).

Gnta files were also designed to be able to combine, in that you can ask the game to play two at once. If the joints do not conflict, the game will do so. This is how hand animations in done in the GNT games. For example, Naruto's clone summoning animation is completely separate from the hand sign animation he does to call it.

## MOT Header

The MOT header defines one or more animation IDs. The MOT header is followed by 4-byte words for each animation ID. Each 4-byte word
is the optional offset to that animation. If there is no animation, the offset will be 0. The animation at the given offset is
a [GNTA Header](#gnta-header) (and therefore a GNTA file).

| Offset | Type | Description                                                                                        |
|--------|------|----------------------------------------------------------------------------------------------------|
| 0x00   | u16  | **Padding**: Zeros.                                                                                |
| 0x02   | u16  | **Padding**: Zeros. Set at runtime to 1 when header is initialized in `LoadObj_readMOTHeader`.     |
| 0x04   | u16  | **Padding**: Zeros.                                                                                |
| 0x06   | u16  | **Number of Animation IDs**: Total possible number of animations. May not reflect the actual size. |
| 0x08   | u32  | **Header Size**: Always 0x10.                                                                      |
| 0x0C   | u32  | **MOT File Size**                                                                                  |

## GNTA Header

A GNTA file defines one or more bone animations. The GNTA header is followed by each respective bone animation header.

| Offset | Type | Description                                                                                        |
|--------|------|----------------------------------------------------------------------------------------------------|
| 0x00   | u16  | **Padding**: Zeros.                                                                                |
| 0x02   | u16  | **Number of Bone Animations**                                                                      |
| 0x04   | u32  | **Header Size**: Always 0x10.                                                                      |
| 0x08   | f32  | **Play Speed**: Lower is bouncier. Usually is between .03 and .25.                                 |
| 0x0C   | f32  | **End Time**: Usually is between .03 and 5.0.                                                      |

## Bone Animation Header

A bone animation header defines one or more key frames for a specific bone. The header is always 0x20 bytes.

| Offset | Type | Description                                                         |
|--------|------|---------------------------------------------------------------------|
| 0x00   | u16  | **Flags**: Usually 0x0202 or 0x0000.                                |
| 0x02   | u16  | **Track Flag**: See values below.[1]                                |
| 0x04   | u16  | **Bone ID**                                                         |
| 0x06   | u16  | **Number of Key Frames**                                            |
| 0x08   | f32  | **Total Time**: `frames / 60` where 60 is the FPS.                  |
| 0x0C   | u32  | **Padding**: Zeros.                                                 |
| 0x10   | u32  | **Time Values Offset**: For each key frame.                         |
| 0x14   | u32  | **Coordinates Offset**: For each key frame.                         |
| 0x18   | u32  | **Padding**: Zeros.                                                 |

Each time value is a 32-bit float, representing the current frame count divided by 60. This is because the game runs at
60 frames per second, therefore the fractional value is in seconds.

[1] Track flag values

- `TRANSLATE = 0x01`
- `SCALE     = 0x02`
- `ROTATE    = 0x08`
- `ENABLED   = 0x20`
- `DISABLED  = 0x40`

## Bone IDs

- 0xFFFF: root?
- 0x00: Y
- 0x01: X
- 0x02: Z
- 0x03: hip
- 0x04: waist
- 0x05: breast
- 0x06: head
- 0x07: right collar
- 0x08: right high arm
- 0x09: right lower arm
- 0x0a: right hand
- 0x0b: left collar
- 0x0c: left high arm
- 0x0d: left lower arm
- 0x0e: left hand
- 0x0f: right high leg
- 0x10: right lower leg
- 0x11: right foot
- 0x12: left high leg
- 0x13: left lower leg
- 0x14: left foot
- 0x15: neck
- 0x16: ?
- 0x17: ?
- 0x18: ?
- 0x19: ?
- 0x1a: ?
- 0x1b: ?
- 0x1c: ?
- 0x1d: ?
- 0x1e: right high arm ex
- 0x1f: right high arm ex eff
- 0x20: ?
- 0x21: ?
- 0x22: ?
- 0x23: left high arm ex
- 0x24: left high arm ex eff
- 0x25: ?
- 0x26: ?
- 0x27: ?
- 0x28: right high leg EX
- 0x29: right high leg EX eff
- 0x2a: ?
- 0x2b: ?
- 0x2c: ?
- 0x2d: right toe
- 0x2e: left high leg EX
- 0x2f: left high leg EX eff
- 0x30: ?
- 0x31: ?
- 0x32: ?
- 0x33: left toe
- 0x34: ?
- 0x35: ?
- 0x36: ?
- 0x37: ?
- 0x38: ?
- 0x39: ?
- 0x3a: ?
- 0x3b: ?
- 0x3c: right thumb 1
- 0x3d: right thumb 2
- 0x3e: right thumb 3
- 0x3f: right index finger 1
- 0x40: right index finger 2
- 0x41: right index finger 3
- 0x42: right middle finger 1
- 0x43: right middle finger 2
- 0x44: right middle finger 3
- 0x45: right ring finger 1
- 0x46: right ring finger 2
- 0x47: right ring finger 3
- 0x48: right pinky 1
- 0x49: right pinky 2
- 0x4a: right pinky 3
- 0x4b: left thumb 1
- 0x4c: left thumb 2
- 0x4d: left thumb 3
- 0x4e: left index finger 1
- 0x4f: left index finger 2
- 0x50: left index finger 3
- 0x51: left middle finger 1
- 0x52: left middle finger 2
- 0x53: left middle finger 3
- 0x54: left ring finger 1
- 0x55: left ring finger 2
- 0x56: left ring finger 3
- 0x57: left pinky 1
- 0x58: left pinky 2
- 0x59: left pinky 3
- 0x5a: ?
- 0x5b: ?
- 0x5c: mouth top lip
- 0x5d: jaw
- 0x5e: mouth right side
- 0x5f: mouth left side
- 0x60: ?
- 0x61: ?
- 0x62: ?
- 0x63: ?
- 0x64: ?
- 0x65: ?
- 0x66: mouth bottom lip
- 0x67: ?
- 0x68: ?
- 0x69: ?
- 0x6a: ?
- 0x6b: ?
- 0x6c: ?
- 0x6d: ?
- 0x6e: pelvic bone?
- 0x6f: hair base
- 0x70: hair right 1
- 0x71: hair right 2
- 0x72: hair right 3
- 0x73: ?
- 0x74: hair left 1
- 0x75: hair left 2
- 0x76: hair left 3
- 0x77: upper breast
- 0x78: lower breast
- 0x79: ?
- 0x7a: ?
- 0x7b: ?
- 0x7c: ?
- 0x7d: ?
- 0x7e: ?
- 0x7f: ?
- 0x80: ?
- 0x81: ?
- 0x82: ?
- 0x83: ?
- 0x84: ?
- 0x85: ?
- 0x86: ?
- 0x87: ?
- 0x88: ?
- 0x89: ?
- 0x8a: ?
- 0x8b: ?
- 0x8c: ?
- 0x8d: ?

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
