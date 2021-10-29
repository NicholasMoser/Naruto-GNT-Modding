# SAM, SDI, POO, and PRO Files

These files are for sound and voice. They contain one or more DSP sound files. You can find the documentation for the N64/GameBoy version of [MusyX audio here](https://archive.org/details/MusyXAudioToolsForNintendo64AndGameBoy/).

## Description

### PROJ

This file contains all data about the structure of the project. This includes the information concerning what belongs to which group. Shortened to .pro

### POOL

The pool file contains all data except the samples. This includes, for example, all macros needed by the specified groups. Shortened to .poo

### SDIR

This file contains information about the location of all samples needed by the specified groups. The actual data is stored separately to make if possible to put it wherever the hardware allows. It may be stored in RAM where the CPU can reach it, but it may also be left in the ROM. Shortened to .sdi

### SAMP

This file contains the actual sample data in the format needed on the target platform. Once you have all these files converted you are ready to use them on your target platform. Shortened to .sam

## How to Listen to Them

You can unpack and pack SAM and SDI files with [MusyX-Extract](https://github.com/Nisto/musyx-extract). This can also be done with [GNTool](https://github.com/NicholasMoser/GNTool), which uses MusyX-Extract underneath.

You can listen to the DSP files using [foobar2000](https://www.foobar2000.org/) with the [foo_input_vgmstream](https://github.com/vgmstream/vgmstream/blob/master/doc/USAGE.md#foo_input_vgmstream-foobar2000-plugin) plugin.

## How to Modify Them

You can create DSP files using the software **DSPADPCM** in the official GameCube SDK. You can find it under `NINTENDO GameCube SDK 1.0\X86\bin\DSPADPCM.exe`. Any sound effects you import must fit the following criteria:

* Audio sampling frequency of 32kHz
* Audio codec of pcm_s16le
* Audio channel id 0 to the output
* The data subchunk located at exactly 0x24 (cannot have other metadata like LIST INFO)

You can apply these settings to an audio file using [ffmpeg](https://ffmpeg.org/). This is built into [GNTool](https://github.com/NicholasMoser/GNTool) which will make all of these changes for you to any audio file specified.

## POO and PRO

