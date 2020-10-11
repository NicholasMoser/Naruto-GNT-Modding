# GNT Special Gecko Codes

These are codes that modify the game in various ways. You can add them to games by right clicking on the game in Dolphin and going to properties. Go to Gecko Codes and you can add them here by either going to Edit Config or hitting the Add button (Add button only exists in latest Dolphin versions).

## General

### Skip Intro Cutscenes [Nick]

```gecko
C21633E0 00000003
2C12000b 40820008
3A400001 9421FFF0
60000000 00000000
```

### Unlock All Characters [Nick]

```gecko
043e896c fecbfebf
043e8970 7f901f01
```

Note: You can remove or disable this code after you create/load your file, they will permanently save to your file data.

### Force 60 FPS [Nick]

```gecko
0416CBEC 60030000
```

### Teleports Use 75% of Chakra (instead of KnJ) [Nick]

```gecko
04064E04 80030044
04064E24 38001D4C
04064B9C 38001D4C
04064B3C 80630044
04064B44 80DF0040
04064B4C 907F0044
C2064B00 00000002
38800000 C8228848
60000000 00000000
```

### No Invincibility on Backsteps/Sidesteps [Nick]

```gecko
C2135B18 00000006
3C604200 60630008
7C001800 40820008
74004200 3C600200
60630008 7C001800
40820008 74000200
90050000 00000000
```
