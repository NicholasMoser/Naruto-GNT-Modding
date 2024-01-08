# Replacing Models

![Chun Lee Model Replacement](/tvc/images/chun_lee.png?raw=true "Chun Lee Model Replacement")

This guide will help provide some tips for replacing a model in Tatsunoko vs Capcom. The information
present here is courtesy of Helen Homunculus.

## Requirements

- [BrawlCrate or BrawlBow](https://github.com/soopercool101/BrawlCrate).
- Unpacked `.brres` files from TvC and the other game you wish to replace the model with. You can use
  [GNTool](https://github.com/NicholasMoser/GNTool) to unpack FPK files to get these `.brres` files.

## Guide

First, open the `.brres` file for the model you wish to replace. For example, you can use Chun-Li's at
`files/chr/chu/0000.brres`.

![Guide Part 1](/tvc/images/modelswap1.png?raw=true "Guide Part 1")

Right click on the `mdl0 0000` like seen above and export as as `.mdl0`. 

Then open the `.brres` file you wish to replace it with in BrawlCrate/BrawlBox and right click the
`mdl0 0000` and select `Import Asset -> Object`. Select the `.mdl0` file you previously saved.

A window will pop up showing all the objects from the mdl0 file you can import.

![Guide Part 2](/tvc/images/modelswap2.png?raw=true "Guide Part 2")

You can scroll tbru the import drop down menu and select the models you want to import.
You will want to make sure that the base bone and skeleton bone matches. Also that the base skeleton
is set to merge, then click Okay.

The catch is that this only works well for objects that have a single bone bind, meaning its only
weighed to one bone. The hand models that chun li and lee from dbc use are bound to a single bone
whereas the lee from gnt hand model is weighed to hand bones and finger bones.

After you save the new `.brres` file you can replace it with the existing one in TvC.

![Chun Lee Model Replacement Kicking](/tvc/images/chun_lee2.png?raw=true "Chun Lee Model Replacement Kicking")
