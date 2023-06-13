# Modeling Guide

First download the latest version of [HSDRAW](https://github.com/Ploaj/HSDLib/releases).
Open a `.dat` file, and in **Nodes** on the left-hand side expand `scene_data` until you
see the RootJoint. Double click on the RootJoint to open the model.

![Expand Root Joint](/gnt4/images/modeling/1.png?raw=true "Expand Root Joint")

## Objects

Models have **Objects**. Objects can be hands, heads, limbs, etc. Two interesting objects
include the Shadow Dummy and the Shadow Outline.

![Shadow Dummy](/gnt4/images/modeling/2.PNG?raw=true "Shadow Dummy")

The Shadow Dummy is a blocky shadow outline of the character. This appears to be used for
the shadow on the ground. It is likely flattened when creating the shadow in-game.

There is also a Shadow Outline.

![Shadow Outline](/gnt4/images/modeling/3.PNG?raw=true "Shadow Outline")

These objects use [Back-face culling](https://en.wikipedia.org/wiki/Back-face_culling) to
create a dark outline on the model. Back-face culling makes the polygons facing the
camera invisible, but leaves the polygons behind them visible. This guarantees that the
model itself will always be over the Shadow Outline polygons.

## Export

You can export the model, allowing you to modify it in external programs like
[Blender](https://www.blender.org/). Go to `File->Export Model to File`

![Export Model to File](/gnt4/images/modeling/4.png?raw=true "Export Model to File")

Export it as a `.dae` file. It is recommended to create a new folder for the output,
as it will also save the respective textures used for the model.

The default settings should be fine, although you may want to select any settings
that seem relevant.

![Export Settings](/gnt4/images/modeling/5.png?raw=true "Export Settings")

## Import

After done modifying the model, you can re-import it at `File->Import Model From File`

![Import Model From File](/gnt4/images/modeling/6.png?raw=true "Import Model From File")

Once again, the default settings should be fine. It is recommended to keep the current skeleton if you get a warning for it.

![Import Settings](/gnt4/images/modeling/7.png?raw=true "Export Settings")

**Note that many of the object properties will be changed. This is because the export format does not store these properties.
You will need to compare each object to the original object properties and fix them.**

![Update Culling](/gnt4/images/modeling/8.png?raw=true "Update Culling")

After you've compared to the original model and fixed the object properties, you may notice that the new model still
doesn't appear to match the original.

![Model Not Matching](/gnt4/images/modeling/9.PNG?raw=true "Model Not Matching")

At this point you will need to change the culling on many objects. HSDRAW gets confused
and thinks the original model has `Front` culling on all objects, but the objects are
instead a mix of `None` and `Back`:

- Object 0 - `None` Culling
- Object 1 - `None` Culling
- Object 2 - `None` Culling
- Object 3 - `None` Culling
- Object 4 - `None` Culling
- Object 5 - `None` Culling
- Object 6 - `None` Culling
- Object 7 - `None` Culling
- Object 8 - `None` Culling
- Object 9 - `None` Culling
- Object 10 - `Back` Culling
- Object 11 - `None` Culling
- Object 12 - `Back` Culling
- Object 13 - `Back` Culling
- Object 14 - `Back` Culling
- Object 15 - `Back` Culling
- Object 16 - `None` Culling
- Object 17 - `Back` Culling
- Object 18 - `Back` Culling
- Object 19 - `Back` Culling
- Object 20 - `Back` Culling
- Object 21 - `Back` Culling
- Object 22 - `Back` Culling
- Object 23 - `Back` Culling

The idea being, shadows should only be visible in **Back** of non-shadows. This creates the illusion
of cell shading.

The model should now roughly match the original in HSDRAW:

![Model Matching](/gnt4/images/modeling/10.PNG?raw=true "Model Matching")
