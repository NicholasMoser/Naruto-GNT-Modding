# H4M Files

Movie files. Includes the opening, ending, Tomy and 8ing videos.

You can find the patent on Google under [Patent US6714687B2](https://www.google.com/patents/US6714687).

To decode the audio you can use [h4m_audio_decode](https://github.com/hcs64/vgm_ripping/tree/master/demux/h4m_audio_decode).

You can also find a [H4M Japanese Reference](https://web.archive.org/web/20200605164552/http://www.chaos.cs.tsukuba.ac.jp/research/index.html).

## Format Information

### File Header

The file begins with the header of 0x10 bytes. H4M Includes an extra section (MDL3) that BMD does not:

| Offset | Size(h) | Type             | Description                                   |
|--------|---------|------------------|-----------------------------------------------|
| 0x00   | 9       | String           | Magic: 'HVQM4 ' with version ('1.3') in ASCII | 
| 0x08   | 4       | Le               |                                               |
| 0x0c   | 4       | N                |                                               |
| 0x10   | 4       | 'SVR3' in ASCII. |                                               |
| 0x14   | 0C      | C                |                                               |

### Data Structures

| Offset | Integer | Use          | Description                                 |
|--------|---------|--------------|---------------------------------------------|
| 0x00   | u16     | Vertex Index | Index of Vertice for Mesh                   |
| 0x02   | u16     | Normal Index | Index of Normal for Mesh (if present)       |
| 0x04   | u16     | Color Index  | Index of Vertex Color for Mesh (if present) |
| 0x06   | u16     | U Index      | Index of U Coordinate for TexCoords         |
| 0x08   | u16     | V Index      | Index of V Coordinate for TexCoords         |

| uint   | Description                                             |
|--------|---------------------------------------------------------|
| uint8  | matrix index                                            |
| uint8  | texcoord0 matrix index?                                 |
| uint8  | texcoord1 matrix index?                                 |
| uint16 | position index                                          |
| uint16 | normal index (only present if the model has normals)    |
| uint16 | color index (only present if the model has colors)      |
| uint16 | texcoord index (only present if the model has texcoord) |


[Source](http://lmhacking.shoutwiki.com/wiki/Luigi%27s_Mansion:Docs/H4M_(File_Format))

## HVQM4 Doc: msheppard

```doc
# HVQM4: compressed movie format designed by Hudson for Nintendo GameCube
# From Mark Sheppard <msheppard@climax.co.uk>, 2002-10-03
#
0		string		HVQM4	%s
>6		string		>\0		v%s
>0		byte		x		GameCube movie,
>0x34	ubeshort	x		%d x
>0x36	ubeshort	x		%d,
>0x26	ubeshort	x		%dÂµs,
>0x42	ubeshort	0		no audio
>0x42	ubeshort	>0		%dHz audio
```

[Source](https://web.archive.org/web/20191111150851/https://assemblergames.com/threads/hvqm4-1-3.10704/)
