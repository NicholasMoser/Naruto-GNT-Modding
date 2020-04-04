# Stage Modding

## Replacing Sounds

You cannot just replace the .poo, .pro, .sam, and .sdi files from one folder to another. Each sound effect contained inside the files has an id associated with it. By copying the sound effects from one folder to another, you duplicate those sound effect ids and lose the sound effect ids of the folder copied to. This can result in sound effects breaking after leaving the stage with duplicate sound effects. Therefore, the proper way to manipulate these sounds is to do the following:

* Extract the .dsp sound files with [GNTool](https://github.com/NicholasMoser/GNTool) or [MusyX-Extract](https://github.com/Nisto/musyx-extract).
* Modify the contents of the sound files without changing the filenames (to preserve the sound effect id).
* Import the new sound files back into the .sam and .sdi files.

If you wish to simply remove sound effects from a stage, you can copy the contents of the last .dsp sound effect file into each other .dsp sound effect file. This is because the last .dsp file in each folder is a sort of "null terminator", or rather, a 0 second blank sound effect.

The sound effect id is the hex number in the .dsp filename surrounded by parentheses, e.g. `0x075C` in `00000 (0x075C).dsp`. It may be theoretically possible to add new sound effects by removing sound effects from other stages and using the ids of the removed sound effects for new ones in a given stage.

## Draw Distance

When overriding an existing stage, it is possible for some objects in the stage to unload incorrectly due to draw distance.

![Incorrect Draw Distance](/gnt4/images/gameplay/drawdistance1.gif?raw=true "Incorrect Draw Distance")

This can be fixed by modifying the draw distance values in the `0000.seq` file of the stage. By default the draw distance values are set to `0x2AAA`. This value is used in the following function:

![Draw Distance Function](/gnt4/images/functions/drawdistance.png?raw=true "Draw Distance Function")

So let's assume that our custom stage has overriden `files/stg/008`. If we open `files/stg/008/0000.seq`, we can find the draw distance for each stage object by searching for `0x2AAA`:

Offset 0x1BC

```hex
40 00 2A AA 23 0D 28 3F 00 00 00 1E // Object 1
20 00 2A AA 23 0D 28 3F 00 00 00 28 // Object 2
00 00 2A AA 23 0D 28 3F 00 00 00 32 // Object 3
E0 00 2A AA 23 0D 28 3F 00 00 00 3C // Object 4
C0 00 2A AA 23 0D 28 3F 00 00 00 46 // Object 5
A0 00 2A AA 23 0D 28 3F 00 00 00 50 // Object 6
80 00 2A AA 23 0D 28 3F 00 00 00 5A // Object 7
60 00 2A AA 04 02 28 66 00 00 00 14 // Object 8
```

These 8 sets of bytes represent the 8 objects in the stage. We can lower `0x2AAA` to `0x0000` to force them to always be loaded.

```hex
40 00 00 00 23 0D 28 3F 00 00 00 1E // Object 1
20 00 00 00 23 0D 28 3F 00 00 00 28 // Object 2
00 00 00 00 23 0D 28 3F 00 00 00 32 // Object 3
E0 00 00 00 23 0D 28 3F 00 00 00 3C // Object 4
C0 00 00 00 23 0D 28 3F 00 00 00 46 // Object 5
A0 00 00 00 23 0D 28 3F 00 00 00 50 // Object 6
80 00 00 00 23 0D 28 3F 00 00 00 5A // Object 7
60 00 00 00 04 02 28 66 00 00 00 14 // Object 8
```

Which results in the following:

![Incorrect Draw Distance](/gnt4/images/gameplay/drawdistance2.gif?raw=true "Incorrect Draw Distance")
