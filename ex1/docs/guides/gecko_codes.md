# GNT EX 1 Gecko Codes

These are codes that modify the game in various ways. You can add them to games by right clicking on the game in Dolphin and going to properties. Go to Gecko Codes and you can add them here by either going to Edit Config or hitting the Add button (Add button only exists in latest Dolphin versions).

## General

### Online Fix [Nick]

The latest Dolphin dev version currently crashes when attempting to play this game online. The following code is a hack to fix this. It has yet to be fully tested and may have unintentional side effects.

```gecko
04014840 60000000
```

## Disable Stage Transition [Nick]

```gecko
040dc720 4e800020
```

## Disable Stage Obstacles [Nick]

Obstacles were hard to remove because the code of the stages forces the obstacles into the stage, unlike Rev2 and Rev3. This was addressed by making all obstacles explode upon first loading the stage. Furthermore, the sound for these obstacles exploding had to be muted or else you get a giant explosion sound when the match starts.

```gecko
040d1200 38000001
040d1204 901f02ac
C203ED40 00000009
80630000 2C03017B
41820034 2C03017C
4182002C 2C03017D
41820024 2C03017E
4182001C 2C03014B
41820014 2C030159
4182000C 2C03015A
40820008 3860FFFF
60000000 00000000
```
