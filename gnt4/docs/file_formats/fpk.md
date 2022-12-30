# FPK Files

Naruto character data is stored in FPK files. These files are archives that contain related character data files. All Eighting games use this format. For more information on game data archives, see XeNTaX's page on [DGTEFF](http://wiki.xentax.com/index.php/DGTEFF).

Each entry is compress with a properietary form of PRS compression. [QuickBMS](https://www.google.com/search?q=quickbms) has support for unpacking this. You will need the following BMS file to extract: [naruto_fpk.bms](/utils/naruto_fpk.bms)

## FPK Headers

The first 16 bytes in an FPK file represent the header for the file. In particular, this header describes information regarding the archive such as how many files are being stored in this single FPK file. The byte order is **Big-Endian**.

| Offset | Size   | Type    | Name   | Description                                   |
|--------|--------|---------|--------|-----------------------------------------------|
| 0x00   |  0x04  | UInt32  | flag   | Left null                                     |
| 0x04   |  0x04  | UInt32  | lzs_n  | The count of all the files in the FPK archive |
| 0x08   |  0x04  | UInt32  | lzs_p  | The size of the archive header                |
| 0x0C   |  0x04  | UInt32  | size   | The size of the whole file                    |

After the first 16 bytes, will be 32 byte headers for each archived file.

| Size  | Type    | Name      | Description                    |
|-------|---------|-----------|--------------------------------|
| 0x14  | String  | name      | Name of the entry              |
| 0x04  | UInt32  | data_p    | Offset of to the entry         |
| 0x04  | UInt32  | dst_size  | Compressed size of the entry   |
| 0x04  | UInt32  | src_size  | Uncompressed size of the entry |

The rest of the information in the FPK file will be the data contained in each archived file. You can use the file sizes and offsets to find where each one starts and ends. 

## Character File Abbreviations

Please note that **cmn** is Effects and Items and is therefore not included in this list.

| Abbreviation | Character                  |
| :----------- | :------------------------- |
|   ank        | Anko                       |
|   bou        | Jirōbō                     |
|   cho        | Chōji                      |
|   dog        | Akamaru                    |
|   gai        | Might Guy                  |
|   gar        | Gaara                      |
|   hak        | Haku                       |
|   hi(2)      | Awakened Hinata            |
|   hin        | Hinata                     |
|   ino        | Ino                        |
|   iru        | Iruka                      |
|   ita        | Itachi                     |
|   jir        | Jiraiya                    |
|   kab        | Kabuto                     |
|   kak        | Kakashi                    |
|   kan        | Kankurō                    |
|   kar        | Karasu (Puppet)            |
|   kib        | Kiba                       |
|   kid        | Kidōmaru                   |
|   kim        | Kimimaro                   |
|   kis        | Kisame                     |
|   loc        | Rock Lee                   |
|   miz        | Mizuki                     |
|   na(9)      | Kyūbi Naruto               |
|   nar        | Naruto                     |
|   nej        | Neji                       |
|   obo        | Oboro                      |
|   oro        | Orochimaru                 |
|   sa(2)      | Sasuke CS2                 |
|   sak        | Sakura                     |
|   sar        | Sarutobi (Third Hokage)    |
|   sas        | Sasuke                     |
|   sik        | Shikamaru                  |
|   sin        | Shino                      |
|   sko        | Sakon                      |
|   ta(2)      | Tayuya's Doki Demon        |
|   tay        | Tayuya                     |
|   tem        | Temari                     |
|   ten        | Tenten                     |
|   tsu        | Tsunade                    |
|   zab        | Zabuza                     |
