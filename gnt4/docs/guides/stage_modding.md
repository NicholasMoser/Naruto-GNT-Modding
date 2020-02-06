# Stage Modding

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
