# Finding Opcodes

This document is a general guide to finding the location of specific opcodes in SEQ files,
such as how much chakra an attack consumes. This guide will work with any Eighting GameCube/Wii game.

## Requirements

First, you will need:

- [Dolphin Emulator](https://dolphin-emu.org/)
- [A hex editor like HxD](https://mh-nexus.de/en/downloads.php?product=HxD20)
- [SEQ Search](https://github.com/NicholasMoser/SEQ-Search/releases)

Second, you are not required to have, but will likely want:

- A [Symbol Map](/general/docs/guides/symbol_maps.md) for the respective game.

## Setup

First, figure out the memory location of something you would like to observe. For example, if you are trying
to find how much chakra an attack consumes, we will want to observe chakra. Then use the
[Finding Memory Addresses](/general/docs/guides/finding_memory.md) guide to find the memory address for that value.

## How to Find the Program Counter

Now, enable in Dolphin:

- Memory
- Breakpoints
- Code
- Registers

![Enable breakpoints](/general/images/mem/enable_breakpoints.png?raw=true "Enable breakpoints")

Select the Breakpoints tab and create a new breakpoint.

![Write breakpoint](/general/images/mem/write_breakpoint.png?raw=true "Write breakpoint")

We can create a memory read or write breakpoint to find where in the code this value is read or written to. In our case, we want to see when 0 will be written to this memory
address since that would be when chakra is used.

Now in-game, do whatever would cause the memory to be read from or written to. In our
case we will use Gaara's 5X super which should use all of the chakra.

![Breakpoint hit](/general/images/seq_search/breakpoint_hit.png?raw=true "Breakpoint hit")

Now our breakpoint has been hit. In the assembly code I can see it is doing the code
`stw r3, 0x0044 r(31)` which per
[PowerPC documentation](https://www.ibm.com/docs/vi/aix/7.1?topic=reference-appendix-f-powerpc-instructions)
will store the value of register 3 (r3) to register 31 (r31) plus an offset of 0x44.
If you look at the red line I've added to the image, it shows that r3 has 0 in it,
so we know that here we are storing 0 to chakra.

Now we need to figure out what opcode we're at. If you look at the callstack at the
top left, we can see the function calls that have gotten us to the code we are currently
at. If we have a [Symbol Map](/general/docs/guides/symbol_maps.md), we may be able
to see what opcode group this is coming from.

![Opcode group](/general/images/seq_search/opcode_group.png?raw=true "Opcode group")

What we want to do now is hit the **Step Out** button until we are back at the
`seq_parse(...)` function.

![SEQ Parse](/general/images/seq_search/seq_parse.png?raw=true "SEQ Parse")

This function is responsible for reading the opcodes from the SEQ file and executing them.
Now what we can do is hit the **Step** button until we are inside the next opcode.

![Next SEQ Opcode](/general/images/seq_search/next_seq_opcode.png?raw=true "Next SEQ Opcode")

So now we're processing the next SEQ opcode. All opcode processing functions
have the same three parameters in every Eighting game: `seq_p`, `reg_p`, and `pc`.
For our purposes, we only care about `pc`.

![Opcode Parameters](/general/images/seq_search/opcode_parameters.PNG?raw=true "Opcode Parameters")

The `pc` parameter stands for [Program Counter](https://en.wikipedia.org/wiki/Program_counter)
and is a pointer to the currently executing code in memory. For these opcode functions,
`pc` is always the third parameter and always stored in register 5 (r5). Therefore, we
can get the memory address of the current opcode in r5:

![Program Counter](/general/images/seq_search/program_counter.png?raw=true "Program Counter")

In the above image I have grabbed the value in r5 (0x9014481c) and in
Dolphin's memory tab I've pasted it in the search bar. Dolphin now will
show the hex of the current opcode being executed, 0x111e3f00 in this case.

## How to Find the SEQ File of an Opcode

Now we have a particular opcode in an SEQ file, but each opcode can show up
hundreds of times across every SEQ file. Now we can use
[SEQ Search](https://github.com/NicholasMoser/SEQ-Search/releases) to find what file
this opcode is in and at what offset in the file.

![SEQ Search Input](/general/images/seq_search/seq_search_input.png?raw=true "SEQ Search Input")

Let's start by searching the unpacked Naruto GNT Rev3 files for just the 4-byte opcode
by itself. After I hit enter:

![SEQ Search Output](/general/images/seq_search/seq_search_output.png?raw=true "SEQ Search Output")

Thousands of results return. Looks like we need to refine our query to nail down exactly
where this code is at. Back in Dolphin, I can write click on the next hex word to copy
it:

![Copy Hex](/general/images/seq_search/copy_hex.png?raw=true "Copy Hex")

I can keep copying hex after the current opcode and entering it into SEQ Search
until I have my SEQ file and offset. Eventually I'll get something like this:

![Narrow Down Search](/general/images/seq_search/narrow_down_search.png?raw=true "Narrow Down Search")

You can see above I kept adding more bytes until it only returned one SEQ file and one offset. Now I know that this opcode I am looking at is in `DATA\files\chr\gar\0000.seq`
at offset 0x7203C!

![Bytes Found](/general/images/seq_search/bytes_found.png?raw=true "Bytes Found")

However, if you remember, this isn't the original opcode we hit a breakpoint on.
This is the opcode after it. So now we just need to look at the bytes before and
see if we can identify the opcode. I remember that the original opcode was in
opcode group 36:

![Opcode group](/general/images/seq_search/opcode_group.png?raw=true "Opcode group")

So the opcode is almost certainly here:

![Opcode Found](/general/images/seq_search/opcode_found.png?raw=true "Opcode Found")
