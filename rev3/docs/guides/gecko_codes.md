# GNT Revolution 3 Gecko Codes

These are codes that modify the game in various ways. You can add them to games by right clicking on the game in Dolphin and going to properties. Go to Gecko Codes and you can add them here by either going to Edit Config or hitting the Add button (Add button only exists in latest Dolphin versions).

## US

### Skip Intro Cutscenes [Nick]

```gecko
c2055264 00000005  
827c0018 2c13000d  
4082000c 3a60000e  
48000010 2c130010  
40820008 3a600000  
60000000 00000000
```

### Force 60 FPS [Nick]

```gecko
041712A8 60030000
```

### X and X+Y Do Not Throw Break [Nick]

When you don't have full chakra, you can mash X for easy throw breaks. This code disables X as a throw break button completely to disable that.

When you press X+Y on the same frame your character does not do anything. X+Y is also capable of throw breaking, so you can set X+Y to a macro for easier throw breaks. This code disables X+Y as a throw break button completely to disable that.

```gecko
040739BC 54000676
C20739B8 00000004
801F0B98 700000C0
2C0000C0 4082000C
38000000 48000008
801F0B98 00000000
```

### LNP Always Activated [Nick]

```gecko
0449ee00  3f8ccccd
0449ee04  3f8ccccd
0449ee08  3f8ccccd
```

### Replace Kiba with Rogue Ninja [Nick]

```gecko
C2155014 00000003  
2C00000F 40820008  
3800002B 90040028  
60000000 00000000
```

Note: The `0F` in `2C00000F` is Kiba. Replace the `0F` with other hex values to replace other characters. The `2B` in `3800002B` is Rogue Ninja. Replace the `2B` that with other values to load other characters.

### Remove/Modify 2v2 Passive Chakra Gain [Nick]

To remove passive chakra gain for your partner in 2v2 use the below Gecko code:

```gecko
04069928 38800000
```

To modify the passive chakra gain:

```gecko
04069928 38800001
```

In the above code, the 0x1 at the end of the code is the amount of chakra to gain each frame. By default is is 0xA. The above code sets it to 0x1.
For example, to change it to 0x10 chakra per frame change it to `04069928 38800010`.

### 2v2 Rounds Set in Options [Nick]

When you set **Single or Multi Number of Rounds** in the options menu, it also applies to 2-Man Squad (2v2) modes.

```gecko
040582e8 80040c9c
```

### Modify 2v2 Rounds [Nick]

```gecko
04395b4c 00000003
```

In the above code, the 0x3 at the end of the code is the amount of rounds to change it to.

## PAL

### 60 FPS + Widescreen (PAL) [Nick]

This code makes Rev 3 PAL run in 60 FPS widescreen. This effectively changes the game from NTSC to PAL.
This is useful since the PAL version fixed a few bugs in the NTSC version such as the game crashing when
Kabuto does 2X on Kurenai. For more info see
[Regional Differences](https://tcrf.net/User:DarthDub/Naruto_Shippuden:_Clash_of_Ninja_Revolution_3#Regional_Differences).

```gecko
04172020 60000000
04172028 60000000
04172078 60000000
04172064 60000000
04172084 380002c8
041718f0 38000004
0437ae20 00000002
0437ae24 028001e0
0437ae28 01e00028
0437ae2c 00000280
0437ae30 01e00000
0437ae34 00000000
0437ae50 06060000
0437ae54 15161500
0437ae58 00000000
0437ae5c 00000008
042837d8 48000020
040000cc 00000000
04171a84 60030000
```

### Force 50 FPS (PAL) [Nick]

```gecko
04171a84 60030000
```

### Widescreen (PAL) [Nick]

```gecko
04172064 60000000
04172084 380002C8
0437ae20 00000002
0437ae24 028001e0
0437ae28 01e00028
0437ae2c 00000280
0437ae30 01e00000
0437ae34 00000000
0437ae50 06060000
0437ae54 15161500
0437ae58 00000000
0437ae5c 00000008
042837d8 48000020
```

### X and X+Y Do Not Throw Break (PAL) [Nick]

When you don't have full chakra, you can mash X for easy throw breaks. This code disables X as a throw break button completely to disable that.

When you press X+Y on the same frame your character does not do anything. X+Y is also capable of throw breaking, so you can set X+Y to a macro for easier throw breaks. This code disables X+Y as a throw break button completely to disable that.

```gecko
04073f28 54000676
C2073f24 00000004
801F0B98 700000C0
2C0000C0 4082000C
38000000 48000008
801F0B98 00000000
```

### Remove/Modify 2v2 Passive Chakra Gain (PAL) [Nick]

To remove passive chakra gain for your partner in 2v2 use the below Gecko code:

```gecko
04069e94 38800000
```

To modify the passive chakra gain:

```gecko
04069e94 38800001
```

In the above code, the 0x1 at the end of the code is the amount of chakra to gain each frame. By default is is 0xA. The above code sets it to 0x1.
For example, to change it to 0x10 chakra per frame change it to `04069928 38800010`.

### 2v2 Rounds Set in Options (PAL) [Nick]

When you set **Single or Multi Number of Rounds** in the options menu, it also applies to 2-Man Squad (2v2) modes.

```gecko
04058814 80040c9c
```

### Modify 2v2 Rounds (PAL) [Nick]

```gecko
043963cc 00000003
```

In the above code, the 0x3 at the end of the code is the amount of rounds to change it to.
