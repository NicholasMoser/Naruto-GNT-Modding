# TXG Files

Archive of one or more .tpl files. TPL files are containers for one or more images.

## How to Modify

First you will need to unpack the TXG file to the TPL files it contains. This can be done with ThatTrueStruggle's [TXG2TPL](https://github.com/ThatTrueStruggle/TXG2TPL) software. You can also use [GNTool](https://github.com/NicholasMoser/GNTool) to unpack these files, which uses TXG2TPL underneath.

TPL files can be opened and modified with [BrawlBox](https://github.com/libertyernie/brawltools). Afer you have modified them, you can repack the TXG using TXG2TPL or GNTool.

## TPL Header

[TPL (File Format)](http://wiki.tockdom.com/wiki/TPL_(File_Format))

### File Header

| Offset | Size | Description                                                                |
|--------|------|----------------------------------------------------------------------------|
| 0x00   | 4    | File identifier, originally the version number. Always 0x00 0x20 0xAF 0x30 |
| 0x04   | 4    | Number of images                                                           |
| 0x08   | 4    | Offset of the Image Table (always 0x0c?)                                   |

### Image Offset Table

The image table contains one pair of values for each image:

| Offset | Size | Description                       |
|--------|------|-----------------------------------|
| 0x00   | 4    | Offset of image header.           |
| 0x04   | 4    | Offset of palette header or NULL. |

### Palette Header

The palette header usually occurs directly after the file header, at the address specified in the image offset table.

| Offset | Size | Description          |
|--------|------|----------------------|
| 0x00   | 2    | Entry Count          |
| 0x02   | 1    | Unpacked             |
| 0x03   | 1    | 1 byte of padding    |
| 0x04   | 4    | Palette Format       |
| 0x08   | 4    | Palette Data Address |

The palette data address is relative to the start of the file. The palette format values are listed below.

| Value | Name   |
|-------|--------|
| 0x00  | IA8    |
| 0x01  | RGB565 |
| 0x02  | RGB5A3 |

### Image Header

The image header normally occurs after the palette header and data. The image data usually follows, after padding to the nearest 0x20 bytes.

| Offset | Type  | Description        |
|--------|-------|--------------------|
| 0x00   | u16   | Height             |
| 0x02   | u16   | Width              |
| 0x04   | u32   | Format             |
| 0x08   | u32   | Image Data Address |
| 0x0C   | u32   | WrapS              |
| 0x10   | u32   | WrapT              |
| 0x14   | u32   | MinFilter          |
| 0x18   | u32   | MagFilter          |
| 0x1C   | float | LODBias            |
| 0x20   | u8    | EdgeLODEnable      |
| 0x21   | u8    | MinLOD             |
| 0x22   | u8    | MaxLOD             |
| 0x23   | u8    | Unpacked           |

The image data address is relative to the start of the file. The image format values are listed below.

| ID   | Name           | Bits per pixel | Block width | Block height | Block size | Type                             |
|------|----------------|----------------|-------------|--------------|------------|----------------------------------|
| 0x00 | I4             | 4              | 8           | 8            | 32 bytes   | Gray                             |
| 0x01 | I8             | 8              | 8           | 4            | 32 bytes   | Gray                             |
| 0x02 | IA4            | 8              | 8           | 4            | 32 bytes   | Gray + Alpha                     |
| 0x03 | IA8            | 16             | 4           | 4            | 32 bytes   | Gray + Alpha                     |
| 0x04 | RGB565         | 16             | 4           | 4            | 32 bytes   | Color                            |
| 0x05 | RGB5A3         | 16             | 4           | 4            | 32 bytes   | Color + Alpha                    |
| 0x06 | RGBA32 (RGBA8) | 32             | 4           | 4            | 64 bytes   | Color + Alpha                    |
| 0x08 | C4 (CI4)       | 4              | 8           | 8            | 32 bytes   | Palette (IA8, RGB565, RGB5A3)    |
| 0x09 | C8 (CI8)       | 8              | 8           | 4            | 32 bytes   | Palette (IA8, RGB565, RGB5A3)    |
| 0x0A | C14X2 (CI14x2) | 16             | 4           | 4            | 32 bytes   | Palette (IA8, RGB565, RGB5A3)    |
| 0x0E | CMPR           | 4              | 8           | 8            | 32 bytes   | Color + 1 bit Alpha (compressed) |

#### Image Format Documentation

* [I4](http://wiki.tockdom.com/wiki/Image_Formats#I4)
* [I8](http://wiki.tockdom.com/wiki/Image_Formats#I8)
* [IA4](http://wiki.tockdom.com/wiki/Image_Formats#IA4)
* [IA8](http://wiki.tockdom.com/wiki/Image_Formats#IA8)
* [RGB565](http://wiki.tockdom.com/wiki/Image_Formats#RGB565)
* [RGB5A3](http://wiki.tockdom.com/wiki/Image_Formats#RGB5A3)
* [RGBA32 (RGBA8)](http://wiki.tockdom.com/wiki/Image_Formats#RGBA32_.28RGBA8.29)
* [C4 (CI4)](http://wiki.tockdom.com/wiki/Image_Formats#C4_.28CI4.29)
* [C8 (CI8)](http://wiki.tockdom.com/wiki/Image_Formats#C8_.28CI8.29)
* [C14X2 (CI14x2)](http://wiki.tockdom.com/wiki/Image_Formats#C14X2_.28CI14x2.29)
* [CMPR](http://wiki.tockdom.com/wiki/Image_Formats#CMPR)
