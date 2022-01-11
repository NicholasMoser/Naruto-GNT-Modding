# GNT Revolution 1 Gecko Codes

These are codes that modify the game in various ways. You can add them to games by right clicking on the game in Dolphin and going to properties. Go to Gecko Codes and you can add them here by either going to Edit Config or hitting the Add button (Add button only exists in latest Dolphin versions).

## General

### Force 60 FPS [Nick]

```gecko
041091e0 60030000
```

## Disable Stage Transition

```gecko
040b9f8c 4e800020
```

## Disable Stage Obstacles

Obstacles were hard to remove because the code of the stages forces the obstacles into the stage, unlike Rev2 and Rev3. This was addressed by making all obstacles explode upon first loading the stage. Furthermore, the sound for these obstacles exploding had to be muted or else you get a giant explosion sound when the match starts.

```gecko
040aff3c 38000001
040aff40 901f02ac
C20358A0 00000009
80630000 2C0304A2
41820034 2C0304A3
4182002C 2C0304A4
41820024 2C0304A5
4182001C 2C030480
41820014 2C030481
4182000C 2C030472
40820008 3860FFFF
60000000 00000000
```
