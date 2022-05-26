# GNT4 Tournament Edition

On July 24th, 2021, a unique version of Naruto GNT4 was [uploaded to redump.org](http://redump.org/disc/81868/). It was purchased from [an Ebay listing](https://www.ebay.co.uk/itm/174820335684) and has been referred to as **Naruto: Gekitou Ninja Taisen! 4 Rev 1**. It is believed to have been a disc only printed for use in GNT4 tournaments.

- [Differences](#differences)
- [How to Play](#how-to-play)
- [Images of the TE Disc](#images-of-the-te-disc)

## Differences

The only files changed were:

- chr/kis/0000.seq
- chr/nar/0000.seq
- chr/sa2/0000.seq
- maki/char_sel.seq
- maki/charsel4.seq
- maki/m_title.seq
- bi2.bin
- boot.bin
- fst.bin

### Character Changes

Kisame, Naruto, and CS2 Sasuke were changed. Kisame and Naruto only had their combo lists changed, and were changed in a way that the display for them broke.

![ZTK Combo Changes](/gnt4/images/te/te_ztk_combos.png?raw=true "ZTK Combo Changes")

![Kisame Combo Changes](/gnt4/images/te/te_kisame_combos.png?raw=true "Kisame Combo Changes")

Please note that only the **combo lists** were changed, not the actual combos. Therefore no actual gameplay changes were made to Kisame and Naruto.

CS2 Sasuke does have a gameplay change, and it is the only change made to his SEQ file:

![CS2 Sasuke Fireball Clash](/gnt4/images/te/cs2_fireball_clash.gif?raw=true "CS2 Sasuke Fireball Clash")

Notably, two CS2 Sasuke's that use 2X against each other will not cause the fireballs to clash. This is a known glitch in the game that drastically slows the speed of the game down when performed. Now the fireballs will pass through each other.

You can see the SEQ code change for this below:

![CS2 Sasuke Code Change](/gnt4/images/te/cs2_code_change.png?raw=true "CS2 Sasuke Code Change")

### Menu Changes

`char_sel.seq` had a new function added to it at offset 0x9EC.

Before

![char_sel.seq before](/gnt4/images/te/char_sel_before.png?raw=true "char_sel.seq before")

After

![char_sel.seq after](/gnt4/images/te/char_sel_after.png?raw=true "char_sel.seq after")

## How to Play

The easiest way to play the tournament edition is to patch your [ripped copy of GNT4](https://dolphin-emu.org/docs/guides/ripping-games/). Right click on your GNT4 ISO in Dolphin and select **Properties**. Go to the **Verify** tab and hit the button **Verify Integrity**.

If the results look like this:

![Good Dump](/gnt4/images/te/good_dump.png?raw=true "Good Dump")

Download this patch: [te.xdelta](https://github.com/NicholasMoser/Naruto-GNT-Modding/releases/download/TE/te.xdelta)

If the results look like this:

![Bad Dump](/gnt4/images/te/bad_dump.png?raw=true "Bad Dump")

Download this patch: [te.xdelta](https://github.com/NicholasMoser/Naruto-GNT-Modding/releases/download/TE2/te.xdelta)

If your results do not look like either of the above two images, you will need to [rerip your GNT4 disc](https://dolphin-emu.org/docs/guides/ripping-games/).

Once you have the patch, you will need to patch it using [xdelta3](https://github.com/jmacd/xdelta-gpl/releases). Assuming your GNT4 ISO is named `GNT4.iso` and the patch is in the same directory as the ISO, you can patch it with the command:

```ps
xdelta3.exe -d -s GNT4.iso te.xdelta GNT4_TE.iso
```

This will output the tournament edition of GNT4 to the file `GNT4_TE.iso`.

## Images of the TE Disc

![TE Disc Picture 1](/gnt4/images/te/TE_1.jpg?raw=true "TE Disc Picture 1")

![TE Disc Picture 2](/gnt4/images/te/TE_2.jpg?raw=true "TE Disc Picture 2")
