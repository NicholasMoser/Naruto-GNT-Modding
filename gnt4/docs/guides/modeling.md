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

Once again, the default settings should be fine.

![Import Settings](/gnt4/images/modeling/7.png?raw=true "Export Settings")

After importing, you likely will need to update the **Culling** for the Shadow Outline.

![Update Culling](/gnt4/images/modeling/8.png?raw=true "Update Culling")
