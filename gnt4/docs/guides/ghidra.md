# Ghidra Guide

This page is a guide for using Ghidra to decompile GNT4. [Ghidra](https://ghidra-sre.org/) is a software reverse engineering (SRE) suite of tools developed by the NSA. It is available as free software under the 2.0 version of the Apache License.

## Getting Started

In addition to downloading Ghidra, you will need a few other things as well.

- An extracted ISO. [GNTool](https://github.com/NicholasMoser/GNTool) can do this for GameCube and [Wiimms ISO Tool](https://wit.wiimm.de/) can do this for Wii
- Download the [Gecko extension](https://github.com/aldelaro5/ghidra-gekko-broadway-lang), and follow instructions to install it.
- Download the [DOL/REL loaders](https://github.com/Cuyler36/Ghidra-GameCube-Loader), and follow instructions to install it.

On first boot, you will want to create a new project. You will want to create a **Non-Shared Project**, as a **Shared Project** requires Ghidra running on a server. Once the project is created, select `File->Import File`. Find the DOL file under the `sys` directory of the extracted ISO. It likely will be named `main.dol`.

Make sure that under Language it says `PowerPC:BE:32:Gekko_Broadway:default`. You may also want to change the name of the program in case you intend on importing other DOL files named main.dol. Select OK and it will begin processing.

Say No to importing a Symbol Map, as there is not one yet ready to be used. Double click on your new file in your new project. This will open the Ghidra editor on your project. When it opens it will ask if you would like to analyze it. Select Yes, leave the defaults as-is, and select Analyze. It will then spend a few minutes analyzing the DOL file.

## Resources

[NWPlayer123 Ghidra Documentation](https://github.com/NWPlayer123/Resources/blob/bbf25e24ed9990d6421426320ad71b7cc6b1e561/Ghidra/Ghidra.md)
