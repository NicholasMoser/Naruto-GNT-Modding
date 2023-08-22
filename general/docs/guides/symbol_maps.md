# Symbol Maps

## General Information

A [symbol map](https://en.wikipedia.org/wiki/Symbol_table) is a description of what variables and functions exist
where in compiled code they are. GameCube and Wii games are written in C, compiled to PowerPC assembly code,
and stored in a [.dol file](/gnt4/docs/file_formats/dol.md). The `.dol` file does not include a symbol map,
and therefore we do not know where certain variables and functions are, nor what their names are.

Instead of using an official symbol map, we have community symbol maps. These are symbol maps that are
created from the ground-up using inference about what specific code does. You can find the current community
symbol maps under [general/symbol_maps](https://github.com/NicholasMoser/Naruto-GNT-Modding/tree/main/general/symbol_maps).
Each symbol map is named after its respective [Game ID](https://wiki.dolphin-emu.org/index.php?title=GameIDs)
and ending with `.map`.

## How to Use Symbol Maps in Dolphin

First, figure out if there is already a community symbol map for your game. If we look at
[Game IDs](https://wiki.dolphin-emu.org/index.php?title=GameIDs), we can see that
[Naruto GNT4](https://wiki.dolphin-emu.org/index.php?title=Naruto%3A_Gekit%C5%8D_Ninja_Taisen%21_4)
uses the Game ID **G4NJDA**, so we should download `G4NJDA.map`. Once you open the community
symbol map on Github, [here for GNT4 for example](https://github.com/NicholasMoser/Naruto-GNT-Modding/blob/main/general/symbol_maps/G4NJDA.map),
right click on the **Raw** button and select **Save Link As...** to save it somewhere.

Now in Dolphin, go to **File->Open User Folder**. If you are on an older version of Dolphin and don't have
this setting, use Windows Explorer to navigate to **C:\Users\{your user}\Documents\Dolphin Emulator**

![Open User Folder](/general/images/symbol_map/open_user_folder.png?raw=true "Hotkey Settings 1")

Once you have it open, then open the **Maps** folder and put your symbol map file in it.

![Maps Folder](/general/images/symbol_map/maps.png?raw=true "Maps Folder")

Now back in Dolphin, start up your game and it should load the symbol map automatically.
You can be 100% it is loaded by doing so manually by going to `Symbols->Load Symbol Map`

![Load Symbol Map](/general/images/symbol_map/load_symbol_map.png?raw=true "Load Symbol Map")

To actually see the symbols, you'll need to enable the **Code** view on Dolphin.
Right click on the grey bar below the Dolphin controls and select **Code**.

![Enable Code View](/general/images/symbol_map/code_view_1.png?raw=true "Enable Code View")

Now in the code view, you can see the known function names and locations under **Symbols**
as well as the current code being called under **Callstack**. These both are highlighted in
red below. Read more info on [Callstacks here](https://en.wikipedia.org/wiki/Call_stack).

![Symbols in Code View](/general/images/symbol_map/code_view_2.png?raw=true "Symbols in Code View")

## How to Use Symbol Maps in Ghidra

Make sure you follow the [Ghidra Guide](/gnt4/docs/guides/ghidra.md) first to make sure Ghidra is
set up correctly.

It is generally preferred to use a community Ghidra Zip File instead of a symbol map in Ghidra.
That is because the Ghidra Zip File contains more game information than a symbol map does.
Community Ghidra Zip Files cannot be directly linked here due to containing the code of the game.

Assuming you cannot get a Ghidra Zip File or none exists, [find](#general-information) or
[create](#how-to-create-a-new-symbol-map) a symbol map for your game. Then in Ghidra,
go to `File->Import File` and select the `.dol` file for your game. After you give it a
Program Name and hit OK it will ask for your Symbol Map. Hit Yes and select your symbol map.

Ghidra will use the symbol map to document functions and variables that it disassembles.

![Ghidra Symbols](/general/images/symbol_map/ghidra_symbols.png?raw=true "Ghidra Symbols")

## How to Create a New Symbol Map

If a symbol map doesn't exist yet for a game, you first will need to create a starting map
from Dolphin. In Dolphin run the game and go to `Symbols -> Generate Symbols From -> Signature Database`.

![Generate Symbols](/general/images/symbol_map/generate_symbols.png?raw=true "Generate Symbols")

Once that is complete go to `Symbols -> Save Symbol Map`.

![Save Symbol Map](/general/images/symbol_map/save_symbol_map.png?raw=true "Save Symbol Map")

You can find your new symbol map file in the Dolphin symbol map folder described in
[How to Use Symbol Maps in Dolphin](#how-to-use-symbol-maps-in-dolphin).

When Dolphin generates a symbol map, it will examine the code and look for patterns similar
to known GameCube/Wii SDK functions. Dolphin will almost certainly create many false positives,
so you may see many instances of the same symbol. At this point the symbol map is usable, but
you may want to use Ghidra to remove false positives and document other known functions.
