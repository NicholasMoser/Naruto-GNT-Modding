# How to Dump Textures for a Specific Costume

First, open Dolphin and go to Options->Graphics Settings

![Graphics Settings](/general/images/dump_specific_costume/1.png?raw=true "Graphics Settings")

Then, under **Texture Dumping** select Enable, Dump Base Textures, and Dump Mip Maps.

![Enable Texture Dumping](/general/images/dump_specific_costume/2.png?raw=true "Enable Texture Dumping")

Then, go to File->Open User Folder and navigate to Dump->Textures

![Open User Folder](/general/images/dump_specific_costume/3.png?raw=true "Open User Folder")

![Open Dump](/general/images/dump_specific_costume/4.png?raw=true "Open Dump")

![Open Textures](/general/images/dump_specific_costume/5.png?raw=true "Open Textures")

Last, open the folder named after the [Game ID](https://www.gametdb.com/) of your game, such as `SG4JDA` for SCON4 or `G4NJDA` for vanilla GNT4.

![Texture Directory](/general/images/dump_specific_costume/6.png?raw=true "Texture Directory")

Now you are in the folder where textures will be dumped to. As you open and play the game in Dolphin, new textures that are loaded will be saved to this folder.

To isolate a specific costume, we must start the game and get to a point right before the textures are loaded. So for example, if we want Choji costume 3 textures, hover over Choji. Then, delete all the existing textures in the texture folder like so:

![Delete Existing Textures](/general/images/dump_specific_costume/7.png?raw=true "Delete Existing Textures")

Then, select the costume to load the textures. Dolphin will dump them out to the folder.

![Dump Textures](/general/images/dump_specific_costume/8.png?raw=true "Dump Textures")

You can now modify these textures to make them custom and load them using the guide [Dolphin Texture Loading](/general/docs/guides/dolphin_texture_loading.md).
