# Naruto Clash of Ninja 2 Gecko Codes

These are codes that modify the game in various ways. You can add them to games by right clicking on the game in Dolphin and going to properties. Go to Gecko Codes and you can add them here by either going to Edit Config or hitting the Add button (Add button only exists in latest Dolphin versions).

## General

## Skip Intro Cutscenes [Nick]

Note: This does not skip a few of the title cards. I tried to skip them but the game would randomly crash when
loading the character select screen. The function that loads them appears to be at 0x8006a310.

```gecko
0406a9e4 60000000
0406a9f8 60000000
0406aa1c 60000000
```

## Unlock Characters and Stages [Nick]

```gecko
C206A944 00000007
3800FFFF 3C60801B
9003D2BC 9003D2C0
9003D2C4 9003D2C8
9003D2CC 9003D2D0
9003D2D4 9003D2D8
9003D2DC 9003D2E0
3C60801B 00000000
```

## Force 90 Second Matches [Nick]

```gecko
0401f0c0 38000002
```

## Force 3 Round Matches [Nick]

```gecko
0401f0c8 38000003
```
