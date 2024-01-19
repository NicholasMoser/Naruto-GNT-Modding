# TCG

Eighting games since the first GNT game often refer to "TCG". For example, the SEQ interpreter contains many opcodes
used for menu logic. These include:

- seq_cmdtcg::SEQ_CmdTCGSystem
- seq_cmdtcg::SEQ_CmdTCGBranch
- seq_cmdtcg::SEQ_CmdTCGGWork
- seq_cmdtcg::SEQ_CmdTCGGReg
- seq_cmdtcg::SEQ_CmdTCGCell
- seq_cmdtcg::SEQ_CmdTCGPos
- seq_cmdtcg::SEQ_CmdTCGZoom
- seq_cmdtcg::SEQ_CmdTCGRot
- seq_cmdtcg::SEQ_CmdTCGYure
- seq_cmdtcg::SEQ_CmdTCGColor
- seq_cmdtcg::SEQ_CmdTCGJob
- seq_cmdtcg::SEQ_CmdTCGModel
- seq_cmdtcg::SEQ_CmdTCGDraw
- seq_cmdtcg::SEQ_CmdTCGTsk
- seq_cmdtcg::SEQ_CmdTCGEtc
- seq_cmdtcg::SEQ_CmdTCGEffect

These functions are of particular interest, because they seem to duplicate opcodes already provided in SEQ.
For example, the `tcg_add` opcode in `SEQ_CmdTCGGWork` could be serviced by using the `i32_add` opcode in
`SEQ_CmdI`. The difference is that TCG opcodes seem to have their own "global" and "local temporary" variables.

The best understanding of what TCG represents is a **Tiny Code Generator**. An example of this is the
[QEMU Tiny Code Generator](https://github.com/qemu/qemu/tree/master/tcg#readme). The
[documentation](https://wiki.qemu.org/Documentation/TCG) states that it exists to transform target insns
(the processor being emulated) via the TCG frontend to TCG ops which are then transformed into host insns
(the processor executing QEMU itself) via the TCG backend. QEMU was first released in 2003 and the first
GNT game was released in 2003, so it does seem to line up.

## s_lpCTD

From Doraemon, we know there's a variable called `s_lpCTD` used in many TCG functions. It's defined in the file `seq_cmdtcg.o` along
with another variable called `s_lpCTDBACKUP` (this variable is not used in GNT4). It is a pointer used to lookup variables and
globals for reading and writing.

The name `s_lpCTD` [doesn't return any results on Github](https://github.com/search?q=s_lpCTD), but [lpCTD does](https://github.com/search?q=lpCTD).
The best guess for what the name means is:

```
s_  = static
lp  = long pointer
CTD = Cell Table Data
```

The first part, `s_` makes sense considering that the variable is static and accessible from many functions. This can further be
confirmed by the variable existing in the [.sbss section](https://en.wikipedia.org/wiki/.bss).

The second part, `lp` likely is long pointer which is apparently a name derived from Windows using that name for
[far pointers](http://computer-programming-forum.com/81-vc/7c4e259370b0542a.htm) (32-bit). An example usage of this
is for the Windows data type [LPSTR](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/3f6cc0e2-1303-4088-a26b-fb9582f29197).

The third part, `CTD` has a few things it could be. The `TD` likely stands for Table Data since this is a pointer to a table of data.
Not sure what the `C` stands for though, maybe Context or Command. More likely Cell since that shows up in many related function names.

## Current Understanding

Based on known function names from the Doraemon symbol map, each graphical component is a _TCGCELL struct. These cells appear to be
initialized in the SEQ files, e.g. m_title.seq. It is likely creating some [Finite-state_machine](https://en.wikipedia.org/wiki/Finite-state_machine)
to tie the cells to each other, where certain inputs display and move certain cells. This is believed to be the case due to the fact that
we can see little SEQ code running between frames in the menus. Furthermore the text entries at the end of m_title.seq are read only
once at the title screen after hitting Start.
