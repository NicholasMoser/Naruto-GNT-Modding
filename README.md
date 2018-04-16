# Naruto GNT Hacking

Naruto Gekitō Ninja Taisen(GNT)/Clash of Ninja Hacking White Paper

## Introduction

This repository is dedicated to investigating and modding the Naruto GNT games (known as Clash of Ninja in the United States) for the Nintendo Gamecube and Wii. Most of the information you'll find here is for GNT4 and GNT Special, however much of the information has been generalized to be appropriate to any of the games. Before you begin, I would highly suggest visiting the Naruto GNT4 subreddit: https://www.reddit.com/r/GNT4/
Here you'll find a community of both modders and players interested in the game. The Discord channel in particular is good for connecting with people interested in modding the game. You can also download the most up to date Naruto GNT4 balance patch. Most of the information you'll find on this repository was discovered and written about by the various members of the Discord, so thanks to them for this :)

## Basics

For those only interested in modifying textures for an emulated copy of the GNT games you are in luck. The [Dolphin Emulator](https://dolphin-emu.org/) drastically simplifies this process with the **Dump Textures** and **Load Textures** tools. This will allow you to skip straight to the texture design process.

You can find a guide for this process here: [Dolphin Texture Loading](/general/docs/guides/dolphin_texture_loading.md)

[Naruto GNT4 English Patch](https://www.youtube.com/watch?v=d-NbZB3I4wo)

[Naruto GNT4 Gecko Codes](/gnt4/docs/guides/gecko_codes.md)

[Naruto GNT Special Gecko Codes](/gntsp/docs/guides/gecko_codes.md)

## Advanced

If you are wanting to do anything other than dumping and loading textures with Dolphin, you will need to put in some more effort. You will want to familiarize yourself with the process of hex editing and the various data formats stored in the game. You can both import and export these files by using the [GCRebuilder](https://www.google.com/search?q=gcrebuilder) with your copy of the game.

Here are various pages associated with hacking the game:

### GNT4

[Useful Addresses and Functions](/gnt4/docs/guides/addresses_and_functions.md)

[File Formats](/gnt4/docs/file_formats/formats.md)

[FPK Files](/gnt4/docs/file_formats/fpk.md)

[Sequence Files](/gnt4/docs/file_formats/seq.md)

[Background Music](/gnt4/docs/audio/bgm.md)

[DOL Hacking](/gnt4/docs/file_formats/dol.md)

### GNT Special

[Useful Addresses and Functions](/gntsp/docs/guides/addresses_and_functions.md)

[Teleport Fix](/gntsp/docs/guides/teleport_fix.md)

[Vulnerable Backstep/Sidestep](/gntsp/docs/guides/teleport_fix.md)