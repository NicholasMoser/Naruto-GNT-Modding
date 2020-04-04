# Stage Modding

## Collision in GNT4 Stages

The collision in GNT4 is done in a unique way from other fighting games that have seperate files for collision. In GNT4 the collision is part of the bones that make up a stage model. In almost all cases, 200.dat is the model for the walls in a stage. These effectively double as collision files and can be swapped around to change collision in stages

For the Collision Viewing feature in Debug: (Stage; Touch)

**Yellow Lines**: Bones that are the boundaries of the stage, they stretch infinitely long and infinitely high. Even if they do not look it. Thus, the engine is made to only accomodate convex shaped stage layouts.

**Blue lines**: Bones that help the game inform the axis you are playing on, without these projectiles will not land and running side step will be weird

Parameters of what makes the game recognize these bones as collision and not others currently unknown. But stage shape can be manipulated extensively with the ones that already exist. As the lines are drawn by bones, these can be opened up in Blender or HSDRAW and then manipulated to change stage shape. Through creative rotating and moving of bones, custom shaped stages such as triangles have been made. Each bone has a parent which draws the yellow lines, and a child that draws the blue line. A stage can work without blue lines but not without yellow.

For reference

* 0000.dat the background of the stage
* 0100.dat the floor of the stage
* 0200.dat the walls and thus collision of a stage

Any dats beyond 0200 are additional nonessential background elements.

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
