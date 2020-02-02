# TRK Files

TRK files are music files, such as stage music.

## How to Listen to Them

TRK files are ADP files and can be renamed to .adp. This will allow you to listen to them using [foobar2000](https://www.foobar2000.org/) with the [foo_input_vgmstream](https://www.foobar2000.org/components/view/foo_input_vgmstream) plugin.

## How to Modify Them

You can create TRK files using the software **dtkmake** (also known as trkmake) in the official GameCube SDK. You can find it under `NINTENDO GameCube SDK 1.0\X86\bin\dtkmake.exe`. Any music you import must fit the following criteria:

* Audio sampling frequency of 32kHz or 48kHz
* Audio codec of pcm_s16le
* Audio channel of stereo
* The data subchunk located at exactly 0x24 (cannot have other metadata like LIST INFO)

You can apply these settings to an audio file using [ffmpeg](https://ffmpeg.org/). This is built into [GNTool](https://github.com/NicholasMoser/GNTool) which will make all of these changes for you to any audio file specified.

## Music List

A list of what each audio file represents and can be found here: [Background Music](/gnt4/docs/audio/bgm.md)