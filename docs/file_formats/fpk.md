# FPK Files
Naruto character data is stored in FPK files. These files are archives that contain related character data files. All Eighting games use this format. For more information on game data archives, see http://wiki.xentax.com/index.php/DGTEFF

Each entry is compress with a properietary form of PRS compression. [QuickBMS](https://www.google.com/search?q=quickbms&ie=utf-8&oe=utf-8&client=firefox-b-ab) has support for unpacking this.

### FPK Headers
The first 16 bytes in an FPK file represent the header for the file. In particular, this header describes information regarding the archive such as how many files are being stored in this single FPK file. The byte order is **Big-Endian**. 

| Offset |  Size |  Type   |  Description                                   | 
|--------|-------|---------|------------------------------------------------| 
| 0x00   |  0x04 |  UInt32 |  Left null                                     | 
| 0x04   |  0x04 |  UInt32 |  The count of all the files in the FPK archive | 
| 0x08   |  0x04 |  UInt32 |  The size of the archive header                | 
| 0x0C   |  0x04 |  UInt32 |  The size of the whole file                    | 

After the first 16 bytes, will be 32 byte headers for each archived file.

| Size |  Type   |  Description                    | 
|------|---------|---------------------------------| 
| 0x14 |  String |  Name of the entry              | 
| 0x04 |  UInt32 |  Left null                      | 
| 0x04 |  UInt32 |  Offset of to the entry         | 
| 0x04 |  UInt32 |  Compressed size of the entry   | 
| 0x04 |  UInt32 |  Uncompressed size of the entry | 


The rest of the information in the FPK file will be the data contained in each archived file. You can use the file sizes and offsets to find where each one starts and ends. 

### Character File Abbreviations
| Abbreviation | Character                  |
| :----------- | :------------------------- |
|   ank        | Anko                       |
|   bou        | Jirōbō                     |
|   cho        | Chōji                      |
|   cmn        | ???                        |
|   dog        | Akamaru                    |
|   gai        | Might Guy                  |
|   gar        | Gaara                      |
|   hak        | Haku	                    |
|   hi         | Awakened Hinata            |
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
|   na         | Kyūbi Naruto               |
|   nar        | Naruto                     |
|   nej        | Neji                       |
|   obo        | Oboro                      |
|   oro        | Orochimaru                 |
|   sa         | Sasuke CS2                 |
|   sak        | Sakura                     |
|   sar        | Sarutobi (Third Hokage)    |
|   sas        | Sasuke                     |
|   scmn       | ???                        |
|   sik        | Shikamaru                  |
|   sin        | Shino                      |
|   sko        | Sakon                      |
|   ta         | ???                        |
|   tay        | Tayuya                     |
|   tem        | Temari                     |
|   ten        | Tenten                     |
|   tsu        | Tsunade                    |
|   zab        | Zabuza                     |
  
### FPK File Contents
When you unpack an FPK file, you will find a handful of different files types that have been extracted. Different characters will have different amounts of these files.

| File Type | Purpose                                                                                        |
| :-------- | :--------------------------------------------------------------------------------------------- |
|   .dat    | HAL Labs HSD Model format                                                                      |
|   .jcv    | Potentially bones/armature for DAT files                                                       |
|   .txg    | Texture file                                                                                   |
|   .mot    | Animations                                                                                     |
|   .ptl    | Unknown                                                                                        |
|   .ref    | Unknown                                                                                        |
|   .poo    | Sound and Voice                                                                                |
|   .pro    | Sound and Voice                                                                                |
|   .sam    | Sound and Voice                                                                                |
|   .sdi    | Sound and Voice                                                                                |