# SAM and SDI Files

These files are for sound and voice. They contain one or more DSP sound files.

## How to Listen to Them

You can unpack and pack SAM and SDI files with [MusyX-Extract](https://github.com/Nisto/musyx-extract). This can also be done with [GNTool](https://github.com/NicholasMoser/GNTool), which uses MusyX-Extract underneath.

You can listen to the DSP files using [foobar2000](https://www.foobar2000.org/) with the [foo_input_vgmstream](https://www.foobar2000.org/components/view/foo_input_vgmstream) plugin.

## How to Modify Them

You can create DSP files using the software **DSPADPCM** in the official GameCube SDK. You can find it under `NINTENDO GameCube SDK 1.0\X86\bin\DSPADPCM.exe`. Any sound effects you import must fit the following criteria:

* Audio sampling frequency of 32kHz
* Audio codec of pcm_s16le
* Audio channel id 0 to the output
* The data subchunk located at exactly 0x24 (cannot have other metadata like LIST INFO)

You can apply these settings to an audio file using [ffmpeg](https://ffmpeg.org/). This is built into [GNTool](https://github.com/NicholasMoser/GNTool) which will make all of these changes for you to any audio file specified.
