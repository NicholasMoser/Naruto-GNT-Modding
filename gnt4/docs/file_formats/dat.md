# DAT File

## Description

HAL Labs HSD Model format. The same model format used in Melee.

## Replacing Models

It is possible to replace models in GNT4 with models from outside GNT4. The steps below will describe how to do this.

### Required Software

* [HSDLib](https://github.com/Ploaj/HSDLib/releases)
* [Blender](https://www.blender.org/download/)*
* [io_export_objex Blender Plugin](https://github.com/CrookedPoe/io_export_objex)

\* This guide was written using Blender 2.79, but theoretically any version should work.

### Extracting the Models

After extracted with [GNTool](https://github.com/NicholasMoser/GNTool), character models can be found in: [workspace]/uncompressed/files/chr/
Each folder within the /chr/ directory is an individual character. For example, the /zab/ folder is Zabuza’s character.
In order to edit the character, we must extract the model to obtain the necessary base for our future import. How is this done? Ploaj has developed a tool named HSDRaw that thankfully supports the model format we will be looking at. Simply download the latest version from the github page linked above.

From my knowledge, the file “0000.dat” is the primary character model file. We can open this model in HSDRaw, and open the subfolders on the left-hand column until you reach a subdirectory called “RootJoint”.

Double click on “RootJoint” to open the model in the viewport on the right side of the program. Select the “DOBJs”tab, and keep track of how many objects there are in the list, we’ll need this information for later. Now we can take a look at the model, and export it for us to then use in blender. We can export the model by clicking “File” next to the viewport tab, and selecting “Export Model to File”. Simply save the model anywhere where you can keep track of it, as it is very important.

### Setting up in Blender

After you have extracted the “.dae” model of your choosing, you can import it into Blender. In doing so, it is now possible to make edits or completely replace the character.

Now that it is in Blender, it is a good time to set the skeleton to display the bone names, so we can see what bone we will be assigning to our new model’s vertices. Also, install the io_export_objex plugin, which will allow you to view what vertices are not linked to a bone, for rigging convenience.

After doing this, you should now look to deleting Bone #0, as this bone will cause importing stress in the future. This bone will not be missed.

Now then, after dealing with the stray bone, we can begin to set up our new model. First, delete the original character model, excluding the skeleton. Select your custom model, then select the skeleton, and press “ctrl+p”, selecting “Armature Deform [With Empty Groups]. This allows us to rig our custom model to the character’s skeleton.

Now that we have our custom model tied to the skeleton, we should be able to start assigning our vertices to the bones. In edit mode, select the vertices that line up with what the bone represents, and start rigging! A good tip to keep in mind is that not every bone needs to be assigned to something. I only assign bones to the major bones, so don’t worry about having to do all of them!

It is also recommended to keep the poly limit at or below 9k tris.

### Importing your model

After rigging the model and successfully testing it, it is now time to export. In blender, export as “.dae”, and in the export settings, make sure UV Maps is selected instead of Materials, if your model uses UV maps. Otherwise keep the settings default and export like usual.

With your new character model rigged and exported as “.dae”, follow the process of opening the ORIGINAL character “.dat” in HSDRaw. Now, instead of selecting “Export Model To File”, select “Import Model From File”. Find your custom character’s “.dae”, and select it. A window will appear named “Import Options”. Set “Flip UVs” to “True”, and “Apply Naruto Materials” to “True” as well. Now, your model should load in the viewport!

Make sure it is oriented properly, as the skeleton and model sometimes need to be rotated a certain way to align properly. Once you have confirmed that it is at an acceptable state, open the “DOBJs” tab. Here, what you will want to do is select “Options”, then “Add Dummy DOBJ” until your custom model has an equal amount of objects as the original model.
Now click “File” in the top left of the window and select “save”!

### Testing

After saving your new “.dat” file, make sure it has overwritten the original character “.dat” file in /chr/[character_folder]/.
Now, go to the /uncompressed/sys/ directory, and load “main.dol” in Dolphin. This will allow you to load the game with your modded files without need for recompressing your files.

Check if it works, and if so, congrats! If not, let us know in the GNT Discord so we can assist you. Thanks for reading!

Thanks to @Psi-Hate for writing the above guide!

## DAT Header

[Custom Mario Kart Wiiki Entry](http://wiki.tockdom.com/wiki/HAL_DAT_(File_Format))

The HAL Labs. HSD-Archive (*.dat) format can be described as an unordered multi-root hierarchy (tree) of various data structures.

All pointers are relative to the Data Block (0x20) except for string pointers.

NOTE: pointers and offsets are the same thing, but the term "offset" is only used to describe the data at that location.

### File Header

| Offset | Size | Format   | Description                |
|--------|------|----------|----------------------------|
| 0x00   | 4    | unsigned | File Size                  |
| 0x04   | 4    | pointer  | Pointer Table Offset       |
| 0x08   | 4    | unsigned | Pointer Count              |
| 0x0C   | 4    | unsigned | Root Node Count            |
| 0x10   | 4    | unsigned | Reference Node Count       |
| 0x14   | 4    | string   | Unknown. "001B" when used. |
| 0x18   | 4    | unsigned | Unknown. Padding?          |
| 0x1C   | 4    | unsigned | Unknown. Padding?          |

### Data Block

The Data Block consists of the data, structures, and string table in the archive.

### String Table

The String Table is an array of 0-terminated strings which the string pointers in some structs point to directly.
This array is not aligned (or allocated), and the pointer table begins directly after the last 0-termination byte.

### Pointer Table

The Pointer Table lists (points to) every valid (0x00000000 is invalid if not pointed to otherwise) pointer in the data block.
The order of the list is exactly the order of the pointers in the data block.

| Offset               | Size              | Format  | Description    |
|----------------------|-------------------|---------|----------------|
| Pointer Table Offset | Pointer Count * 4 | pointer | Pointer Offset |

### Root Nodes

This is where our journey through the data begins as these contain the data and string offsets.

| Offset | Size | Format  | Description                              |
|--------|------|---------|------------------------------------------|
| 0x00   | 4    | pointer | Data Offset                              |
| 0x04   | 4    | pointer | String Offset (relative to String Table) |

Reading the strings means reading until a stop character of '\x00'.

### Reference Nodes

Following these there is another String Table, which has no definite size and no padding.
The strings seem to be used as identifier keys for the data (similar to how a Python dict or JavaScript object identifies its data).
