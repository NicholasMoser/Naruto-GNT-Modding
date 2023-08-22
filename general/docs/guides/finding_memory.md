# Finding Memory Addresses

This document is a general guide to finding memory locations for things such as chakra for a character. This guide will work with any GameCube/Wii game.

## Requirements

First, you will need:

- [Dolphin Emulator](https://dolphin-emu.org/)
- [A hex editor like HxD](https://mh-nexus.de/en/downloads.php?product=HxD20)

Second, you are not required to have, but will likely want:

- [Dolphin Memory Engine](https://github.com/aldelaro5/Dolphin-memory-engine)
- [Ghidra](https://github.com/NicholasMoser/Naruto-GNT-Modding/blob/main/gnt4/docs/guides/ghidra.md)
- A [Symbol Map](/general/docs/guides/symbol_maps.md) for the respective game. 

The following guide assumes you have Dolphin Memory Engine and Ghidra, however you can use the Dolphin
built-in memory search instead of Dolphin Memory Engine which is located under
`Tools->Cheats Manager->Cheats Search`. Ghidra is only needed to better understand how and where
memory addresses are used.

## Setup

First, in Dolphin go to Hotkey Settings and bind `General->Toggle Pause` and `TAS Tools->Frame Advance`.
You will use these to step through the game frame by frame when searching memory.

![Hotkey Settings 1](/general/images/mem/hotkey_settings_1.png?raw=true "Hotkey Settings 1")

![Hotkey Settings 2](/general/images/mem/hotkey_settings_2.png?raw=true "Hotkey Settings 2")

In Dolphin Memory Engine, select **Hexidecimal** as that is generally easier to work with when looking
at memory:

![Set Hexidecimal](/general/images/mem/set_hex.png?raw=true "Set Hexidecimal")

Last, boot up Dolphin and start playing the game until you get to the point where the memory you
are looking for should be loaded. For example, if we are looking for where chakra is stored,
we need to be in a battle.

## Anchoring

Now we will start "anchoring" to find the memory address. This is what I call the process of either using
Dolphin Memory Engine or Dolphin's Cheats Search to refine a memory search until there are only a few locations
you need to check. Then you manually check those locations to confirm if they are what you are looking for.

We start by establishing a baseline. We don't know what the max chakra is, so let's start a new search using **4 bytes (Word)** and **Unknown initial value**.

![Unknown initial value](/general/images/mem/unknown_initial_value.PNG?raw=true "Unknown initial value")

This tells Dolphin Memory Engine to load all 4-byte integers from Dolphin memory with no restraints.
Max chakra may be a float, so we could also try selecting **Float** instead of **4 bytes (Word)**.

Hit the **First scan** button and it will then look something like this:

![Something like this](/general/images/mem/something_like_this.png?raw=true "Something like this")

It has now loaded all of memory, which is 23068668 4-byte integers. This is about 92 MB, which roughly correlates
to all of the Wii memory. For GameCube games it will be a lot less.

In order for Dolphin Memory Engine to show us potential memory values, we must narrow it down. We do this by doing
stuff in-game that should change the value we are interested in. So for example, if we did the initial memory
search at the start of training mode:

![Full chakra Gaara](/general/images/mem/full_chakra.png?raw=true "Full chakra Gaara")

Then we know Dolphin Memory Engine currently has a memory address with full chakra stored to it.
In-game, we can use a super to remove all of our chakra:

![No chakra Gaara](/general/images/mem/no_chakra.png?raw=true "No chakra Gaara")

Having no chakra now means that the value is probably 0. So now we can refine the search like so:

![Search for 0](/general/images/mem/search_0.PNG?raw=true "Search for 0")

After we hit **Next Scan**, it will take the previous memory addresses and see which of those are now 0.
Unfortunately, it's likely still in the millions, so we have to keep refining it.

Now if I let the chakra fill a little bit, we know that the value should be larger now:

![Some chakra Gaara](/general/images/mem/some_chakra.png?raw=true "Some chakra Gaara")

So in Dolphin Memory Engine, now I can search for values that have **Increased** since the last search:

![Search increased](/general/images/mem/search_increased.PNG?raw=true "Search increased")

Now as the chakra increases each frame, I can keep searching for **Increased**. This eventually narrows
down the values to only a handful of memory addresses:

![Narrowed down](/general/images/mem/narrowed_down.PNG?raw=true "Narrowed down")

If it doesn't, you can use the other options to help test different scenarios that the memory may
have changed (or not changed):

![Options](/general/images/mem/options.png?raw=true "Options")

## Testing a Potential Memory Address

Now we must test the potential memory addresses to see which one is the one we are looking for.
If you look at the **Current** column you can see the value it currently is, and in the **Scanned**
column we can see the last value scanned.

By resuming the game we can watch this value change live and determine if it is what we're looking for.
Furthermore, you can double click on it to add it to the watch list below:

![Watch list](/general/images/mem/watch_list.PNG?raw=true "Watch list")

Now that we have it here, we can double click on the **Value** to manually change it to see what happens in-game.
We can also select the **Lock** checkbox to prevent it from changing and see what happens in-game. We also may
change the type at this point if we realize that it may be a float or other data type.

Eventually we should be able to confirm that this memory address is the one we are looking for.

Please note that this memory address may change at any time to something else if it exists
[on the heap](https://en.wikipedia.org/wiki/Memory_management#HEAP). Most memory addresses will stay in the
same location at least during the same battle, so it should stay the same as long as you stay in the same
menu or the same battle.

## How to Find Permanent Memory Location

Since most memory locations likely exist [on the heap](https://en.wikipedia.org/wiki/Memory_management#HEAP),
we'll want to find a way to determine where it exists. Now, enable in Dolphin:

- Memory
- Breakpoints
- Code
- Registers

![Enable breakpoints](/general/images/mem/enable_breakpoints.png?raw=true "Enable breakpoints")

Select the Breakpoints tab and create a new breakpoint.

![Write breakpoint](/general/images/mem/write_breakpoint.png?raw=true "Write breakpoint")

We can create a memory read or write breakpoint to find where in the code this value is read or written to.
Since battle state is updated every frame, we should expect this to be hit every frame, possibly multiple
times a frame:

![Code stopped](/general/images/mem/code_stopped.PNG?raw=true "Code stopped")

We can now right click on this line of code and select **Copy address** and open Ghidra to view the code
at that location. Once Ghidra is open hit **G** on your keyboard and paste the address.

Now, we can begin looking at the disassembled C code and how the game actually uses this memory address,
what struct it may be stored in, etc.

![Ghidra code](/general/images/mem/ghidra_code.PNG?raw=true "Ghidra code")
