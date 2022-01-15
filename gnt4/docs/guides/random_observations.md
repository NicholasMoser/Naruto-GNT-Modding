# Random Observations

This page contains a list of random observations that may be of use for something at some point.

## Menu Debug

Some Eighting titles like [Inuyasha: Feudal Combat](https://tcrf.net/Inuyasha:_Feudal_Combat) have a debug menu usable upon starting the game.
This differs from the known GNT4 debug menu that can be used in battle. GNT4 contains many similar strings as Inuyasha for the game start
debug menu, but does not have references to any of these strings. Therefore it can be assumed that GNT4 had the game start debug menu at one
point but it was commented out. This would explain why the strings are still there.

Since these strings in GNT4 are unused they could be overwritten with data from mods. These strings are contained between 0x801fd91c and
0x801fda28 (268 bytes).

## Increasing Memory

Posting some of my notes here, I was able to find out where to increase memory for GNT4. There is a main heap that most allocations in the game uses, such as when it loads a model.

So in the below info, **Main system RAM** is how much memory the GameCube has available, **Main heap** is the main heap for loading stuff, and there are a few other heaps below it used for other system stuff.

```
Main system RAM is 24 MB (0x01800000 bytes)
Main heap uses    ~15 MB (0x00e4b000 bytes)
Graphics use    ~0.52 MB (0x00080000 bytes)
HSD FXB uses    ~0.61 MB (0x00096000 bytes)
HSD FIFO uses   ~0.52 MB (0x00080000 bytes)
* There are very likely other heaps as well that I couldn't find

I was able to bump the main heap to ~18.8 MB (0x011fb000 bytes) before it would crash on boot.
```

You can bump the main heap by about 4 MB with the following Gecko code

```gecko
0400c99c 3c600120
0400c9a0 3863b000
```

^ WARNING: Very experimental, high likelihood of breaking stuff

If you try and bump the main heap any higher than 18.8 MB, it will fail to allocate memory for the other stuff like graphics and the game will crash on boot.

I wanted to see if I could actually just tell Dolphin to make RAM larger than 24 MB. Unfortunately the way the GameCube lays out memory is kind of weird. There's data after RAM, so you'd have to push all that data even further.
Specifically:
RAM ends at 0x817FEC60 and the file system table begins (fst.bin)[1]
24 MB likely is a hard cap, looks like Dolphin can't even address above 0x817FFFFF.

[1] https://wiibrew.org/wiki/Memory_map
