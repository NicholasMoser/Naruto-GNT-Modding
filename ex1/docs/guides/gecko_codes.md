# GNT EX 1 Gecko Codes

These are codes that modify the game in various ways. You can add them to games by right clicking on the game in Dolphin and going to properties. Go to Gecko Codes and you can add them here by either going to Edit Config or hitting the Add button (Add button only exists in latest Dolphin versions).

## General

### Online Fix [Nick]

The latest Dolphin dev version currently crashes when attempting to play this game online. The following code is a hack to fix this. It has yet to be fully tested and may have unintentional side effects.

```hex
c2014840 00000001
60000000 00000000
```
